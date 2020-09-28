# Write the code that:

# Calculates and prints the first 50 terms of the fibonacci sequence.

series = [0,1]

digits = int(input('How many digits would you like? '))

if digits < 1:
    print('Invalid Input')
elif digits < 2:
    print(f'Term 1 / number: {series[-2]}')
elif digits < 3:
    print(f'Term 1 / number: {series[-2]}')
    print(f'Term 2 / number: {series[-1]}')
else:
    startPoint = 3

    print(f'Term {startPoint -2} / number: {series[-2]}')
    print(f'Term {startPoint -1} / number: {series[-1]}')

    while startPoint <= digits:

        nextValue = series[-1] + series[-2]
        series.append(nextValue)

        print(f'Term {startPoint} / number: {series[-1]}')

        startPoint +=1