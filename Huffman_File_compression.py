"""
Project : Huffman File Compression
Author  : Golla Manogna
Language: Python
Description:
This project implements Huffman Coding for lossless file compression
using Binary Trees and Min Heap.
"""

import heapq
# Read input file
with open("input.txt", "r") as file:
    text = file.read()

print("Input File:")
print(text)
# Count character frequencies
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\nCharacter Frequencies:")

for char, count in frequency.items():
    print(char, ":", count)
class Node:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
codes = {}
# Generate Huffman Codes
def generate_codes(node, code):

    if node is None:
        return

    if node.char is not None:
        codes[node.char] = code

    generate_codes(node.left, code + "0")
    generate_codes(node.right, code + "1")
# Decode Text
def decode(root, encoded_text):

    decoded_text = ""

    current = root

    for bit in encoded_text:

        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded_text += current.char
            current = root

    return decoded_text    

heap = []

# Create Node objects
for char, freq in frequency.items():
    node = Node(char, freq)
    heapq.heappush(heap, node)

while len(heap) > 1:

    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    merged = Node(None, left.freq + right.freq)

    merged.left = left
    merged.right = right

    heapq.heappush(heap, merged)

#print("Merged:", left.freq, "+", right.freq, "=", merged.freq)
root = heap[0]

#print("Root Frequency:", root.freq)
generate_codes(root, "")

print("\nHuffman Codes:")

for char, code in codes.items():
    print(char, ":", code)
encoded_text = ""

for char in text:
    encoded_text += codes[char]

print("\nEncoded Text:")
print(encoded_text)
with open("compressed.txt", "w") as file:
    file.write(encoded_text)

print("\nCompressed file created successfully!")

decoded_text = decode(root, encoded_text)

print("\nDecoded Text:")
print(decoded_text)

with open("decompressed.txt", "w") as file:
    file.write(decoded_text)

print("\nDecompressed file created successfully!")

if text == decoded_text:
    print("\n Success! Original text and decoded text are identical.")
else:
    print("\n Error! Decoding failed.")