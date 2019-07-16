
"""
class parrot:
    def fly(self):
        print("parrots can fly")

    def swim(self):
        print("parrots can not swin")

class penguin:
    def fly(self):
        print("penguins cannot fly")
    def swim(self):
        print("penguins can swim")

def fly_test(bird):
    bird.fly()

bd=parrot()
pg=penguin()
fly_test(bd)
fly_test(pg)

#function overloading

class human:
    def sayhello(self,name=None):
        if name is not None:
            return ("hello"+name)
        else:
            return ("hello")

obj=human()
print(obj.sayhello())
print(obj.sayhello("tony"))


class student:
    def stark(self,name=None,rollno=None):
        if name or rollno is not None:
            return(name or rollno)
        else:
            return("none")
obj1=student()
print(obj1.stark("tony \n"))
print(obj1.stark())

#operator overloading

class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    #adding two objects

    def __add__(self,others):
        return self.a+others.a,self.b+others.b

obj2=complex(1,5)
obj3=complex(5,8)
obj4=obj2+obj3
print(obj4)


class mathematics:

    def addnumbers(x,y):
        return x+y

#create addnumbers static method
mathematics.addnumbers=staticmethod(mathematics.addnumbers)

print("the sum is",mathematics.addnumbers(9,10))"""


class student:
    def __init__(self,name,rollno,branch,classroom):
        self.name=name
        self.rollno=rollno
        self.branch=branch
        self.classroom=classroom
    def display(self):
        print("name:-",self.name,"rollno:-",self.rollno,"branch:-",self.branch,"classroom:-",self.classroom)
    def update(self,classroom1,rollno):
        return self.classroom=classroom1
        return self.rollno=rollno

obj=student()
print=(obj(input("enter name"),int(input("enter value")),input("enter value"),input("classroom"))
obj.display()
obj.update()

    
