# Write the code that:

# Prompts the user to enter the month (as three characters): Enter the month of the year (Jan - Dec):
# Then prompts the user to enter the day of the month: Enter the day of the month:
# Calculate what season it is based upon this chart: Dec 21 - Mar 19: Winter Mar 20 - Jun 20: Spring Jun 21 - Sep 21: Summer Sep 22 - Dec 20: Fall
# Print the result as follows:
# is in

month = input('Please enter the month: ').lower()

day = int(input('Please enter the day: '))

if month == 'jan' or month == 'feb':
    print('Winter.')
elif month == 'mar' and day < 20:
    print('Winter.')
elif month == 'mar' and day >= 20:
    print('Spring.')
elif month == 'apr' or month == 'may':
    print('Spring.')
elif month == 'jun' and day <= 20:
    print('Spring.')
elif month == 'jun' and day > 20:
    print('Summer.')
elif month == 'jul' or month == 'aug':
    print('Summer.')
elif month == 'sep' and day < 22:
    print('Winter.')
elif month == 'sep' and day >= 22:
    print('Fall.')
elif month == 'oct' or month == 'nov':
    print('Fall.')
elif month == 'dec' and day <= 20:
    print('Fall.')
elif month == 'dec' and day > 20:
    print('Winter.')