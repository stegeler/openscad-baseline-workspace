#!/usr/bin/env python3
"""
OpenSCAD Libraries Downloader
Downloads all official OpenSCAD libraries from their GitHub repositories
"""

import os
import subprocess
import sys
from pathlib import Path

# Library definitions with their GitHub repositories
LIBRARIES = {
    # General Purpose Libraries
    "bosl": {
        "url": "https://github.com/revarbat/BOSL.git",
        "description": "Belfry OpenScad Library v1"
    },
    "bosl2": {
        "url": "https://github.com/revarbat/BOSL2.git",
        "description": "Belfry OpenScad Library v2 (beta)"
    },
    "dotscad": {
        "url": "https://github.com/JustinSDK/dotSCAD.git",
        "description": "Mathematical 3D modeling utilities"
    },
    "nopscadlib": {
        "url": "https://github.com/nophead/NopSCADlib.git",
        "description": "Parts for 3D printers and electronics enclosures"
    },
    "ub-scad": {
        "url": "https://github.com/UBaer21/UB.scad.git",
        "description": "Full 3D printing workflow solution"
    },
    "functional-openscad": {
        "url": "https://github.com/JustinSDK/FunctionalOpenSCAD.git",
        "description": "Functional programming in OpenSCAD"
    },
    "constructive": {
        "url": "https://github.com/revarbat/Constructive.git",
        "description": "Complex mechanical parts with stamping approach"
    },
    "stoneagelib": {
        "url": "https://github.com/StoneAgeLib/StoneAgeLib.git",
        "description": "All sorts of scripts for OpenSCAD"
    },
    "bolts": {
        "url": "https://github.com/jreinhardt/BOLTS.git",
        "description": "Open Library of Technical Specifications"
    },
    "asset-collection": {
        "url": "https://github.com/JustinSDK/AssetCollection.git",
        "description": "Mechanical parts, furniture, and models"
    },
    
    # Single Topic Libraries
    "round-anything": {
        "url": "https://github.com/Irev-Dev/Round-Anything.git",
        "description": "Rounding utilities"
    },
    "marks-enclosure-helper": {
        "url": "https://github.com/MarkGalloway/EnclosureHelper.git",
        "description": "Two-piece hinged boxes"
    },
    "funcutils": {
        "url": "https://github.com/JustinSDK/funcutils.git",
        "description": "Functional programming utilities"
    },
    "threads-scad": {
        "url": "https://github.com/JohK/threads.scad.git",
        "description": "Threading library"
    },
    "smooth-primitives": {
        "url": "https://github.com/JustinSDK/SmoothPrimitives.git",
        "description": "Smooth primitives with rounded edges"
    },
    "function-plotting": {
        "url": "https://github.com/JustinSDK/FunctionPlotting.git",
        "description": "Mathematical function plotting"
    },
    "closepoints": {
        "url": "https://github.com/JustinSDK/ClosePoints.git",
        "description": "Creating shapes from point lists"
    },
    "tray-library": {
        "url": "https://github.com/JustinSDK/TrayLibrary.git",
        "description": "Tray design with subdivisions"
    },
    "yapp-generator": {
        "url": "https://github.com/YPOP/YAPP_Generator.git",
        "description": "Electronic project boxes"
    },
    "stemfie-parts": {
        "url": "https://github.com/JustinSDK/STEMFIEParts.git",
        "description": "Educational construction set parts"
    },
    "catch-n-hole": {
        "url": "https://github.com/JustinSDK/CatchNHole.git",
        "description": "Nut catches and screw holes"
    },
    "pathbuilder": {
        "url": "https://github.com/JustinSDK/Pathbuilder.git",
        "description": "Complex 2D shapes with SVG syntax"
    },
    "scon": {
        "url": "https://github.com/JustinSDK/SCON.git",
        "description": "JSON-like configuration for OpenSCAD"
    },
    "altair-2d": {
        "url": "https://github.com/JustinSDK/Altair2D.git",
        "description": "2D drawing utilities"
    }
}

def run_command(cmd, cwd=None):
    """Run a command and return success status"""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def download_library(name, info, libraries_dir):
    """Download a single library"""
    print(f"Downloading {name}: {info['description']}")
    
    lib_dir = libraries_dir / name
    if lib_dir.exists():
        print(f"  {name} already exists, updating...")
        success, stdout, stderr = run_command("git pull", cwd=lib_dir)
        if success:
            print(f"  ✓ {name} updated successfully")
        else:
            print(f"  ✗ Failed to update {name}: {stderr}")
    else:
        print(f"  Cloning {name}...")
        success, stdout, stderr = run_command(f"git clone {info['url']} {name}", cwd=libraries_dir)
        if success:
            print(f"  ✓ {name} downloaded successfully")
        else:
            print(f"  ✗ Failed to download {name}: {stderr}")

def main():
    """Main function to download all libraries"""
    script_dir = Path(__file__).parent
    workspace_dir = script_dir.parent
    libraries_dir = workspace_dir / "libraries"
    
    # Create libraries directory
    libraries_dir.mkdir(exist_ok=True)
    
    print("OpenSCAD Libraries Downloader")
    print("=" * 50)
    print(f"Downloading to: {libraries_dir}")
    print()
    
    # Check if git is available
    success, _, _ = run_command("git --version")
    if not success:
        print("Error: Git is not installed or not in PATH")
        print("Please install Git to download the libraries")
        sys.exit(1)
    
    # Download all libraries
    for name, info in LIBRARIES.items():
        download_library(name, info, libraries_dir)
        print()
    
    print("Download complete!")
    print(f"Libraries are available in: {libraries_dir}")
    print()
    print("To use a library in your OpenSCAD files:")
    print("  use <libraries/library-name/main-file.scad>")

if __name__ == "__main__":
    main()
