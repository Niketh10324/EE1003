import numpy as np
import matplotlib.pyplot as plt

# Load numerical solution data from .dat file
data = np.loadtxt("data.dat", comments="#")
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

