// OpenSCAD Library Examples
// This file demonstrates how to use various OpenSCAD libraries

// Uncomment the library you want to test:

// BOSL2 Examples
// use <../libraries/bosl2/attachments.scad>
// use <../libraries/bosl2/shapes.scad>
// use <../libraries/bosl2/distributors.scad>

// Round Anything Examples
// use <../libraries/round-anything/round_anything.scad>

// threads.scad Examples
// use <../libraries/threads-scad/threads.scad>

// dotSCAD Examples
// use <../libraries/dotscad/src/round_corners.scad>
// use <../libraries/dotscad/src/bezier_curve.scad>

// NopSCADlib Examples
// use <../libraries/nopscadlib/core.scad>

// ===========================================
// BOSL2 Examples (uncomment to use)
// ===========================================

// Rounded cube with BOSL2
// rounded_cube([50, 30, 20], r=5, center=true);

// Cylinder with rounded edges
// cyl(h=30, d=20, rounding=3);

// Attachments (for connecting parts)
// attach(TOP) {
//     cube([20, 20, 20], center=true);
// }

// ===========================================
// Round Anything Examples (uncomment to use)
// ===========================================

// Round a cube
// round_cube([40, 40, 40], r=5);

// Round a cylinder
// round_cylinder(h=30, r=10, r2=3);

// Round a polygon
// round_polygon(points=[[0,0], [20,0], [10,20]], r=2);

// ===========================================
// threads.scad Examples (uncomment to use)
// ===========================================

// Metric thread
// metric_thread(diameter=8, pitch=1.25, length=20);

// Internal thread (nut)
// metric_thread(diameter=8, pitch=1.25, length=10, internal=true);

// ===========================================
// dotSCAD Examples (uncomment to use)
// ===========================================

// Bezier curve
// bezier_curve([0, 0, 0], [10, 10, 5], [20, 5, 10], [30, 0, 0], 20);

// Round corners
// round_corners([[0,0], [20,0], [20,20], [0,20]], 3);

// ===========================================
// NopSCADlib Examples (uncomment to use)
// ===========================================

// Screw holes
// screw_hole(M3_cap_screw, 10);

// PCB standoffs
// pcb_spacer(M3_standoff, 10);

// Default example (basic cube)
cube([20, 20, 20], center=true);
