# Write the code that:

# Prompts the user to enter a dog's age in human years like this: Input a dog's age in human years:
# Calculates the equivalent dog years, where:
# The first two years count as 10 years each
# Any remaining years count as 7 years each
# Prints the answer in the following format: The dog's age in dog years is xx
# Hint: Use the int() function to convert the string returned from input() into an integer

humanAge = float(input('Input a dog\'s age in human years: '))

if humanAge > 2:
    dogYears = (humanAge - 2) * 7 + 20
else:
    dogYears = humanAge * 10

print(f'The dog\'s age in dog years is {dogYears:.0f}')