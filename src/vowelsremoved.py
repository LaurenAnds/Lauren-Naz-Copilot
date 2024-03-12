import re

def remove_vowels(given_string):
    new_string = ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for letter in given_string:
        if letter not in vowels:
            new_string += letter
    return new_string


print(remove_vowels("python"))
print(remove_vowels("hello")) 
print(remove_vowels("world")) 
print(remove_vowels("programming"))