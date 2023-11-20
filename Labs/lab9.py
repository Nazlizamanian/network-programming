#Lab9 Nazli Zamanian Gustavsson
#9.2 Compression
import random 
import math
import zlib

file_path = 'exempeltext.txt'

# 1C 
with open(file_path, 'rb') as file:
    bytes_content = file.read()
    txt = bytes_content.decode("utf-8", errors= "replace")
    
byteArr = bytearray(txt, "utf-8")
    
number_of_symbols= len(txt)
    
number_of_bytes= len(byteArr)
    
print(f"Number of symbols in the string: {number_of_symbols}")
print(f"Number of bytes in the byte array: {number_of_bytes}")
#number_of_symbols in the stirngs are: 29189
#number_of_bytes in the byte array are: 31787

#2 
def makeHisto(byteArr):
    # Initialize a list with zeros to represent the histogram
    histogram = [0] * 256

    # Iterate through the byte array and update the histogram
    for byte in byteArr:
        histogram[byte] += 1

    return histogram

# Example usage:
file_path = 'exempeltext.txt'

with open(file_path, 'rb') as file:
    bytes_content = file.read()

# Call the function with the byte array
histogram_result = makeHisto(bytes_content)

# Print the histogram
for i, count in enumerate(histogram_result):
    print(f"Byte value {i}: {count} occurrences")
def makeProb(histo):
    # Calculate the total count in the histogram
    total_count = sum(histo)

    # Normalize the histogram to create a probability distribution
    probability_distribution = [count / total_count for count in histo]

    return probability_distribution

# Example usage:
file_path = 'exempeltext.txt'

with open(file_path, 'rb') as file:
    bytes_content = file.read()

# Create a histogram using the previous function
histogram_result = makeHisto(bytes_content)

# Call the makeProb function with the histogram
probability_distribution_result = makeProb(histogram_result)

# Print the probability distribution
for i, probability in enumerate(probability_distribution_result):
    print(f"Byte value {i}: Probability {probability:.6f}")


import math

def entropy(prob):
    # Avoid division by zero by ensuring that probabilities are not 0
    prob_nonzero = [p if p != 0 else 1 for p in prob]

    # Calculate entropy using the formula
    entropy_value = -sum(p * math.log2(p) for p in prob_nonzero)

    return entropy_value

# Example usage:
file_path = 'exempeltext.txt'

with open(file_path, 'rb') as file:
    bytes_content = file.read()

# Create a histogram and probability distribution using previous functions
histogram_result = makeHisto(bytes_content)
probability_distribution_result = makeProb(histogram_result)

# Call the entropy function with the probability distribution
entropy_result = entropy(probability_distribution_result)

# Print the entropy value
print(f"Entropy: {entropy_result:.6f}")


import math

def entropy(prob):
    # Avoid division by zero by ensuring that probabilities are not 0
    prob_nonzero = [p if p != 0 else 1 for p in prob]

    # Calculate entropy using the formula
    entropy_value = -sum(p * math.log2(p) for p in prob_nonzero)

    return entropy_value

# 2C
file_path = 'exempeltext.txt'

with open(file_path, 'rb') as file:
    bytes_content = file.read()

# Create a histogram and probability distribution using previous functions
histogram_result = makeHisto(bytes_content)
probability_distribution_result = makeProb(histogram_result)

# Call the entropy function with the probability distribution
entropy_result = entropy(probability_distribution_result)

# Calculate the theoretical minimum number of bits needed
bits_needed = int(entropy_result * len(bytes_content))

# Print the result
print(f"Theoretical minimum number of bits needed: {bits_needed}")


theCopy = bytearray(byteArr)  # Create a copy of byteArr
random.shuffle(theCopy)  # Shuffle the copy

# (c) Verify that you have not erroneously shuffled byteArr.
# Compare the original byteArr with the shuffled theCopy
if byteArr == theCopy:
    print("Error: byteArr has been erroneously shuffled.")
else:
    print("Verification successful: byteArr is not shuffled.")