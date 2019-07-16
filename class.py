"""class myclass:
    x=5
    y=6
    z=x+y


p1=myclass()
print(p1.z)"""

#def  name():
#        print("stark")
#name()

"""class avengers:
    def __init__(self,name,typ):
        self.name=name
        self.typ=typ
p1=avengers("stark","energy")
print(p1.name,p1.typ)"""

"""__init__()function :-
use the __init__() function to assign values of object properties,or other operations
that are neccesary to do when the object is being created.

ex:-
class person:
   def__init__(self,name,age):
         self.name=name
         self.age=age

    def  my func(self):
         print("hello my name is"+self.name)
p1=person("john",36)
p1.myfunc()


note:- the__init__() function is called automatically every time the class is being
used to create a new object.
note:-the self parameter is a reference to the current instance of the class is being
used to access variables that belong to the class."""

"""class person:
   def __init__(self,name,age):
       self.name=name
       self.age=age
   def  myfunc(self):
       print("hello my name is",self.name)
       print("my age is",self.age)
p1=person("john",36)
p1.myfunc()"""


class employee:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
        
    def info(self):
        print("my name is ",self.name ,"my contact number is ",self.contact)
p1=employee("tony",8958798745)
p2=employee("steve",7896589687)
p3=employee("strange",6985774896)
p1.info()
p2.info()
p3.info()

class solution:
    def __init__(self,radius):
        self.radius=radius
    def getarea(




