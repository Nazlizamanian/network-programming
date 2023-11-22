import math
import random
import zlib  

file_path = 'exempeltext.txt'
#1C 
with open(file_path, 'rb') as file:
    bytes_content = file.read()
    txt = bytes_content.decode("utf-8", errors= "replace")
    
byteArr = bytearray(txt, "utf-8")
    
number_of_symbols= len(txt)
    
number_of_bytes= len(byteArr)
    
print(f"Number of symbols in the string: {number_of_symbols}")
print(f"Number of bytes in the byte array: {number_of_bytes}")
print("\n")
#number_of_symbols in the stirngs are: 29189
#number_of_bytes in the byte array are: 31787


#2D
def makeHisto(byteArr):
    histogram = [0] * 256
    for byte in byteArr:
        histogram[byte] += 1
    return histogram

# (b) Function to create a probability distribution
def makeProb(histo):
    total = sum(histo)
    probability_distribution = [count / total if total != 0 else 0 for count in histo]
    return probability_distribution

# (c) Function to calculate entropy
def entropy(prob):
    entropy_value = 0
    for p in prob:
        if p != 0:
            entropy_value -= p * math.log2(p)
    return entropy_value

# (d) Function to calculate the theoretical minimum size for compression
def min_compression_size(byteArr):
    return len(set(byteArr)) * 8

with open(file_path, 'rb') as file:
    bytes_content = file.read()
    txt = bytes_content.decode("utf-8", errors="replace")

byteArr = bytearray(txt, "utf-8")

# Calculate statistics and entropy
number_of_symbols = len(txt)
number_of_bytes = len(byteArr)

histogram = makeHisto(byteArr)
probability_distribution = makeProb(histogram)
entropy_value = entropy(probability_distribution)
min_size = min_compression_size(byteArr)

# Print results
print(f"2D\nNumber of symbols in the string: {number_of_symbols}")
print(f"Number of bytes in the byte array: {number_of_bytes}")
print("(a) Histogram:", histogram)
print("(b) Probability Distribution:", probability_distribution)
print("(c) Entropy:", entropy_value)
print("(d) Theoretical Minimum Compression Size:", min_size)
print("\n")



#3 
theCopy = bytearray(byteArr)
random.shuffle(theCopy)

# (c) Verify that byteArr is not shuffled
print("Original byteArr:", byteArr)
print("Shuffled copy (theCopy):", theCopy)
print("\n")

#4B 
import zlib

# Assuming theCopy is already defined from your previous code

# (b) Zip-compress theCopy using zlib
compressed_code_copy = zlib.compress(theCopy)

# Print the size of the original and compressed data for theCopy
print(f"4\nSize of the original data (theCopy): {len(theCopy)} bytes")
print(f"Size of the compressed data: {len(compressed_code_copy)} bytes")

# (c) Calculate the size in bytes and bits, and the number of source symbols
size_in_bytes_copy = len(compressed_code_copy)
size_in_bits_copy = size_in_bytes_copy * 8
number_of_symbols_copy = len(theCopy)

# Calculate bits per symbol
bits_per_symbol_copy = size_in_bits_copy / number_of_symbols_copy

# Print the results for theCopy
print(f"Size of the compressed data: {size_in_bytes_copy} bytes")
print(f"Size of the compressed data: {size_in_bits_copy} bits")
print(f"Number of source symbols (theCopy): {number_of_symbols_copy}")
print(f"Compression ratio (bits per symbol): {bits_per_symbol_copy:.2f} bits/symbol")
print("\n")

# Assuming byteArr is already defined from your previous code

# (b) Zip-compress byteArr using zlib
compressed_code_original = zlib.compress(byteArr)

# (c) Calculate the size in bytes and bits, and the number of source symbols for the original byteArr
size_in_bytes_original = len(compressed_code_original)
size_in_bits_original = size_in_bytes_original * 8
number_of_symbols_original = len(byteArr)

# Calculate bits per symbol for the original byteArr
bits_per_symbol_original = size_in_bits_original / number_of_symbols_original

# Print the results for the original byteArr
print(f"Size of the compressed data (original): {size_in_bytes_original} bytes")
print(f"Size of the compressed data (original): {size_in_bits_original} bits")
print(f"Number of source symbols (original): {number_of_symbols_original}")
print(f"Compression ratio (bits per symbol) for the original: {bits_per_symbol_original:.2f} bits/symbol")
print("---------------------------")

#4D
import zlib

# (b) Zip-compress byteArr using zlib
compressed_code_original = zlib.compress(byteArr)

# Print the size of the original and compressed data for byteArr
print(f"Size of the original data (byteArr): {len(byteArr)} bytes")
print(f"Size of the compressed data: {len(compressed_code_original)} bytes")

# (c) Calculate the size in bytes and bits, and the number of source symbols for byteArr
size_in_bytes_original = len(compressed_code_original)
size_in_bits_original = size_in_bytes_original * 8
number_of_symbols_original = len(byteArr)

# Calculate bits per symbol for byteArr
bits_per_symbol_original = size_in_bits_original / number_of_symbols_original

# Print the results for byteArr
print(f"Size of the compressed data: {size_in_bytes_original} bytes")
print(f"Size of the compressed data: {size_in_bits_original} bits")
print(f"Number of source symbols (byteArr): {number_of_symbols_original}")
print(f"Compression ratio (bits per symbol) for byteArr: {bits_per_symbol_original:.2f} bits/symbol")
