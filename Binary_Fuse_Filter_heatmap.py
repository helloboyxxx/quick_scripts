import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 5000  # Length of the array
w = 1000    # Window size
k = 50000  # Number of iterations

d = 4

# Initialize the array
array = np.zeros(N)

# Perform the iterations
for _ in range(k):
    # Uniformly randomly choose the window location
    window_start = np.random.randint(0, int(N/w)) * w   # ChalametPIR paper pseudocode
    # window_start = np.random.randint(0, N - w + 1)      # my understanding of BFF window selection
    
    # Within the window, randomly choose d many positions (simulating hashing)
    positions = np.random.choice(range(window_start, window_start + w), d, replace=True)
    
    # Add 1 to each chosen position (counting frequency)
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




