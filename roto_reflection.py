from matplotlib import pyplot as plt
import numpy as np
from reflect_point import reflect_point
from rotate_point import rotate_point


def roto_reflection(point, plane_normal, plane_point, axis, angle):
    reflected_point = reflect_point(point, plane_normal, plane_point)
    rotated_point = rotate_point(reflected_point, axis, angle)
    return rotated_point

# Define the point, plane, and rotation axis
point = np.array([3, 4, 5])
plane_normal = np.array([0, 0, 1])
plane_point = np.array([0, 0, 0])
axis = np.array([0, 0, 1])
angle = np.pi / 4  # 45 degrees

# Calculate the roto-reflected point
roto_reflected_point = roto_reflection(point, plane_normal, plane_point, axis, angle)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original point
ax.scatter(point[0], point[1], point[2], color='blue', label='Original Point')
# Plot the roto-reflected point
ax.scatter(roto_reflected_point[0], roto_reflected_point[1], roto_reflected_point[2], color='red', label='Roto-Reflected Point')

# Plot the plane
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.2)

# Plot the rotation axis
ax.quiver(0, 0, 0, axis[0], axis[1], axis[2], length=10, color='green', label='Rotation Axis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
