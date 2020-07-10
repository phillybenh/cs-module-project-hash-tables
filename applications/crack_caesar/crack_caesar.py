# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

import re
char_freq = {'E': 11.53, 'T': 9.75, 'A': 8.46, 'O': 8.08, 'H': 7.71, \
    'N': 6.73, 'R': 6.29, 'I': 5.84, 'S': 5.56, 'D': 4.74, 'L': 3.92, \
    'W': 3.08, 'U': 2.59, 'G': 2.48, 'F': 2.42, 'B': 2.19, 'M': 2.18, \
    'Y': 2.02, 'C': 1.58, 'P': 1.08, 'K': 0.84, 'V': 0.59, 'Q': 0.17, \
    'J': 0.07, 'X': 0.07, 'Z': 0.03}

with open('ciphertext.txt') as ct:
    ciphertext = ct.read()



# find how many of each character there are
char = re.sub(r'[^\w]', '', ciphertext)

total_char = len(char) - 1 # -1 due to key " still in there
count = {}
for c in char:
    if c not in count:
        count[c] = 0

    count[c] += 1
# TODO: get rid of "1" in teh regex    
del count["1"]
# find percentage of total_char
char_percentage = {}
for c in count:
    char_percentage[c] = round(count[c] / total_char * 100, 2)

# compare percentages to normal_freq to make decode_table
sorted_char = {k: v for k, v in sorted(char_percentage.items(),key=lambda \
    item: item[1], reverse=True)}

decode_table = {}
for c in range(len(sorted_char)):
    decode_table[list(sorted_char.keys())[c]] = list(char_freq.keys())[c]

# decode the text 
decoded_text = ""
for c in ciphertext:
    if c in decode_table:
        decoded_text += decode_table[c]
    else:
        decoded_text += c

print(decoded_text)






"""
# Caeser Cipher

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

decode_table = {}
# Automatically generate the decode_table from teh encode_table
for k, v in encode_table.items():
    decode_table[v] = k


def encode(s):
    r = ""

    for c in s:
        r += encode_table[c]

    return r

def decode(s):
    r = ""

    for c in s:
        r += decode_table[c]

    return r

print(encode("HELLO"))

print (decode("DOGGE"))
"""



