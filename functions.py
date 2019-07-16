"""function:-

in python ,function is a group of related statements that perform a
specific task.
function helps to break our program smaller and modular chunks.
as our program grows larger and larger ,function make it more
organised and managable.
furthermore,it avoids repition and makes code resumable.
function blocks begin with the keyword "def" followed by fuction name and
paranthesis(()).

syntax:-
def functionname( parameters):
    statements..
    .....
    returns[expression]

ex:-without parameter

def myfirst function()
     print("hello World")
myfirstfuction()


ex:-with parameter

def my function(x)
      print(x)

myfirst function("hello world")"""

"""def myfirstfunction(x):
    
    print(x)

myfirstfunction("hello world")

def myfunction(x):
    print(x)
myfunction("hello world")"""

def myfunction(x): #x=[1,2,3,4,5,6]
    print(x)
    sum = 0
    for a in x:
        sum=(a+sum)
    print(sum)

myfunction([1,2,3,4,5,6])

#tupple

a=(1,2,3,4,5)

myfunction(a)

#set
b={1,2,3,4,5,6,7}

myfunction(b)

"""def myfirstfunc(list):
         sum=0
         for x in list:
            sum=sum+x
         print(sum)

    abc=[1,2,3]
    myfunction(abc)

    2nd :-

    def my fuction(list= [1,2,3])
         sum=0
         for x in list:
            sum=sum+x
        print(sum)

      my function()

      3rd:-

      def myfunction(list)
            sum=0
            for x in list:
                sum=sum+x
            return(sum)
        abc=[1,2,3]
        print(myfunction(abc))
#add
def myfun(a,b):
    ans=(a+b)
    print(ans)
    
a=3
b=2
myfun(a,b)


#substraction
def myfun1(a,b):
    ans=(a-b)
    print(ans)
    
a=3
b=2
myfun1(a,b)


x,y=98,89

myfun1(x,y)
#multiply
def func(a,b):
    ans=(a*b)
    print(ans)
a=5
b=2
func(a,b)
#ex
a=9
b=5

func(a,b)
#divide
def func2(a,b):
    ans=(a/b)
    print(ans)
a=2
b=6
func2(a,b)

#power
def func1(b,p):
    ans=b**p
    print(ans)
b=2
p=5
func1(b,p)
#ex
b=2
p=3
func1(b,p)
#maximum

def a(li):
    

    x=li[0]
    for i in li:
        if x<i:
            x=i
    return x

li=[1,2,7,4,5,6]

print(a(li))

lis=[1,5,9,7,3,8,4]

print(a(lis))
#minimum

def func2(list):
    x=list[0]
    for i in list:
        if x>i:
            x=i
    return x

list=[5,8,7,9,3,1]
print(func2(list))

#calculator
def myfun(a,b):
    ans=(a+b)
    print(ans)
    
a=3
b=2
myfun(a,b)

def myfun1(a,b):
    ans=(a-b)
    print(ans)
    
a=3
b=2
myfun1(a,b)

def func(a,b):
    ans=(a*b)
    print(ans)
a=5
b=2
func(a,b)
def func2(a,b):
    ans=(a/b)
    print(ans)
a=2
b=6
func2(a,b)"""

def add(x,y):
    print(x+y)

def subtract(x,y):
    print(x-y)

def multiply(x,y):
    print(x*y)


def divide(x,y):
    print(x/y)

def power(x,y):
    print(x**y)

print("select")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
print("5.power")

choice=input("enter choice 1/2/3/4/5 :")

x=(int(input("enter 1st")))

y=(int(input("enter 2nd value")))


if choice == "1":
    add(x,y)
    
elif choice == "2":
    subtract(x,y)


elif choice== "3":
    multiply(x,y)

elif choice== "4":
    divide(x,y)

elif choice== "5":
    power(x,y)

else:
    print("invalid")

    





