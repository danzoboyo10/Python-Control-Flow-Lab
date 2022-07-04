# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):

letter = input('Please enter a letter from the alphabet "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z": ').lower()
# 2. Write the code that determines whether the letter entered is a vowel
if letter == "a" or "i" or "e" or "o" or "u":
  print('You entered a vowel')
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant
if letter == "x":
  print('the letter x is a vowel')

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':




# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
phrase = ''
while phrase != 'quit':
  phrase = input('Please enter a word or phrase: ')
  print(f'What you entered is {len(phrase)} characters long')

# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.



# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 

human_years = int(input('Input a dogs age in humans years: '))
if human_years < 3:
  dog_years = human_years * 10
else:
  dog_years = 20 + (human_years - 2) * 7
print(f"The dog's age in dog years is {dog_years}")
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
print('Enter the lengths of three side of a triangle:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a == b and b == c:
  print(f'A triangle with sides of {a}, {b} & {c} is an equalateral triangle')
elif a != b and a != c and b != c:
  print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
else:
  print(f'A triangle with sides of {a}, {b} & {c} is an isosceles triangle')
  
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length


# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


# Write the code that:
#  Calculates and prints the first 50 terms of the fibonacci sequence.
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

# Print each term and number as follows:
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
#  Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):

month = input('Enter "Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec": ').lower()
print(f'The user entered {month}')


#  Then propts the user to enter the day of the month: 
#      Enter the day of the month:
dayOfMonth = input('Enter "Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday": ').lower()
print(f'The user entered {dayOfMonth}')




#  Calculate what season it is based upon this chart:
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


#  Print the result as follows:
#      <Mmm> <dd> is in <season> 
# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
