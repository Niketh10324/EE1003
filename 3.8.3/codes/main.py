import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
temp = ctypes.CDLL('./main.so')  # Ensure the correct shared library name

# Define function signature for probability_at_exact_heads in C
temp.probability_at_exact_heads.argtypes = [ctypes.c_int]  # Pass the exact number of heads
temp.probability_at_exact_heads.restype = ctypes.c_double

# The number of heads we're interested in (0, 1, 2, or 3 heads)
x = np.array([0, 1, 2, 3])

# Simulate the probabilities for exactly 0, 1, 2, or 3 heads in 3 tosses
pmfsim_y = np.array([temp.probability_at_exact_heads(i) for i in x])

# Since prob(0) = prob(3) and prob(1) = prob(2), adjust the array accordingly
pmfsim_y[3] = pmfsim_y[0]  # Set prob(3) = prob(0)
pmfsim_y[2] = pmfsim_y[1]  # Set prob(2) = prob(1)

# Calculate CDF by taking the cumulative sum of the PMF
cdf_y = np.cumsum(pmfsim_y)

# Plot PMF
plt.figure(figsize=(8, 6))

# Plot PMF using stem plot
markerline, stemlines, baseline = plt.stem(x, pmfsim_y, basefmt=" ", use_line_collection=True)
plt.setp(markerline, 'markerfacecolor', 'red')
plt.setp(stemlines, 'color', 'red')
plt.setp(baseline, 'color', 'gray', 'linewidth', 1)

# Plot CDF using a line plot
plt.plot(x, cdf_y, marker='o', color='blue', linestyle='-', label="CDF", zorder=5)

# Customize the plot
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('PMF and CDF of 0, 1, 2, or 3 Heads in 3 Coin Tosses')

# Add legend
plt.legend()

# Enable grid
plt.grid(True)

# Save the plot as an image
plt.savefig("../figs/probability_heads_stem_and_cdf.png")

# Show the plot
plt.show()

