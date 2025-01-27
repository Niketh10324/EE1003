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

# Plot PMF
plt.figure(figsize=(8, 6))
markerline, stemlines, baseline = plt.stem(x, pmfsim_y, basefmt=" ", use_line_collection=True)
plt.setp(markerline, 'markerfacecolor', 'red')
plt.setp(stemlines, 'color', 'red')
plt.setp(baseline, 'color', 'gray', 'linewidth', 1)
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Probability of 0, 1, 2, or 3 Heads in 3 Coin Tosses')

# Remove the legend
plt.legend().set_visible(False)

plt.grid(True)
plt.savefig("../figs/probability_heads_stem.png")
plt.show()

