# F-STRINGS LESSON
# Explains every bit of Python f - string feature.It is an implementation of the PEP 498 specifications
# for formatting Python strings in an entirely new way.Since it is available from Python version 3.6, so make sure you have the same or higher version to use f-strings.

# Python f - string uses a new convention that requires every string should begin with the ‘f’ prefix.And hence, it derives the name from this synthesis.One of the main advantages that it brings is making the string interpolation easier.Also, it insists on having a simple way to stuff Python expression in a string literal for formatting.

# Other two methods of formatting a string are by using the % operator or the format() function.
# We’ve got both of these covered here – Format Strings in Python.

# Python F - string with Examples

# What are f - strings in Python?
# F - strings are a new method for handling strings in Python.
# It is based on the PEP 498 design specs.To create an f-string, you need to prefix it with the ‘f’ literal.
# Its primary purpose is to simplify the string substitution.
# It pushes for a minimal syntax and evaluates expressions at run-time.
# This feature is not available in any version below Python 3.6.Hence, use it or a higher version of Python.

# Python f - string syntax
# Create an f - string in Python.
# f'Python {expr}'
# The expr can be anything from a constant, an expression, string or number, or a Python object, etc.
version = 3.6
feature = 'f-string'
str_final = f'Python {feature} was introduced in version {version}.'
print(str_final)
# Result:
# Python f - string was introduced in version 3.6.

# F - strings examples
title = 'Joshua'
experience = 24
dyn_str = f'My title is {title} and my exp is {experience}'
print(dyn_str)
# We can use f or F interchangeably
print(F'My title is {title} and my exp is {experience}')
title = 'Sophia'
experience = 14
# dyn_str doesn't get re-evaluated, if the expr changes later.
print(dyn_str)
# Python is an interpreted language and runs instructions one by one.
# If the f - string expression is evaluated, then it won’t change whether the expression changes or not.
# Hence, in the above example, the dyn_str value is intact even after the title and experience variables
# have got different values.

# Using f - strings in conversions
# F - strings allows conversion like converting a Python datetime to other formats.
from datetime import datetime
# Initializing variables
title = 'Abraham'
experience = 22
cur_date = datetime.now()
# Some simple tests
print(f'Exp after 10 years will be {experience + 10}.')  # experience = 32
print(f'Title in quotes = {title!r}')  # title = 'Abraham'
print(f'Current Formatted Date = {cur_date}')
print(f'User Formatted Date = {cur_date:%m-%d-%Y}')
# Output:
# Exp after 10 years will be 32.
# Title in quotes = 'Abraham'
# Current Formatted Date = 2019 - 07 - 14 07: 06:43.465642
# User Formatted Date = 07 - 14 - 2019

# Generate raw string from an f-string
# F - strings can also produce raw string values.

# To print or form a raw string, we need to prefix it using the ‘fr’ literal.
from datetime import datetime
print(f'Date as F-string:\n{datetime.now()}')
print(fr'Date as raw string:\n{datetime.now()}')
# The difference between f vs. fr strings.
# Date as F - string:
# 2019 - 07 - 14 07: 15:33.849455
# Date as raw string:\n2019 - 07 - 14 07: 15:33.849483

# Using f - string with classes
# Use of F - strings to format Python class objects or their attributes.See the example below:
class Student:
    age = 0
    className = ''

    def __init__(self, age, name):
        self.age = age
        self.className = name

    def __str__(self):
        return f'[age={self.age}, class name={self.className}]'

std = Student(8, 'Third')
print(std)

print(f'Student: {std}\nHis/her age is {std.age} yrs and the class name is {std.className}.')
# Output:
# [age = 8, class name=Third]
# Student: [age = 8, class name=Third]
# His / her age is 8 yrs and the class name is Third.

# Python F - string with a user-defined function
# Custom function and see how can it be called from the f-string
def divide(m, n):
    return m // n
m = 25
n = 5
print(f'Divide {m} by {n} = {divide(m, n)}')
# Output:
# Divide 25 by 5 = 5

# Whitespaces in f - strings
# Python dismisses any whitespace character that appears before or after the expression in an f - string.
# However, if there is some in the overall sentence, then it is eligible to get displayed.
kgs = 10
grams = 10 * 1000
print(f'{kgs} kg(s) equals to {grams} grams.')
# output:
# 10 kg(s) equals to 10000 grams.

# Python f - string with Anonymous function

# Anonymous function, also known as Python Lambda expression, can work alongside f - strings.
# However, you need to be cautious when using “!” or “:” or “}” symbols.
# If they aren’t inside parentheses, then it represents the end of an expression.

# lambda expr uses a colon which can cause adverse behavior.
# lambda_test = f"{lambda x: x * 25 (5)}"
# error:
# File "", line 1
#     (lambda x)
#             ^
# SyntaxError: unexpected EOF while parsing
# Use colon safely with Lambda, wrap it inside parentheses.
lambda_test = f"{(lambda x: x * 25)(5)}"
print(lambda_test)
# Output:
# 125

# Braces  within an f - string
# To see a pair of “{}” in your string, then have double braces to enclose:
lambda_test = f"{{999}}"
print(lambda_test)
# Output:
# {999}
# triple braces, then also, it will only show one set of braces.
lambda_test = f"{{{999}}}"
print(lambda_test)
# Output:
# {999}

# Backslashes inside an f - string
# backslash escapes in a part of a Python f - string.But, we can’t use them to escape inside the expression.
#lambda_test = f"{"Machine Learning"}"
# print(lambda_test)
# error:
# File "jdoodle.py", line 2
# lambda_test = f"{"Machine Learning"}"
#                    ^
# SyntaxError: invalid syntax

# Fix expression and use it directly in the f-string:
topic = "Machine Learning"
lambda_test = f"{topic}"
print(lambda_test)
# Output:
# Machine Learning
# Also, note down that you should not insert comments(using a “  # ” character ) inside f-string expressions.
# # It is because Python would treat this as the syntax error.