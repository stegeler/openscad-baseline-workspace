# OpenSCAD Workspace Forking Workflow

This document explains how to use this baseline OpenSCAD workspace as a foundation for new projects by forking it on GitHub.

## 🚀 Quick Start - Creating a New Project

### 1. Fork the Baseline Repository
1. Go to your baseline repository on GitHub
2. Click the "Fork" button in the top-right corner
3. Choose your GitHub account as the destination
4. Give it a descriptive name (e.g., `my-phone-stand-project`)

### 2. Clone Your Fork Locally
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_PROJECT_NAME.git
cd YOUR_PROJECT_NAME
```

### 3. Create Your Project
```bash
# Create a new project using the template
python3 scripts/create_project.py my_awesome_design "Description of my design"

# Start designing!
cd projects/my_awesome_design/
```

## 📋 Complete Workflow

### Step 1: Fork the Repository
- **Purpose**: Create an independent copy for your specific project
- **Benefits**: 
  - All libraries and tools pre-configured
  - Professional project structure
  - Version control from day one

### Step 2: Customize for Your Project
```bash
# Update project metadata
# Edit README.md with your project description
# Customize .gitignore if needed for specific file types
```

### Step 3: Start Designing
```bash
# Use the project creation script
python3 scripts/create_project.py project_name "Project description"

# Or manually create projects in the projects/ directory
```

### Step 4: Development Workflow
```bash
# Regular development cycle
git add .
git commit -m "Add new feature: description"
git push origin main

# Render and test
python3 scripts/render_preview.py projects/my_project/my_project.scad
```

### Step 5: Publishing Your Design
- Push your final design to GitHub
- Create releases for different versions
- Share the repository with others

## 🎯 Best Practices

### Repository Naming
- Use descriptive names: `phone-stand-v2`, `raspberry-pi-case`
- Include version numbers for iterations
- Use kebab-case (lowercase with hyphens)

### Project Organization
- One repository per design/project
- Keep the baseline workspace clean
- Use the `projects/` directory for your designs
- Document your design process in README.md

### Version Control
- Commit frequently with descriptive messages
- Use semantic versioning for releases
- Tag major milestones
- Keep a changelog

### Library Management
- Only add new libraries if absolutely necessary
- Document why you added specific libraries
- Consider creating a separate branch for experimental libraries

## 🔧 Advanced Usage

### Adding Custom Libraries
```bash
# Download a new library manually
cd libraries/
git clone https://github.com/user/library-name.git
# Update LIBRARY_STATUS.md with new library info
```

### Updating from Baseline
```bash
# Add baseline as upstream remote
git remote add upstream https://github.com/BASELINE_USER/openscad-baseline.git

# Fetch updates from baseline
git fetch upstream

# Merge updates (be careful with conflicts)
git merge upstream/main
```

### Creating a Template from Your Project
If you create a design that could be useful for other projects:
1. Clean up project-specific files
2. Create a new branch called `template`
3. Document the template usage
4. Push the template branch

## 📁 Project Structure After Forking

```
your-project-repo/
├── libraries/           # All OpenSCAD libraries (don't modify)
├── projects/           # Your design projects
│   └── your-design/   # Your specific design
├── scripts/            # Utility scripts (don't modify)
├── templates/          # Project templates (don't modify)
├── utils/              # Common utilities (don't modify)
├── examples/           # Example designs (don't modify)
├── README.md           # Update with your project info
├── .gitignore          # OpenSCAD-specific ignores
└── LIBRARY_STATUS.md   # Library documentation
```

## 🎨 Example Project Workflow

### Creating a Phone Stand Project
```bash
# 1. Fork the baseline repository as "phone-stand-project"
# 2. Clone locally
git clone https://github.com/YOUR_USERNAME/phone-stand-project.git
cd phone-stand-project

# 3. Create the project
python3 scripts/create_project.py phone_stand "Adjustable phone stand for desk"

# 4. Start designing
cd projects/phone_stand/
# Edit phone_stand.scad with your design

# 5. Test and iterate
python3 scripts/render_preview.py phone_stand.scad --watch

# 6. Commit your work
git add .
git commit -m "Initial phone stand design"
git push origin main
```

## 🔄 Maintaining Your Fork

### Regular Updates
- Update libraries periodically using `scripts/library_manager.py`
- Sync with baseline repository for improvements
- Keep your design files organized

### Backup Strategy
- GitHub provides automatic backup
- Consider creating releases for stable versions
- Export important designs as STL files

## 📚 Resources

- [OpenSCAD Documentation](https://openscad.org/documentation.html)
- [GitHub Forking Guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [OpenSCAD Libraries](https://openscad.org/libraries.html)

## 🆘 Troubleshooting

### Common Issues
1. **Library conflicts**: Check LIBRARY_STATUS.md for available libraries
2. **Git conflicts**: Use `git status` to identify issues
3. **Rendering problems**: Ensure OpenSCAD is properly installed

### Getting Help
- Check the baseline repository issues
- Consult OpenSCAD community forums
- Review library documentation
