"""num=int(input("enter the number"))

if num%2==0 :
    print("even number")
else:
    print("odd")
"""

user=int(input("enter a number"))

if user>1:
    i=2
    while i<user:
        if user%i==0:
            print("not prime")
            break
        i=i+1
    else:
        print("prime no")
else:
    print("u have entered a negitive number or not a prime number")
