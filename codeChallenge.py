import sys

# Take input or give default input
inputString = input('Please enter the string to process')
if not inputString:
    inputString = '(id,created,employee(id,firstname,employeeType(id), lastname),location)'

# Check that nesting in () is valid
leftParen = 0
rightParen = 0
for char in inputString:
    if char == '(':
        leftParen += 1
    elif char == ')':
        rightParen += 1
if leftParen != rightParen:
    print('Invalid input')
    sys.exit()

