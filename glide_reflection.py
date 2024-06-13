from matplotlib import pyplot as plt
import numpy as np
from reflect_point import reflect_point
from translate_point import translate_point


def glide_reflection(point, plane_normal, plane_point, translation_vector):
    reflected_point = reflect_point(point, plane_normal, plane_point)
    translated_point = translate_point(reflected_point, translation_vector)
    return translated_point

# Define the point, plane, and translation vector
point = np.array([3, 4, 5])
plane_normal = np.array([0, 0, 1])
plane_point = np.array([0, 0, 0])
translation_vector = np.array([2, 2, 0])

# Calculate the glide reflected point
glide_reflected_point = glide_reflection(point, plane_normal, plane_point, translation_vector)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original point
ax.scatter(point[0], point[1], point[2], color='blue', label='Original Point')
# Plot the glide reflected point
ax.scatter(glide_reflected_point[0], glide_reflected_point[1], glide_reflected_point[2], color='red', label='Glide Reflected Point')

# Plot the plane
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
