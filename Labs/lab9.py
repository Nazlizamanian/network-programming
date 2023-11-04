#Lab9 Nazli Zamanian Gustavsson
#9.2 Comporession

file_path = 'exempeltext.txt'

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