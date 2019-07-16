a=21
b=10
c=0

c=a+b
print(c)
c+=a#c=c+a
print("value of c",c)

c*=a#c=c*a
print("value of c",c)

c/=a#c=c-a
print("value of c",c)

c%=a#c=c/a
print("value of c",c)

c**=a#c=c**a
print("value of c",c)

c//=a#c=c//a
print("value of c",c)



c=52

c&=a#a&b means 00001100
print("value of c",c)

c|=a#a|b means 00111101
print("value of c",c)

c=52
c^=a #a^b=49(00110001)
print("value of c",c)

c=52
a=2
c>>=a#a>>2=15 means(00001111)
print("value of c",c)

c<<=a#a<<2=2=240 means(11110000)
print("value of c",c)

#COMPARISON OPERATOR
x=5
y=3
print(x==y)#false
print(x!=y)#true
print(x>y)#true
print(x<y)#flase
print(x>=y)#true
print(x<=y)#false

#LOGICAL OPERATORS
x=5

print(x>3 and x<10)
# returns true bcuz 5 >3 and 5<10 both condition are true
print(x>3 and x<4)
"""returns true because one of the conditions are true(5 is greater
than 3 but 5 is not less than 4"""
print(not(x>3 and x<10)
#returns false bcuz not is used to reverse the result

#IDENTICAL OPERATOR


D1='hello world'
E1={1:'a',2:'b'}

print('H' in D1)
print('hello not in D1)
print(1 in E1)
print('a' in E1)
