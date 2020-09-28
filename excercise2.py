# Write the code that:

# Prompts the user to enter a phrase: Please enter a word or phrase:
# Print the following message:
# What you entered is xx characters long
# Return to step 1, unless the word 'quit' was entered.

while True:
    newInput = input('Enter a word or phrase: ')
    print(f'This text is {len(newInput)} cahracters long.')
    response = input('Enter new word or phrase? (y/n)').lower()
    if response == 'n':
        break

