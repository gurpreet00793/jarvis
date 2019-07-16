if(1): 
  print("1-got a true expression value ")


var1,var2=100,0
if var1:
  print("1-got a true expression value ")
  print(var1)
  
if var2:
  print("2-got a true expression value")
  print(var2)
  print("good bye!")

if(not(var2)):
    print("var2 is empty")

if((var1 == 100) and (var2 == 0)):
    print("both conditions is true using and")

if((var1 == 100) and (var2 != 0)):
    print("any of 1 condition is true")

if((var1!=100)and(var2!=0)):
    print("both the conditions are false")

if((var1 == 100) or (var2 !=0)):
    print("one of two consitions is true")

if((var1==100)or(var2==0)):
    print("both conditions are true")


a,b,c=100,20,200
if (a>b)and (a>c):
    print("a is hightest ")


if (b>a)and(b>c):
    print("b is highest")


if (c>a) and(c>b):
    print("c is highest")

var=100
if var==200:
    print('1-got a true expression value')
    print(var)


elif var==150:
    print('2-got a true expression value')
    print(var)

elif var==100:
    print('3-got a true expression value')
    print(var)

else:
    print('4-got a false expression')
    print(var)

var=100
if var<200:
   print('expression values is less than 200')
  if var==150:
     print('which is 150')
  elif var==100:
   print('which is 100')
  elif var==145:
   print('which is 145')
  else:
  print('neighter 150,145&100')
else:
print('other number')
