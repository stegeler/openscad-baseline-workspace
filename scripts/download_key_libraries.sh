#!/bin/bash

# OpenSCAD Key Libraries Downloader
# Downloads the most essential OpenSCAD libraries

LIBRARIES_DIR="../libraries"
mkdir -p "$LIBRARIES_DIR"

echo "Downloading key OpenSCAD libraries..."

# BOSL2 - Most comprehensive library
echo "Downloading BOSL2..."
if [ -d "$LIBRARIES_DIR/bosl2" ]; then
    cd "$LIBRARIES_DIR/bosl2" && git pull && cd - > /dev/null
else
    git clone https://github.com/revarbat/BOSL2.git "$LIBRARIES_DIR/bosl2"
fi

# Round Anything - Essential for rounded shapes
echo "Downloading Round Anything..."
if [ -d "$LIBRARIES_DIR/round-anything" ]; then
    cd "$LIBRARIES_DIR/round-anything" && git pull && cd - > /dev/null
else
    git clone https://github.com/Irev-Dev/Round-Anything.git "$LIBRARIES_DIR/round-anything"
fi

# threads.scad - For threaded parts
echo "Downloading threads.scad..."
if [ -d "$LIBRARIES_DIR/threads-scad" ]; then
    cd "$LIBRARIES_DIR/threads-scad" && git pull && cd - > /dev/null
else
    git clone https://github.com/JohK/threads.scad.git "$LIBRARIES_DIR/threads-scad"
fi

# NopSCADlib - For 3D printing parts
echo "Downloading NopSCADlib..."
if [ -d "$LIBRARIES_DIR/nopscadlib" ]; then
    cd "$LIBRARIES_DIR/nopscadlib" && git pull && cd - > /dev/null
else
    git clone https://github.com/nophead/NopSCADlib.git "$LIBRARIES_DIR/nopscadlib"
fi

# dotSCAD - Mathematical utilities
echo "Downloading dotSCAD..."
if [ -d "$LIBRARIES_DIR/dotscad" ]; then
    cd "$LIBRARIES_DIR/dotscad" && git pull && cd - > /dev/null
else
    git clone https://github.com/JustinSDK/dotSCAD.git "$LIBRARIES_DIR/dotscad"
fi

echo "Download complete!"
echo "Key libraries are now available in the libraries/ directory"
