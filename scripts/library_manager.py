#!/usr/bin/env python3
"""
OpenSCAD Library Manager
Manage and update OpenSCAD libraries
"""

import os
import subprocess
import sys
import json
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def get_library_status(libraries_dir):
    """Get status of all libraries"""
    libraries = {}
    
    for lib_dir in libraries_dir.iterdir():
        if lib_dir.is_dir() and lib_dir.name != ".git":
            # Check if it's a git repository
            git_dir = lib_dir / ".git"
            if git_dir.exists():
                # Get current commit
                success, stdout, stderr = run_command("git rev-parse HEAD", cwd=lib_dir)
                if success:
                    current_commit = stdout.strip()
                else:
                    current_commit = "unknown"
                
                # Get remote URL
                success, stdout, stderr = run_command("git remote get-url origin", cwd=lib_dir)
                if success:
                    remote_url = stdout.strip()
                else:
                    remote_url = "unknown"
                
                libraries[lib_dir.name] = {
                    "path": str(lib_dir),
                    "status": "installed",
                    "commit": current_commit,
                    "remote": remote_url
                }
            else:
                libraries[lib_dir.name] = {
                    "path": str(lib_dir),
                    "status": "not_git",
                    "commit": "unknown",
                    "remote": "unknown"
                }
    
    return libraries

def update_library(lib_name, libraries_dir):
    """Update a specific library"""
    lib_dir = libraries_dir / lib_name
    
    if not lib_dir.exists():
        print(f"Library {lib_name} not found")
        return False
    
    print(f"Updating {lib_name}...")
    success, stdout, stderr = run_command("git pull", cwd=lib_dir)
    
    if success:
        print(f"  ✓ {lib_name} updated successfully")
        return True
    else:
        print(f"  ✗ Failed to update {lib_name}: {stderr}")
        return False

def list_libraries(libraries_dir):
    """List all available libraries"""
    libraries = get_library_status(libraries_dir)
    
    print("OpenSCAD Libraries Status")
    print("=" * 50)
    
    if not libraries:
        print("No libraries found")
        return
    
    for name, info in sorted(libraries.items()):
        status_icon = "✓" if info["status"] == "installed" else "?"
        print(f"{status_icon} {name}")
        print(f"  Path: {info['path']}")
        print(f"  Status: {info['status']}")
        if info["remote"] != "unknown":
            print(f"  Remote: {info['remote']}")
        if info["commit"] != "unknown":
            print(f"  Commit: {info['commit'][:8]}")
        print()

def main():
    """Main function"""
    script_dir = Path(__file__).parent
    workspace_dir = script_dir.parent
    libraries_dir = workspace_dir / "libraries"
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 library_manager.py list                    # List all libraries")
        print("  python3 library_manager.py update <library>       # Update specific library")
        print("  python3 library_manager.py update-all             # Update all libraries")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        list_libraries(libraries_dir)
    elif command == "update":
        if len(sys.argv) < 3:
            print("Please specify a library name")
            sys.exit(1)
        lib_name = sys.argv[2]
        update_library(lib_name, libraries_dir)
    elif command == "update-all":
        libraries = get_library_status(libraries_dir)
        for lib_name in libraries.keys():
            update_library(lib_name, libraries_dir)
            print()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
