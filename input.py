"""math=input("enter your maths")
physics=input("enter your physics")
chemistry=input("enter your chemistry")
val=int(math)+int(physics)
print(val)"""



name=input("enter name")
math=input("enter marks")
physics=input("enter marks")
chemistry=input("enter marks")
english=input("enter marks")
val=(((int(math)+int(physics)+int(chemistry)+int(english))/400)*100)
print(val)

if val>=90:
   print('name:',name ,"grade A")

elif (val<90)and(val>=75):
   print("grade B")

elif (val>=60)and (val<75):
   print("grade c")

elif (val>=30)and (val<60):
   print("grade d")

else:
   print("fail")
