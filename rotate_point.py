from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.spatial.transform import Rotation as R

def rotate_point(point, axis, angle):
    rotation = R.from_rotvec(angle * axis / np.linalg.norm(axis))
    return rotation.apply(point)

# Define the point and the rotation axis
point = np.array([3, 4, 5])
axis = np.array([1, 1, 1])
angle = np.pi / 4  # 45 degrees

# Calculate the rotated point
rotated_point = rotate_point(point, axis, angle)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original point
ax.scatter(point[0], point[1], point[2], color='blue', label='Original Point')
# Plot the rotated point
ax.scatter(rotated_point[0], rotated_point[1], rotated_point[2], color='red', label='Rotated Point')

# Plot the rotation axis
ax.quiver(0, 0, 0, axis[0], axis[1], axis[2], length=10, color='green', label='Rotation Axis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
