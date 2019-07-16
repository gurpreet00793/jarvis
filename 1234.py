import datetime
import time
print(time.gmtime(0))
print(time.asctime(time.gmtime(0)))
print(time.ctime())
print(datetime.MINYEAR)
print(datetime.MAXYEAR)
print(datetime.date.today())

from datetime import date
print(date.today())
print(date.fromtimestamp(60*60*24))

list=[1,2,3]
import math
print(math.floor(3.5))
print(math.ceil(3.5))
print(math.fabs(-3.5))
print(math.pow(2,4))
print(math.fsum(list))
print(math.gcd(3,9))

import os
print(os.getcwd())
print(os.name)
print(os.listdir())
print(os.environ)
