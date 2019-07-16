try:
    x=8
    y=0
    a=x/y
    print(a)

except:
    print("not possible")


try:
    av=5+"a"
    print(av)

except:
    print("no way")


li=[1,2,3,4]
    
try:
    c=8
    b=0
    z=c/b
    print(z)

except ZeroDivisionError:
    
    print("ZeroDivisibleError")

except IndexError:
    print("IndexError")


try:
    x=8
    y=0
    z=x/y
    print(z)
except Exception as e:
    print("exception error",e)

print("hello")

try:
    print("tony stark is best avenger")
    x=8/2

except:
    print("love u 3000")
else:
    print("i am ironman")
finally:
    print("tony can beat captain america")



