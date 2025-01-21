import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared object file
coin_toss = ctypes.CDLL('./main.so')

# Set argument and return types for the C function
coin_toss.calculate_probabilities.argtypes = [
    ctypes.c_int,                   # int n (number of trials)
    ctypes.POINTER(ctypes.c_double), # double* probabilities
    ctypes.POINTER(ctypes.c_double), # double* cdf
    ctypes.POINTER(ctypes.c_double)  # double* prob_at_least_2_heads
]

# Parameters
num_trials = 100000
probabilities = (ctypes.c_double * 4)()
cdf = (ctypes.c_double * 4)()
prob_at_least_2_heads = ctypes.c_double()

# Call the C function
coin_toss.calculate_probabilities(num_trials, probabilities, cdf, ctypes.byref(prob_at_least_2_heads))

# Convert results to Python lists
probabilities = np.array(list(probabilities))
cdf = np.array(list(cdf))

# Plotting the stem plot for probabilities
outcomes = ['0 Heads', '1 Head', '2 Heads', '3 Heads']
plt.figure(figsize=(8, 6))
plt.stem(outcomes, probabilities, basefmt=" ", use_line_collection=True)
plt.title('Probability Distribution of Heads in 3 Coin Tosses')
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.grid(True)
plt.show()

# Print probability of at least 2 heads
print(f'Probability of getting at least 2 heads: {prob_at_least_2_heads.value:.4f}')

