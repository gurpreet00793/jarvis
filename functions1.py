"""aNONYMOUS FUCTION(Lambda fuction):-

in python ,anonymous function is the function that is defined without a name.
in python anonymous fuctions are definedusing the lambda keyword.hence, anonymous
functions are also called lambda functions.

syntax:-
lambda arguments: expressions

ex:-
double =lambda x:x*2
print(double(5))"""


"""double =lambda x,y:x*y
print(double(5,2))

table =lambda x,y:x*y
x=int(input("enter number"))

while x:
    y=1
    while y<=10:
        z=x*y
        print(table(x,y))
        y=y+1
    x=x+1
    break"""
   
"""li=[1,2,3,4,5,6,7,8,9,10]
func =lambda odd,even,li:
odd=[]
even=[]
x=0
while x<10:
    if li[x]%2==0:
        even.append(li[x])
    else:
        odd.append(li[x])
    x=x+1
print("even",even)
print("odd",odd)"""


even=lambda a:x%2
even_list=[]
odd_list=[]
list=[2,3,4,5,6,7,8,9]
for x in list:
    if even(x)==0:
        even_list.append(x)
    else:
        odd_list.append(x)
        
print(even_list)
print(odd_list)


func=lambda x:x

x=5+5

print(func(x))



list1=[1,2,3,4]#{1,2,3,4}
def abc(x):
    return(x+x)
a=tuple(filter(abc,list1))
print(a)

list1=[1,2,3,4]
def abc(x):
    return(x*x)
a=tuple(round(abc,list1))
print(a)



