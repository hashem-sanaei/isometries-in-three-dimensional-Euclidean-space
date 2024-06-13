from matplotlib import pyplot as plt
import numpy as np
from rotate_point import rotate_point
from translate_point import translate_point


def screw_transformation(point, axis, angle, translation_vector):
    rotated_point = rotate_point(point, axis, angle)
    translated_point = translate_point(rotated_point, translation_vector)
    return translated_point

# Define the point, rotation axis, and translation vector
point = np.array([3, 4, 5])
axis = np.array([0, 0, 1])
angle = np.pi / 4  # 45 degrees
translation_vector = np.array([0, 0, 2])

# Calculate the screw transformed point
screw_transformed_point = screw_transformation(point, axis, angle, translation_vector)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original point
ax.scatter(point[0], point[1], point[2], color='blue', label='Original Point')
# Plot the screw transformed point
ax.scatter(screw_transformed_point[0], screw_transformed_point[1], screw_transformed_point[2], color='red', label='Screw Transformed Point')

# Plot the rotation axis
ax.quiver(0, 0, 0, axis[0], axis[1], axis[2], length=10, color='green', label='Rotation Axis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
