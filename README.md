# OpenSCAD Workspace

A comprehensive OpenSCAD development workspace with all popular libraries, tools, and utilities pre-configured for rapid prototyping and design iteration.

## 🚀 Quick Start

1. **Create a new project:**
   ```bash
   python3 scripts/create_project.py my_awesome_design "My awesome 3D design"
   ```

2. **Open the project file:**
   - Navigate to `projects/my_awesome_design/my_awesome_design.scad`
   - Open in Cursor for preview capabilities

3. **Start designing:**
   - Uncomment the libraries you need in the imports section
   - Customize the parameters
   - Build your design!

## 📚 Available Libraries

This workspace includes the most popular OpenSCAD libraries as **Git submodules**, linking directly to their GitHub repositories:

- **BOSL2** - Most comprehensive library with utilities for shapes, transforms, threading
- **dotSCAD** - Mathematical 3D modeling utilities
- **Round Anything** - Essential rounding utilities
- **NopSCADlib** - Parts for 3D printers and electronics enclosures
- **BOSL** - Original BOSL library

### 🔄 Library Management

Libraries are managed as Git submodules, which means:

- **Always up-to-date**: Libraries are linked to their source repositories
- **Easy updates**: Use `git submodule update --remote` to get latest versions
- **Clean repository**: No static copies cluttering your workspace
- **Version control**: Each submodule tracks a specific commit for stability

### 📥 Updating Libraries

To update all libraries to their latest versions:

```bash
# Update all submodules to latest commits
git submodule update --remote --merge

# Or use the convenience script
python3 scripts/update_libraries.py all

# Update a specific library
python3 scripts/update_libraries.py bosl2
```

## 🛠️ Tools & Scripts

### Project Management
- `scripts/create_project.py` - Create new projects from template
- `scripts/library_manager.py` - Manage and update libraries
- `scripts/download_libraries.py` - Download all popular libraries

### Rendering & Preview
- `scripts/render_preview.py` - Render OpenSCAD files to STL/PNG
- Auto-preview in Cursor (when OpenSCAD extension is installed)

### Library Management
```bash
# List all libraries
python3 scripts/library_manager.py list

# Update a specific library
python3 scripts/library_manager.py update bosl2

# Update all libraries
python3 scripts/library_manager.py update-all
```

## 🎯 Features

### ✅ Pre-configured Environment
- All popular OpenSCAD libraries downloaded and ready
- Cursor workspace settings for optimal OpenSCAD development
- Project templates for quick start

### ✅ Preview Capabilities
- Real-time preview in Cursor (with OpenSCAD extension)
- Automatic rendering to STL and PNG
- Watch mode for auto-rendering on file changes

### ✅ Library Management
- Automated library downloading and updating
- Library status tracking
- Comprehensive library documentation

### ✅ Project Templates
- Structured project templates
- Best practices built-in
- Easy customization

## 📁 Workspace Structure

```
openscad-workspace/
├── libraries/           # All OpenSCAD libraries
├── projects/           # Your design projects
├── templates/          # Project templates
├── scripts/            # Utility scripts
├── utils/              # Common utility modules
├── examples/           # Example designs
└── .vscode/           # Cursor workspace settings
```

## 🔧 Setup Instructions

### Prerequisites
- OpenSCAD installed (`brew install openscad` on macOS)
- Python 3.x
- Git

### Initial Setup
1. Clone this workspace
2. Run the library downloader:
   ```bash
   python3 scripts/download_libraries.py
   ```
3. Install OpenSCAD extension in Cursor
4. Start creating projects!

### Cursor Extensions
Recommended extensions for optimal experience:
- OpenSCAD Language Support
- OpenSCAD Preview
- OpenSCAD

## 🎨 Example Usage

### Basic Project Creation
```bash
# Create a new project
python3 scripts/create_project.py phone_stand "A phone stand design"

# Navigate to the project
cd projects/phone_stand/

# Open the main file
open phone_stand.scad
```

### Using Libraries
```openscad
// In your .scad file
use <../libraries/bosl2/BOSL2.scad>;
use <../libraries/round-anything/round_anything.scad>;

// Your design code here
```

### Rendering
```bash
# Render once
python3 scripts/render_preview.py projects/my_project/my_project.scad

# Watch and auto-render
python3 scripts/render_preview.py projects/my_project/my_project.scad --watch
```

## 🔄 Workflow

1. **Create** a new project using the template
2. **Import** the libraries you need
3. **Design** your 3D model
4. **Preview** in Cursor or render to files
5. **Iterate** and refine your design
6. **Export** to STL for 3D printing

## 📖 Resources

- [OpenSCAD Documentation](https://openscad.org/documentation.html)
- [BOSL2 Documentation](https://github.com/revarbat/BOSL2)
- [OpenSCAD Cheat Sheet](https://openscad.org/cheatsheet/)

## 🤝 Contributing

This workspace is designed to be forked and customized for your specific needs. Feel free to:
- Add more libraries to the downloader
- Improve the project templates
- Add new utility scripts
- Enhance the documentation

## 📄 License

This workspace template is open source. Individual libraries maintain their own licenses.