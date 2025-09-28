#!/usr/bin/env python3
"""
OpenSCAD Preview Renderer
Automatically renders OpenSCAD files for preview in Cursor
"""

import os
import subprocess
import sys
from pathlib import Path
import time

def run_command(cmd, cwd=None):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def render_scad_file(scad_file, output_dir="renders"):
    """Render an OpenSCAD file to STL and PNG"""
    scad_path = Path(scad_file)
    
    if not scad_path.exists():
        print(f"Error: File {scad_file} does not exist")
        return False
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Generate output filenames
    base_name = scad_path.stem
    stl_file = output_path / f"{base_name}.stl"
    png_file = output_path / f"{base_name}.png"
    
    print(f"Rendering {scad_file}...")
    
    # Render to STL
    print("  Generating STL...")
    success, stdout, stderr = run_command(
        f"openscad -o {stl_file} {scad_file}",
        cwd=scad_path.parent
    )
    
    if not success:
        print(f"  ✗ STL generation failed: {stderr}")
        return False
    else:
        print(f"  ✓ STL generated: {stl_file}")
    
    # Render to PNG (preview)
    print("  Generating PNG preview...")
    success, stdout, stderr = run_command(
        f"openscad -o {png_file} --render --imgsize=800,600 {scad_file}",
        cwd=scad_path.parent
    )
    
    if not success:
        print(f"  ✗ PNG generation failed: {stderr}")
        return False
    else:
        print(f"  ✓ PNG preview generated: {png_file}")
    
    return True

def watch_and_render(scad_file):
    """Watch an OpenSCAD file and auto-render on changes"""
    scad_path = Path(scad_file)
    if not scad_path.exists():
        print(f"Error: File {scad_file} does not exist")
        return
    
    print(f"Watching {scad_file} for changes...")
    print("Press Ctrl+C to stop")
    
    last_modified = 0
    
    try:
        while True:
            current_modified = scad_path.stat().st_mtime
            
            if current_modified > last_modified:
                print(f"\n{time.strftime('%H:%M:%S')} - File changed, rendering...")
                render_scad_file(scad_file)
                last_modified = current_modified
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping watch mode...")

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 render_preview.py <file.scad>           # Render once")
        print("  python3 render_preview.py <file.scad> --watch   # Watch and auto-render")
        sys.exit(1)
    
    scad_file = sys.argv[1]
    watch_mode = len(sys.argv) > 2 and sys.argv[2] == "--watch"
    
    # Check if OpenSCAD is available
    success, _, _ = run_command("openscad --version")
    if not success:
        print("Error: OpenSCAD is not installed or not in PATH")
        print("Please install OpenSCAD to use this tool")
        sys.exit(1)
    
    if watch_mode:
        watch_and_render(scad_file)
    else:
        render_scad_file(scad_file)

if __name__ == "__main__":
    main()
