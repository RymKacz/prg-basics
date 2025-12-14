vowels = "aeiouAEIOU"
inputtext = input("Enter a string: ")
vowel_count = 0
for char in inputtext:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)