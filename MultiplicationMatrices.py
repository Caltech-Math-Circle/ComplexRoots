import numpy as np
import matplotlib.pyplot as plt

# Define the coordinates of the polygon as a matrix (each row is a point)
polygon = np.array([[1, 1], [2, 1], [2, 2], [1, 2], [1, 1]])

# Define the transformation matrix (2x2 matrix)
# This matrix will determine how the polygon is transformed
# For example, multiplying by [[2, 0], [0, 2]] will scale the polygon by a factor of 2.
transformation_matrix = np.array([[2, 0], [0, 1]])
rotation_matrix = np.array([[1, -1], [1, 1]])




# Multiply the polygon coordinates by the transformation matrix
transformed_polygon = polygon;

# this is like mu
transformed_polygon = np.dot(transformed_polygon, transformation_matrix)
transformed_polygon = np.dot(transformed_polygon, rotation_matrix)
_title = 'R*T*P'



# Plot the original and transformed polygons
def plot_figure():
	plt.figure(figsize=(8, 8))
	plt.plot(polygon[:, 0], polygon[:, 1], label='Original Polygon', marker='o')
	plt.plot(transformed_polygon[:, 0], transformed_polygon[:, 1], label='Transformed Polygon', marker='x')
	plt.xlabel('X-axis')
	plt.ylabel('Y-axis')
	plt.title(_title)
	plt.legend()
	plt.grid(True)
	plt.axis('equal')  # Make sure the axes have the same scale
	plt.show()

plot_figure();

# now see if matrix multiplication is associative?

transformed_polygon = np.dot(polygon,np.dot(transformation_matrix,rotation_matrix))

_title = '(R*T)*P'
plot_figure();


# commutative?
_title = '(T*R)*P'
transformed_polygon = np.dot(polygon,np.dot(rotation_matrix,transformation_matrix))

plot_figure();