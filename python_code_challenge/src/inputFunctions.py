import sys
import re

# Take input or give default input
def getInput():
    inputString = input('Please enter the string to process')
    if not inputString:
        inputString='(id,created,employee(id,firstname,employeeType(id),lastname),location)'
    return inputString

# Check that nesting in "()"" is valid
# String will need to start with "(" and end with ")"
# String will need same number of "(" and ")"
def isValid(inputString):
    if inputString.count('(') != inputString.count(')'):
        return False
    elif inputString[0] != '(' or inputString[-1] != ')':
        return False
    else:
        return True

# Process inputString to list
# First removes start and end parenthesis
# Split string on "(" ")" and ","
# Filter out "[,]" and "[]"
def processInput(inputString):
    inputString = re.search(r'\((.+)\)', inputString)[1]
    inputString = re.split('([(),])', inputString)
    processedString = filter(lambda s: not (s[:]==',' or s[:]==''), inputString)
    return processedString