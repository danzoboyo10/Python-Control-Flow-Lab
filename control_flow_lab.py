# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
term = 0
a = 0
b = 1
while term < 50:
  if term < 2:
    print(f'term: {term} / number: {term}')
  else:
    num = a + b
    print(f'term: {term} / number: {num}')
    a = b
    b = num
  term += 1

# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

# exercise-06 What's the  Season?

# Write the code that:
# 3. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):

month = input('Enter "Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec": ').lower()
print(f'The user entered {month}')


# 4. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
dayOfMonth = input('Enter "Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday": ').lower()
print(f'The user entered {dayOfMonth}')




# 5. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall

# season = "Winter or Summer or Spring or Fall"

if month in ('Dec', 'Jan', 'Feb', 'Mar'):
  season = 'Winter'
elif month in ('Dec', 'Jan', 'Feb', 'Mar'):
  season = 'Spring'
elif month in ('Dec', 'Jan', 'Feb', 'Mar'):
  season = 'Spring'
elif month in ('Jul', 'Aug', 'Sep'):
  season = 'Summer'
else:
  season = 'Fall'
if month == 'Mar' and dayOfMonth > 19:
  season = 'Spring'
elif month == 'Jun' and dayOfMonth > 20:
  season = 'Summer'
elif month == 'Sep' and dayOfMonth > 21:
  season = 'Fall'
elif month == 'Dec' and dayOfMonth > 20:
  season = 'Winter'
print(f'{month} {dayOfMonth} is in {season}')


# 6. Print the result as follows:
#      <Mmm> <dd> is in <season> 
# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
