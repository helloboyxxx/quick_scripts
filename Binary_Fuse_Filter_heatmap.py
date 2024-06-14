import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000  # Length of the array
w = 100    # Window size
k = 10000  # Number of iterations

d = 4

# Initialize the array
array = np.zeros(N)

# Perform the iterations
for _ in range(k):
    # Uniformly randomly choose the window location
    window_start = np.random.randint(0, N - w + 1)
    
    # Within the window, randomly choose three positions
    positions = np.random.choice(range(window_start, window_start + w), d, replace=False)
    
    # Add 1 to each chosen position
    for pos in positions:
        array[pos] += 1

# Visualize the array
plt.figure(figsize=(12, 6))
plt.plot(array, label='Frequency of positions within windows')
plt.xlabel('Position in array')
plt.ylabel('Frequency')
plt.title('Frequency of Position Hits in Windows')
plt.legend()
plt.show()


# The results shows that the two ends has lower frequency than the middle part.
