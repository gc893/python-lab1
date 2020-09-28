# Write the code that:

# Prompts the user to enter a letter in the alphabet: Please enter a letter from the alphabet (a-z or A-Z):
# Write the code that determines whether the letter entered is a vowel
# Print one of following messages (substituting the letter for x):
# The letter x is a vowel
# The letter x is a consonant1

vowels = ['a','e','i','o','u']

letter = input('Please enter a letter: ')

if len(letter) < 2 and letter.isalpha():
    printed = False
    for v in vowels:
        if v == letter:
            print(f'{letter} is a vowel')
            printed = True
            break
    if printed == False:
        print(f'{letter} is a consonant')
else:
    print('Please enter a valid letter: a-z or A-Z.')
