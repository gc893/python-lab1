# Write the code that:

# Prompts the user to enter the three lengths of a triangle (one at a time): Enter the lengths of three side of a triangle: a: b: c:
# Write the code that determines if the triangle is: equalateral - all three sides are equal in length scalene - all three sides are unequal in length isosceles - two sides are the same length
# Print a message such as:
# A triangle with sides of , & is a triangle

length1 = float(input('Please enter length 1 of 3: '))

length2 = float(input('Please enter length 2 of 3: '))

length3 = float(input('Please enter length 3 of 3: '))

lengths = []

lengths.append(length1)
lengths.append(length2)
lengths.append(length3)

distinctLengths = set(lengths)

if len(distinctLengths) < 2 :
    print('Equilateral Triangle')
elif len(distinctLengths) < 3:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')