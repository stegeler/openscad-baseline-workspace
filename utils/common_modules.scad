// Common OpenSCAD Modules and Functions
// Reusable components for your projects

// Create a rounded rectangle
module rounded_rectangle(width, height, depth, radius) {
    hull() {
        for (x = [-width/2 + radius, width/2 - radius]) {
            for (y = [-height/2 + radius, height/2 - radius]) {
                translate([x, y, 0]) {
                    cylinder(h=depth, r=radius, center=true);
                }
            }
        }
    }
}

// Create a hexagon
module hexagon(radius, height) {
    cylinder(h=height, r=radius, $fn=6, center=true);
}

// Create a star shape
module star(outer_radius, inner_radius, points, height) {
    linear_extrude(height=height, center=true) {
        polygon(points=concat(
            [for (i = [0:points-1]) [
                outer_radius * cos(i * 360/points),
                outer_radius * sin(i * 360/points)
            ]],
            [for (i = [0:points-1]) [
                inner_radius * cos((i + 0.5) * 360/points),
                inner_radius * sin((i + 0.5) * 360/points)
            ]]
        ));
    }
}

// Create a gear (simplified)
module gear(teeth, pitch_radius, height, tooth_height) {
    difference() {
        cylinder(h=height, r=pitch_radius + tooth_height, center=true);
        for (i = [0:teeth-1]) {
            rotate([0, 0, i * 360/teeth]) {
                translate([pitch_radius, 0, 0]) {
                    cube([tooth_height*2, 2, height+1], center=true);
                }
            }
        }
    }
}

// Create a spiral
module spiral(radius, height, turns, resolution=100) {
    points = [for (i = [0:resolution-1]) [
        (radius * i / resolution) * cos(i * turns * 360 / resolution),
        (radius * i / resolution) * sin(i * turns * 360 / resolution),
        height * i / resolution
    ]];
    
    for (i = [0:len(points)-2]) {
        hull() {
            translate(points[i]) sphere(r=1);
            translate(points[i+1]) sphere(r=1);
        }
    }
}
