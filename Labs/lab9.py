#Lab 7 Nazli Zamanian 
import math
import random
import zlib  

file_path = 'exempeltext.txt'
#1C  How many symbols does the string contain? How many bytes
#does the byte-array contain?
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

#Down to how many bytes should it be possible to compress the
#byte-array byteArr if we treat it as a memory-free source (i.e.,
#we do not exploit statistical redundancy) but use an optimal Answer!
#encoding?
# (d) Function to calculate the theoretical minimum size for compression
def min_compression_size(byteArr):
    return len(set(byteArr)) * 8 #624bits (78bytes)

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
#(c) Verify that byteArr is not shuffled
print("Original byteArr:", byteArr)
print("Shuffled copy (theCopy):", theCopy)
print("\n")



#4 C,D,E
#Now you have three different numbers of bits/symbol: (a) the
#data source's entropy, (b) the zlib-encoding of theCopy, and (c)
#the zlib-encoding of byteArr. Which one is the smallest number? Answer!
#Which one is the highest number? Explain why!
#zip compressin the byteArray, shuffled, and a theCopy 
import zlib 
print("4-----------------------------------------------------------------")

#theCopy
print(f"Size of the original data (theCopy): {len(theCopy)} bytes")

compressed_theCopy = zlib.compress(theCopy)
print(f"Size of the compressed data: {len(compressed_theCopy)} bytes\n")

size_in_bits_copy = size_in_bytes_copy * 8 #amount of bits
number_of_symbols_theCopy = len(theCopy) #amount of symbols
bits_per_symbol_theCopy = size_in_bits_copy / number_of_symbols_theCopy #compression ratio
print(f"theCopy Number of source symbols : {number_of_symbols_theCopy}")
print(f"theCopy Compression ratio (bits per symbol): {bits_per_symbol_theCopy:.2f} bits/symbol\n")


#byteArr (shuffled) takes more place, because their is no pattern to look at. 
print(f"Size of the original data (byte Arr): {len(byteArr)} bytes")

compressed_code_original = zlib.compress(byteArr)

size_in_bytes_original = len(compressed_code_original)
size_in_bits_original = size_in_bytes_original * 8
number_of_symbols_original = len(byteArr)
bits_per_symbol_original = size_in_bits_original / number_of_symbols_original

print(f"ByteArr (Shuffled) Number of source symbols (original): {number_of_symbols_original}")
print(f"ByteArr (Shuffled) Compression ratio (bits per symbol) for the original: {bits_per_symbol_original:.2f} bits/symbol\n")

#byteArr (unshuffled)
# size_in_bytes_original = len(compressed_code_original)
# size_in_bits_original = size_in_bytes_original * 8
# number_of_symbols_original = len(byteArr)
# bits_per_symbol_original = size_in_bits_original / number_of_symbols_original

# print(f"ByteArr (Unshuffled) Number of source symbols (byteArr): {number_of_symbols_original}")
# print(f"ByteArr (Unshuffled)Compression ratio (bits per symbol) for byteArr: {bits_per_symbol_original:.2f} bits/symbol\n")


#5 
print("5-----------------------------------------------------------------")
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


