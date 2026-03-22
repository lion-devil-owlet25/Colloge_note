#Methods of Python String

#upper()
message = 'python is fun'

# convert message to uppercase
print(message.upper())

# first string
firstString = "python is awesome!"

# second string
secondString = "PyThOn Is AwEsOmE!"

if(firstString.upper() == secondString.upper()):
    print("The strings are same.")
else:
    print("The strings are not same.")

#lower()

message = 'PYTHON IS FUN'

# convert message to lowercase
print(message.lower())

# first string
firstString = "PYTHON IS AWESOME!"

# second string
secondString = "PyThOn Is AwEsOmE!"

if(firstString.lower() == secondString.lower()):
    print("The strings are same.")
else:
    print("The strings are not same.")

#split()

cars = 'BMW-Tesla-Range Rover'

# split at '-'
print(cars.split('-'))

text= 'Love thy neighbor'

# splits at space
print(text.split())

grocery = 'Milk, Chicken, Bread'

# splits at ','
print(grocery.split(', '))

# Splits at ':'
print(grocery.split(':'))

grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 0))

#replace()

text = 'bat ball'

# replace 'ba' with 'ro'
replaced_text = text.replace('ba', 'ro')
print(replaced_text)

song = 'cold, cold heart'

# replacing 'cold' with 'hurt'
print(song.replace('cold', 'hurt'))

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurrences of 'let'
print(song.replace('let', "don't let", 2))

song = 'cold, cold heart'
replaced_song = song.replace('o', 'e')

# The original string is unchanged
print('Original string:', song)

print('Replaced string:', replaced_song)

song = 'let it be, let it be, let it be'

# maximum of 0 substring is replaced
# returns copy of the original string
print(song.replace('let', 'so', 0))

#find()

message = 'Python is a fun programming language'

# check the index of 'fun'
print(message.find('fun'))

quote = 'Let it be, let it be, let it be'

# first occurance of 'let it'(case sensitive)
result = quote.find('let it')
print("Substring 'let it':", result)

# find returns -1 if substring not found
result = quote.find('small')
print("Substring 'small ':", result)

# How to use find()
if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))

# Substring is searched in ' small things with great love' 
print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))

#rstrip()

title = 'Python Programming   '

# remove trailing whitespace from title
result = title.rstrip()
print(result)

random_string = 'this is good    '

# Trailing whitespace are removed
print(random_string.rstrip())

# 'si oo' are not trailing characters so nothing is removed
print(random_string.rstrip('si oo'))

# in 'sid oo', 'd oo' are the trailing characters, 'ood' is removed from the string
print(random_string.rstrip('sid oo'))
website = 'www.programiz.com/' 

print(website.rstrip('m/.'))

#startswith()
message = 'Python is fun'

# check if the message starts with Python
print(message.startswith('Python'))

text = "Python is easy to learn."

result = text.startswith('is easy')
print(result)

result = text.startswith('Python is ')
print(result)

result = text.startswith('Python is easy to learn.')
print(result)

text = "programming is easy"
result = text.startswith(('python', 'programming'))

print(result)

result = text.startswith(('is', 'easy', 'java'))

print(result)

# With start and end parameter
# 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)
print(result)

#isnumeric()

pin = "523"

# checks if every character of pin is numeric 
print(pin.isnumeric())

symbol_number = "012345"

# returns True as symbol_number has all numeric characters  
print(symbol_number.isnumeric()) 

text = "Python3"

# returns False as every character of text is not numeric 
print(text.isnumeric())

# string with superscript 
superscript_string = '²3455'
print(superscript_string.isnumeric())

# string with fraction value 
fraction_string = '½123'
print(fraction_string.isnumeric())

#index()

text = 'Python is fun'

# find the index of is
result = text.index('is')
print(result)

sentence = 'Python programming is fun.'

result = sentence.index('is fun')
print("Substring 'is fun':", result)

#result = sentence.index('Java')
#print("Substring 'Java':", result)

sentence = 'Python programming is fun.'

# Substring is searched in 'gramming is fun.'
print(sentence.index('ing', 10))

# Substring is searched in 'gramming is '
print(sentence.index('g is', 10, -4))

# Substring is searched in 'programming'
#print(sentence.index('fun', 7, 18))

