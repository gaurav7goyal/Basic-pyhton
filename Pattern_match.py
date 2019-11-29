'''
##regex pattern matching in pyhton
>>> help(re)
https://www.tutorialspoint.com/python/python_reg_expressions.htm
The match Function
This function attempts to match RE pattern to string with optional flags.
Here is the syntax for this function −

re.match(pattern, string, flags=0)

'''

#!/usr/bin/python
import re

line = "Cats and dogs are smarter than dogs"

matchObj = re.match( r'(.*) and (.*) .*', line, re.M|re.I)
	##falg use bitwise | operator use multiple flag assign### 
	#re.M= multiline flag and re.I=ignorecase falg#
if matchObj:
   print( "matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
