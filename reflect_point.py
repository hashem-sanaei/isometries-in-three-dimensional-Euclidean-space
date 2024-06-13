import numpy as np
import matplotlib.pyplot as plt

def reflect_point(point, plane_normal, plane_point):
    # Calculate the vector from the plane point to the point
    vec = point - plane_point
    # Calculate the projection of the vector onto the plane normal
    distance = np.dot(vec, plane_normal) / np.linalg.norm(plane_normal)
    # Reflect the point across the plane
    reflected_point = point - 2 * distance * plane_normal / np.linalg.norm(plane_normal)
    return reflected_point

# Define the point and the plane
point = np.array([3, 4, 5])
plane_normal = np.array([0, 0, 1])
plane_point = np.array([0, 0, 0])

# Calculate the reflected point
reflected_point = reflect_point(point, plane_normal, plane_point)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the original point
ax.scatter(point[0], point[1], point[2], color='blue', label='Original Point')
# Plot the reflected point
ax.scatter(reflected_point[0], reflected_point[1], reflected_point[2], color='red', label='Reflected Point')

# Plot the plane
xx, yy = np.meshgrid(range(-10, 10), range(-10, 10))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, alpha=0.2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
