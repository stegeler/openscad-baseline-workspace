// Parametric Design Example
// This shows how to create customizable designs with parameters

// Parameters - adjust these values to customize the design
width = 30;
height = 20;
depth = 15;
wall_thickness = 2;
corner_radius = 3;

// Main box with rounded corners
module rounded_box(w, h, d, r) {
    hull() {
        for (x = [-w/2 + r, w/2 - r]) {
            for (y = [-h/2 + r, h/2 - r]) {
                translate([x, y, 0]) {
                    cylinder(h=d, r=r, center=true);
                }
            }
        }
    }
}

// Create the main object
difference() {
    // Outer box
    rounded_box(width, height, depth, corner_radius);
    
    // Inner cavity
    translate([0, 0, wall_thickness]) {
        rounded_box(
            width - 2*wall_thickness, 
            height - 2*wall_thickness, 
            depth, 
            corner_radius - wall_thickness
        );
    }
}
