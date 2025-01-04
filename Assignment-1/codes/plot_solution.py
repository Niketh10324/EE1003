import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library
lib = ctypes.CDLL("./finite_difference.so")

# Define the DataPoint structure in Python
class DataPoint(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double), ("y", ctypes.c_double)]

# Set return types for the library functions
lib.get_data_size.restype = ctypes.c_int
lib.get_data.restype = ctypes.POINTER(DataPoint)

# Set argument types for the finite_difference function
lib.finite_difference.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]

# Compute finite differences in the C library
lib.finite_difference(-2.0, 1.0, 5.0, 0.01)

# Get the number of data points and the data array
size = lib.get_data_size()
data_pointer = lib.get_data()

# Convert the data to a NumPy array
data = np.array([(data_pointer[i].x, data_pointer[i].y) for i in range(size)])

# Separate x and y values
x_num, y_num = data[:, 0], data[:, 1]

# Define the theoretical solution
def theoretical_solution(x):
    return (x + 4)**2 - 3

x_theory = np.linspace(-2, 5, 500)
y_theory = theoretical_solution(x_theory)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x_theory, y_theory, label="Theoretical Solution", color="blue")
plt.scatter(x_num, y_num, label="Numerical Solution (Finite Differences)", color="red", s=10)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparison of Theoretical and Numerical Solutions")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.savefig("comparison_plot.pdf")
plt.show()

# Clean up the C library memory
lib.cleanup()

