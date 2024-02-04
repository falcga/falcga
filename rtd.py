import numpy as np
import system 
import randomgen

# Create a random number generator
rng = randomgen.Xoroshiro128()

# Roll the die
result = rng.integers(1, 7)  # Generates a random integer between 1 and 6
print(result)