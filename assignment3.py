#1 time tuple =
"""it is an object returned by gmtime, localtime ,strptime functions containing attribute-value pairs"""

#2.
import time
t1=time.localtime()#all infromation like time,date,year etc. of local host
print(t1)
print(time.strftime('%T',t1))#current time
print(time.strftime('%B',t1))#current month
print(time.strftime('%A',t1))#current day
print(time.strftime('%D',t1))#current date
import math
print(math.factorial(4))
print(math.gcd(150,65))
import os
print(os.getcwd())
print(os.environ)

