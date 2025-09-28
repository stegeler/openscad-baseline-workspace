/*
 * OpenSCAD Project Template
 * Copy this file to start a new project
 */

// =============================================================================
// PROJECT CONFIGURATION
// =============================================================================

// Project metadata
PROJECT_NAME = "My Project";
PROJECT_VERSION = "1.0.0";
PROJECT_AUTHOR = "Your Name";
PROJECT_DESCRIPTION = "Description of your project";

// =============================================================================
// LIBRARY IMPORTS
// =============================================================================

// Core libraries (uncomment as needed)
// use <../libraries/bosl2/BOSL2.scad>;           // Most comprehensive library
// use <../libraries/dotscad/dotSCAD.scad>;       // Mathematical utilities
// use <../libraries/round-anything/round_anything.scad>; // Rounding utilities
// use <../libraries/nopscadlib/NopSCADlib.scad>; // 3D printing parts
// use <../libraries/bolts/bolts.scad>;           // Hardware specifications

// Local utilities
use <../utils/common_modules.scad>;

// =============================================================================
// PARAMETERS
// =============================================================================

// Main dimensions
width = 50;
height = 30;
depth = 20;

// Design parameters
wall_thickness = 2;
corner_radius = 3;
hole_diameter = 5;

// Quality settings
$fn = 50;  // Fragment number for smooth curves

// =============================================================================
// MODULES
// =============================================================================

module main_object() {
    difference() {
        // Outer shape
        rounded_rectangle(width, height, depth, corner_radius);
        
        // Inner cavity
        translate([0, 0, wall_thickness]) {
            rounded_rectangle(
                width - 2*wall_thickness,
                height - 2*wall_thickness,
                depth,
                corner_radius - wall_thickness
            );
        }
        
        // Holes or cutouts
        translate([0, 0, -1]) {
            cylinder(h=depth+2, d=hole_diameter);
        }
    }
}

module decorative_element() {
    // Add decorative elements here
    translate([0, 0, depth/2 + 2]) {
        star(8, 4, 5, 2);
    }
}

// =============================================================================
// MAIN ASSEMBLY
// =============================================================================

// Uncomment the parts you want to include
main_object();
// decorative_element();

// =============================================================================
// ANIMATION (for preview)
// =============================================================================

// Uncomment for animated preview
// $t = time;  // Animation parameter
// rotate([0, 0, $t * 360]) {
//     main_object();
// }

// =============================================================================
// DEBUGGING
// =============================================================================

// Uncomment for debugging
// %main_object();  // Ghost view
// #decorative_element();  // Highlight view
