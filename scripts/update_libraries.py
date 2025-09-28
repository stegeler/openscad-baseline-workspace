#!/usr/bin/env python3
"""
OpenSCAD Library Update Script

This script updates all Git submodules (libraries) to their latest versions.
It provides options for updating all libraries or specific ones.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"  {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        if result.stdout:
            print(f"    {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"    ✗ Error: {e.stderr.strip()}")
        return False

def update_submodule(submodule_path, update_all=False):
    """Update a specific submodule or all submodules."""
    if update_all:
        print("Updating all OpenSCAD libraries...")
        success = run_command(
            "git submodule update --remote --merge",
            "Updating all submodules to latest versions"
        )
        if success:
            print("✓ All libraries updated successfully!")
        return success
    else:
        print(f"Updating library: {submodule_path}")
        success = run_command(
            f"git submodule update --remote --merge {submodule_path}",
            f"Updating {submodule_path}"
        )
        if success:
            print(f"✓ {submodule_path} updated successfully!")
        return success

def show_library_status():
    """Show the current status of all submodules."""
    print("Current library status:")
    try:
        result = subprocess.run("git submodule status", shell=True, capture_output=True, text=True, check=True)
        for line in result.stdout.strip().split('\n'):
            if line.strip():
                parts = line.split()
                commit = parts[0]
                path = parts[1]
                name = parts[2] if len(parts) > 2 else path
                
                # Determine if submodule is up to date
                status = "✓" if not commit.startswith('-') else "⚠"
                print(f"  {status} {path}: {name}")
    except subprocess.CalledProcessError as e:
        print(f"Error getting submodule status: {e.stderr}")

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("OpenSCAD Library Update Script")
        print("Usage:")
        print("  python3 update_libraries.py all          - Update all libraries")
        print("  python3 update_libraries.py status       - Show library status")
        print("  python3 update_libraries.py <library>    - Update specific library")
        print("")
        print("Available libraries:")
        print("  bosl2, dotscad, round-anything, nopscadlib, bosl")
        return

    command = sys.argv[1].lower()
    
    # Change to workspace root directory
    script_dir = Path(__file__).parent
    workspace_root = script_dir.parent
    os.chdir(workspace_root)
    
    if command == "all":
        update_submodule(None, update_all=True)
    elif command == "status":
        show_library_status()
    elif command in ["bosl2", "dotscad", "round-anything", "nopscadlib", "bosl"]:
        update_submodule(f"libraries/{command}")
    else:
        print(f"Unknown library: {command}")
        print("Available libraries: bosl2, dotscad, round-anything, nopscadlib, bosl")

if __name__ == "__main__":
    main()
