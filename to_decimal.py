'''
You are given 2 input strings;  base and number.  Base must satisfy 2 <= base <= 36. 
Number is a string consisting of letters and numbers.
First check if base is valid; then check if number is valid in the given base. 
If both number and base are valid, convert the given number to its decimal representation. 
'''


def to_decimal(base, number):
  if not 2 <= int(base) <= 36:
    return 'Invalid Base'
  else:
    validity_checker = [0]*36
    for ch in number:
      if ch in '0123456789':
        index = int(ch)
        validity_checker[index] = ch
        if index >= int(base):
          return 'Invalid Number'
      else:
        ch = ch.lower()
        index = ord(ch) - 87
        validity_checker[index] = ch
        if index >= int(base):
          return 'Invalid number'
  
  result = 0
  for i, elem in enumerate(reversed(number)):
    result = result + validity_checker.index(elem)*int(base)**i
  return result  
  
  '''
  Comment:
  A number is valid in a given base iff all the characters in the number are 'less than'
  the base.
  '''
