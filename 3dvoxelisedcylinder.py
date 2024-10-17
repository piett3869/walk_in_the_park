import numpy as np
from mayavi import mlab

def voxelize_cylinder(radius, height, voxel_size, center=(0, 0, 0)):
    """
    Voxelizes a 3D cylinder with the specified radius, height, voxel size, and center.

    Args:
        radius: The radius of the cylinder's base.
        height: The height of the cylinder.
        voxel_size: The size of each voxel in the voxelized representation.
        center: The center of the cylinder.

    Returns:
        A 3D NumPy array representing the voxelized cylinder.
    """

    # Calculate the dimensions of the voxel grid
    nx = int(2 * radius / voxel_size) + 1
    ny = int(2 * radius / voxel_size) + 1
    nz = int(height / voxel_size) + 1

    # Create an empty voxel grid
    voxels = np.zeros((nx, ny, nz))

    # Iterate over each voxel and check if it's inside the cylinder
    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                # Calculate the coordinates of the voxel's center
                voxel_center = (x - nx // 2) * voxel_size + center[0], (y - ny // 2) * voxel_size + center[1], z * voxel_size + center[2]

                # Check if the voxel's center is inside the cylinder
                if np.sqrt(voxel_center[0]**2 + voxel_center[1]**2) <= radius and voxel_center[2] >= 0 and voxel_center[2] <= height:
                    voxels[x, y, z] = 1

    return voxels

def voxelize_full_cylinder(radius, height, voxel_size, center=(0, 0, 0)):
    """
    Voxelizes a full 3D cylinder (including the top and bottom faces) with the specified radius, height, voxel size, and center.

    Args:
        radius: The radius of the cylinder's base.
        height: The height of the cylinder.
        voxel_size: The size of each voxel in the voxelized representation.
        center: The center of the cylinder.

    Returns:
        A 3D NumPy array representing the voxelized cylinder.
    """

    # Calculate the dimensions of the voxel grid
    nx = int(2 * radius / voxel_size) + 1
    ny = int(2 * radius / voxel_size) + 1
    nz = int(height / voxel_size) + 1

    # Create an empty voxel grid
    voxels = np.zeros((nx, ny, nz))

    # Iterate over each voxel and check if it's inside the cylinder
    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                # Calculate the coordinates of the voxel's center
                voxel_center = (x - nx // 2) * voxel_size + center[0], (y - ny // 2) * voxel_size + center[1], z * voxel_size + center[2]

                # Check if the voxel's center is inside the cylinder
                if np.sqrt(voxel_center[0]**2 + voxel_center[1]**2) <= radius and voxel_center[2] >= 0 and voxel_center[2] <= height:
                    voxels[x, y, z] = 1

                # Check if the voxel's center is on the top or bottom face
                if np.sqrt(voxel_center[0]**2 + voxel_center[1]**2) <= radius and (voxel_center[2] == 0 or voxel_center[2] == height):
                    voxels[x, y, z] = 1

    return voxels

# Example usage
radius = 2
height = 5
voxel_size = 0.1
center = (0, 0, 0)
# voxels = voxelize_cylinder(radius, height, voxel_size, center)
voxels = voxelize_full_cylinder(radius, height, voxel_size, center)

# Visualize the voxelized cylinder using Mayavi
mlab.contour3d(voxels, color=(0.5, 0.5, 0.5))
mlab.contour3d(voxels, color=(0.5, 0.5, 0.5))
mlab.show()


