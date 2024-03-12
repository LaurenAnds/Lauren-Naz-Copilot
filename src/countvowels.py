def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("python"))
print(count_vowels("hello")) 
print(count_vowels("world")) 
print(count_vowels("programming"))