#!/usr/bin/env python3
"""
OpenSCAD Project Creator
Create a new project from template
"""

import os
import sys
from pathlib import Path
import shutil
from datetime import datetime

def create_project(project_name, description=""):
    """Create a new OpenSCAD project"""
    script_dir = Path(__file__).parent
    workspace_dir = script_dir.parent
    projects_dir = workspace_dir / "projects"
    templates_dir = workspace_dir / "templates"
    
    # Create projects directory if it doesn't exist
    projects_dir.mkdir(exist_ok=True)
    
    # Create project directory
    project_dir = projects_dir / project_name
    if project_dir.exists():
        print(f"Error: Project '{project_name}' already exists")
        return False
    
    project_dir.mkdir()
    
    # Copy template file
    template_file = templates_dir / "project_template.scad"
    project_file = project_dir / f"{project_name}.scad"
    
    if template_file.exists():
        shutil.copy2(template_file, project_file)
        
        # Update template with project information
        content = project_file.read_text()
        content = content.replace("My Project", project_name)
        content = content.replace("Description of your project", description)
        content = content.replace("Your Name", "OpenSCAD User")
        content = content.replace("1.0.0", "1.0.0")
        
        project_file.write_text(content)
        
        print(f"✓ Project '{project_name}' created successfully")
        print(f"  Location: {project_dir}")
        print(f"  Main file: {project_file}")
        print()
        print("Next steps:")
        print(f"  1. Open {project_file}")
        print(f"  2. Customize the parameters section")
        print(f"  3. Uncomment the libraries you need")
        print(f"  4. Start designing!")
        
        return True
    else:
        print(f"Error: Template file not found: {template_file}")
        return False

def list_projects():
    """List all existing projects"""
    script_dir = Path(__file__).parent
    workspace_dir = script_dir.parent
    projects_dir = workspace_dir / "projects"
    
    if not projects_dir.exists():
        print("No projects directory found")
        return
    
    projects = [d for d in projects_dir.iterdir() if d.is_dir()]
    
    if not projects:
        print("No projects found")
        return
    
    print("Existing Projects:")
    print("=" * 20)
    
    for project in sorted(projects):
        scad_files = list(project.glob("*.scad"))
        print(f"📁 {project.name}")
        if scad_files:
            print(f"   Files: {len(scad_files)} .scad files")
        else:
            print("   Files: No .scad files")
        print(f"   Path: {project}")
        print()

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 create_project.py <project_name> [description]  # Create new project")
        print("  python3 create_project.py list                          # List existing projects")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "list":
        list_projects()
    else:
        project_name = command
        description = sys.argv[2] if len(sys.argv) > 2 else ""
        create_project(project_name, description)

if __name__ == "__main__":
    main()
