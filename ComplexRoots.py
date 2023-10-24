"""
# Here's what the function does:
# It takes a list of coefficients as input, similar to the previous function.
# It calculates the roots of the polynomial using np.roots().
# It filters out any real roots using np.iscomplex().
# It separates the real and imaginary parts of the complex roots.
# It creates a 3D plot with matplotlib using fig.add_subplot(111, projection='3d').
# It creates a surface plot of the polynomial using np.polyval() to evaluate the polynomial for complex numbers.
# It adds a scatter plot of the complex roots on top of the polynomial surface.
# It sets labels, title, and legend for the plot.
# You can use this function by providing the coefficients of the polynomial you want to analyze. For example, plot_complex_roots_3d([1, 0, 1]) will plot the complex roots of the polynomial x^2 + 1 in 3D along with the polynomial surface.
#
# Usage:
plot_complex_roots_3d([1, 0, 1])
"""

def plot_complex_roots_3d(coefficients):
    # Find the roots of the polynomial
    roots = np.roots(coefficients)
    # Filter out real roots
    complex_roots = [root for root in roots if np.iscomplex(root)]
    # Separate real and imaginary parts for plotting
    real_parts = np.real(complex_roots)
    imag_parts = np.imag(complex_roots)
    # Create the plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    # Plot the polynomial surface
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.polyval(coefficients, X + 1j*Y)
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    # Plot the complex roots
    ax.scatter(real_parts, imag_parts, np.zeros_like(real_parts), color='red', s=50, label='Complex Roots')
    # Set labels and title
    ax.set_xlabel('Real Part')
    ax.set_ylabel('Imaginary Part')
    ax.set_zlabel('Magnitude')
    plt.title('Complex Roots of the Polynomial')
    # Show the legend
    ax.set_box_aspect([1, 1, 1])
    ax.legend()
    plt.show()

