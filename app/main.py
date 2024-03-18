import cadquery as cq

assy = cq.Assembly()
# These can be modified rather than hardcoding values for each dimension.
length = 80.0  # Length of the block
height = 60.0  # Height of the block
thickness = 10.0  # Thickness of the block

# Create a 3D block based on the dimension variables above.
# 1.  Establishes a workplane that an object can be built on.
# 1a. Uses the X and Y origins to define the workplane, meaning that the
# positive Z direction is "up", and the negative Z direction is "down".
result = cq.Workplane("XY").box(length, height, thickness)
box1 = cq.Workplane("XY").box(length, height, thickness)

# The following method is now outdated, but can still be used to display the
# results of the script if you want
# from Helpers import show
assy.add(result, loc=cq.Location((1,2,3)), color=cq.Color('green'), name='test')
assy.add(result, loc=cq.Location((100,200,300)), name='test2')
assy.save('test.step')