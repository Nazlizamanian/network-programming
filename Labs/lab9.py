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
#number_of_symbols in the strings are: 29 189
#number_of_bytes in the byte array are: 31 787, å,ä,ö


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
# print("Original byteArr:", byteArr)
# print("Shuffled copy (theCopy):", theCopy)
print("\n")



#4 C,D,E
import zlib 
print("4")

#theCopy
compressed_code_copy = zlib.compress(theCopy)
print(f"Size of the original data (theCopy): {len(theCopy)} bytes")
print(f"Size of the compressed data: {len(compressed_code_copy)} bytes\n")

size_in_bytes_copy = len(compressed_code_copy)
size_in_bits_copy = size_in_bytes_copy * 8
number_of_symbols_copy = len(theCopy)
bits_per_symbol_copy = size_in_bits_copy / number_of_symbols_copy
print(f"theCopy Number of source symbols : {number_of_symbols_copy}")
print(f"theCopy Compression ratio (bits per symbol): {bits_per_symbol_copy:.2f} bits/symbol\n")




#byteArr (shuffled)
compressed_code_original = zlib.compress(byteArr)

size_in_bytes_original = len(compressed_code_original)
size_in_bits_original = size_in_bytes_original * 8
number_of_symbols_original = len(byteArr)
bits_per_symbol_original = size_in_bits_original / number_of_symbols_original
print(f"ByteArr (Shuffled) Number of source symbols (original): {number_of_symbols_original}")
print(f"ByteArr (Shuffled) Compression ratio (bits per symbol) for the original: {bits_per_symbol_original:.2f} bits/symbol\n")

#byteArr (unshuffled)
size_in_bytes_original = len(compressed_code_original)
size_in_bits_original = size_in_bytes_original * 8
number_of_symbols_original = len(byteArr)
bits_per_symbol_original = size_in_bits_original / number_of_symbols_original

print(f"ByteArr (Unshuffled) Number of source symbols (byteArr): {number_of_symbols_original}")
print(f"ByteArr (Unshuffled)Compression ratio (bits per symbol) for byteArr: {bits_per_symbol_original:.2f} bits/symbol\n")


#5 
print("5")
import zlib 

t1= """I hope this lab never ends because
it is so incredibly thrilling!"""

t10= t1*10

print("t1: ", t1)
print(f"Size of original data for t1: {len(t1.encode('utf-8'))} bytes")

compressed_t1= zlib.compress(t1.encode("utf-8"))
print(f"Size of compressed data for t1: {len(compressed_t1)} bytes")

print("\nt10: ", t10)
print(f"Size of original data for t10: {len(t10.encode('utf-8'))} bytes")

compressed_t10= zlib.compress(t10.encode("utf-8"))
print(f"Size of compressed data for t10: {len(compressed_t10)} bytes")