# 2. Character Frequency

# •   ​Difficulty​: Advanced
# •   ​Description​: Write a function character_frequency that takes 
# a string as input and returns a dictionary. The keys of the dictionary 
# should be the unique characters from the string, and the values should 
# be the number of times each character appears. The function should be 
# case-sensitive and include spaces and punctuation.

def character_frequency(s):
    d = {}
    count = 0
    for char in s:
        count = s.count(char)
        print(count)
        




#     ​Test Cases:

print(character_frequency("Hello World!"))
# Expected output: {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'W': 1, 'r': 1, 'd': 1, '!': 1}

# print(character_frequency("Python is fun"))
# # Expected output: {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 2, ' ': 2, 'i': 1, 's': 1, 'f': 1, 'u': 1}