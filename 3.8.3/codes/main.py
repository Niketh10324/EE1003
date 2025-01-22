import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
coin_toss = ctypes.CDLL('./main.so')

# Set argument and return types for the C function
coin_toss.calculate_pmf_z_transform.argtypes = [
    ctypes.POINTER(ctypes.c_double)  # double* probabilities
]

# Array to store probabilities for 0, 1, 2, 3 heads
probabilities = (ctypes.c_double * 4)()

# Call the C function to compute PMF
coin_toss.calculate_pmf_z_transform(probabilities)

# Convert results to NumPy array for easier handling
probabilities = np.array(list(probabilities))

# Compute probability of getting at least 2 heads (sum of P(2) + P(3))
prob_at_least_2_heads = probabilities[2] + probabilities[3]

# Plotting the stem plot for probabilities
outcomes = ['0 Heads', '1 Head', '2 Heads', '3 Heads']
plt.figure(figsize=(8, 6))
plt.stem(outcomes, probabilities, basefmt=" ", use_line_collection=True)
plt.title('Probability Distribution of Heads in 3 Coin Tosses')
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.grid(True)
plt.show()

# Print the probability of getting at least 2 heads
print(f'Probability of getting at least 2 heads: {prob_at_least_2_heads:.4f}')

