class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a=A()
b=B()
print (a.f(), b.f())
print (a.g(), b.g())

#ques no 1
class Animal:
    def __init__(self,species,region,life):
        self.species=species
        self.region=region
        self.life=life
    def animal_attribute(self):
        print("species name:",self.species,"region:",self.region,"lifeline",self.life)

class tiger(Animal):
    "same"

p1=tiger("tigers \n","africa \n","20 \n")
p1.animal_attribute()

#ques no 3
class Shape:
    def __init__(self ,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        print(self.length*self.breadth)

class square(Shape):
    "same"

class rectangle(Shape):
    "same"

abcd=square(5,5)
abc=rectangle(5,6)
abcd.area()
abc.area()

#ques no 4

class cop:
    def __init__(self,name,age,exp,designation):
        self.name=name
        self.age=age
        self.exp=exp
        self.designation=designation

    def add(self):
        print(self.age+self.exp)

    def display(self):
        print("name :-",self.name,"age:-",self.age,"exp:-",self.exp,"designation:-",self.designation)

    def update(self,a1,a2,a3,a4):
        self.name=a1
        self.age=a2
        self.exp=a3
        self.designation=a4
               
xy=cop("tony \n","36 \n"," 5years \n","sherrif \n")
xy.display()
xy.update("steve","85","kj","kl")
xy.display()
