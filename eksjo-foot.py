import cadquery as cq

nozzle_diameter = 0.4  # mm
layer_height = 0.2  # mm


def calculate_extrusion_width(nozzle_diameter):
    """Calculate the extrusion width that PrusaSlicer defaults use"""
    if nozzle_diameter == 0.4:
        return nozzle_diameter * 1.125
    elif nozzle_diameter == 0.6:
        return nozzle_diameter
    else:
        print("Not sure what the extrusion width should be, using nozzle diameter")
        return nozzle_diameter


def calculate_shell_thickness(layer_height, extrusion_width):
    """
    Calculate the thickness of the shell in mm
    This is the recommend object thin wall thickness for the layer
    height with 2 lines
    https://manual.slic3r.org/advanced/flow-math
    """
    return (extrusion_width - layer_height * (1 - (3.141 / 4))) + extrusion_width


# The extrusion width in mm
extrusion_width = calculate_extrusion_width(nozzle_diameter)

# The thickness of the shell in mm
two_walls = calculate_shell_thickness(layer_height, extrusion_width)

width = 40  # mm
depth = 11  # mm
height = 10  # mm

foot = (
    cq.Workplane()
    .box(width, depth, height)
    .faces(">Z")
    .shell(two_walls)
)

cq.exporters.export(
    foot, f"eksjo-foot-{nozzle_diameter}mm-{layer_height}mm.stl")
