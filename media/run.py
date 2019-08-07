import bpy

# Number of cubes.
count = 2

# Size of grid.
extents = 8.0

# Spacing between cubes.
padding = 0.05

# Size of each cube.
sz = (extents / count) - padding

# To convert abstract grid position within loop to real-world coordinate.
iprc = 0.0
jprc = 0.0
kprc = 0.0
countf = 1.0 / (count - 1)
diff = extents * 2

# Position of each cube.
z = 0.0
y = 0.0
x = 0.0

# Center of grid.
centerz = 0.0
centery = 0.0
centerx = 0.0

# Clear scene
scene = bpy.context.scene
print("Before clearing there is %d objects in scene" % len(scene.objects))
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()
print("After clearing there is %d objects in scene" % len(scene.objects))

#for obj in bpy.context.scene.objects:
#    if obj.type == 'MESH':
#        obj.select = True
#    else:
#        obj.select = False
#    bpy.ops.object.delete()

#bpy.ops.scene.delete()
#bpy.ops.scene.new()

# Loop through grid z axis.
for i in range(0, count, 1):
    print("i = %d" % i)
    # Convert from index to percent in range 0 .. 1,
    # then convert from prc to real world coordinate.
    # Equivalent to map(val, lb0, ub0, lb1, ub1).
    iprc = i * countf
    z = -extents + iprc * diff
    # Loop through grid y axis.
    for j in range(0, count, 1):
        print("j = %d" % j)
        jprc = j * countf
        y = -extents + jprc * diff
        # Loop through grid x axis.
        for k in range(0, count):
            print("k = %d" % k)
            kprc = k * countf
            x = -extents + kprc * diff
            # Add grid world position to cube local position.
            bpy.ops.mesh.primitive_cube_add(location=(centerx + x, centery + y, centerz + z), size=sz)
            # Cache the current object being worked on.
            current = bpy.context.object
            # Equivalent to Java's String.format. Placeholders
            # between curly braces will be replaced by value of k, j, i.
            current.name = 'Cube ({0}, {1}, {2})'.format(k, j, i)
            current.data.name = 'Mesh ({0}, {1}, {2})'.format(k, j, i)
            # Create a material.
            mat = bpy.data.materials.new(name='Material ({0}, {1}, {2})'.format(k, j, i))
            # Assign a diffuse color to the material.
            mat.diffuse_color = (kprc, jprc, iprc, 0)
            current.data.materials.append(mat)

# Add a sun lamp above the grid.
bpy.ops.object.light_add(type='SUN', radius=1.0, location=(0.0, 0.0, extents * 0.667))

# Add an isometric camera above the grid.
# Rotate 45 degrees on the x-axis, 180 - 45 (135) degrees on the z-axis.
#cam_data = bpy.data.cameras.new("MyCam")
#cam_data.type = "ORTHO"
#cam_data.ortho_scale = extents * 7.0
#cam_ob = bpy.data.objects.new(name="MyCam", object_data=cam_data)
#scene.collection.objects.link(cam_ob)  # instance the camera object in the scene
#scene.camera = cam_ob       # set the active camera
#cam_ob.rotation_axis_angle = (0.785398, 0.0, 2.35619, 0)
#cam_ob.location = (extents * 1.414, extents * 1.414, extents * 2.121)



bpy.ops.object.camera_add(location=(extents * 1.414, extents * 1.414, extents * 2.121), rotation=(0.785398, 0.0, 2.35619))
scene.camera = bpy.context.object
bpy.context.object.data.type = 'ORTHO'
bpy.context.object.data.ortho_scale = extents * 7.0

bpy.context.view_layer.update()
render = scene.render
render.engine = 'CYCLES'
render.use_file_extension = True
render.filepath = "/media/out.png"
bpy.ops.render.render(write_still=True)
#bpy.ops.render.render()


