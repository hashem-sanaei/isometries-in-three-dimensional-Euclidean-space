import numpy as np
import matplotlib.pyplot as plt

def reflect_point(point, plane_normal, plane_point):
    vec = point - plane_point
    distance = np.dot(vec, plane_normal) / np.linalg.norm(plane_normal)
    reflected_point = point - 2 * distance * plane_normal / np.linalg.norm(plane_normal)
    return reflected_point

def translate_point(point, translation_vector):
    return point + translation_vector

# Define the point and the planes
point = np.array([3, 4, 5])
plane_normal = np.array([0, 0, 1])
plane_point1 = np.array([0, 0, 0])
plane_point2 = np.array([0, 0, 10])

# First reflection
reflected_point1 = reflect_point(point, plane_normal, plane_point1)
# Second reflection
reflected_point2 = reflect_point(reflected_point1, plane_normal, plane_point2)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original point
ax.scatter(point[0], point[1], point[2], color='blue', label='Original Point')
# Plot the first reflected point
ax.scatter(reflected_point1[0], reflected_point1[1], reflected_point1[2], color='green', label='First Reflected Point')
# Plot the second reflected point (final translated point)
ax.scatter(reflected_point2[0], reflected_point2[1], reflected_point2[2], color='red', label='Second Reflected Point (Translated Point)')

# Plot the planes
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
zz1 = np.zeros_like(xx)
zz2 = np.ones_like(xx) * 10
ax.plot_surface(xx, yy, zz1, alpha=0.2)
ax.plot_surface(xx, yy, zz2, alpha=0.2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
