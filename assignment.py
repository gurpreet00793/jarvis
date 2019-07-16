
"""#Ques no. 2

class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print("Student Name:- ",self.name,"     "" Rollno :- ",self.rollno)

Stu1=student("tony",101)
Stu2=student("steve",102)
Stu3=student("stephen",103)
Stu4=student("natasha",104)
Stu5=student("bruce",105)
Stu6=student("peter",106)
Stu1.display()
Stu2.display()
Stu3.display()
Stu4.display()
Stu5.display()
Stu6.display()

#ques no 1

class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*radius**2
    def circumfrance(self):
        return 2*3.14*radius

radius=float(input("enter value"))
xyz1=circle(radius)
print(xyz1.area())
print(xyz1.circumfrance())


#ques no 3
class temperature:
    def __init__(self,celcius,fah):
        self.celcius=celcius
        self.fah=fah

    def convert(self):
        return  celcius*1.8+32
       

    def convert2(self):
        return (fah-32)*5/9
       

celcius=float(input("enter value"))
fah=float(input("enter value"))
av=temperature(celcius,fah)
print(av.convert())
print(av.convert2())"""

"""#ques no 4
class moviedetails:
    def __init__(self,moviename,artist,year,rating):
        self.moviename=moviename
        self.artist=artist
        self.year=year
        self.rating=rating
    def display(self):
        print("moviename :-",self.moviename,"\n artist name:-",self.artist,"\n year",self.year,"\n rating",self.rating)
    def update(self,a1,a2,a3,a4):
        self.moviename,self.artist,self.year,self.rating=a1,a2,a3,a4

abc=moviedetails("Avengers Endgame","robert downey jr",2018,10)
abc.display()
abc.update("Avengers Returns ","robert downey Jr.",2025,10)
abc.display()

#ques no 5
class expenditure:
    def __init__(self,expen,saving):
        self.expen=expen
        self.saving=saving
    def display(self):
        print("expediture:-",self.expen,"saving-",self.saving)
    def salary(self):
        return expen+saving

expen=int(input("enter value"))
saving=int(input("enter value"))
avc=expenditure(expen,saving)
avc.display()
print(avc.salary())"""


class avengers:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def display(self):
        print("name:-",self.name,"role:-",self.role)


class newavengers(avengers):
    "same"
   
    

abc=newavengers("tony  \n","leader")
abc.display()

class ultra(avengers):
    def __init__(self,age):
        self.age=age
    def display(self):
        print("age:-",self.age)

abc=ultra(36)
abc.display()


class xmen:
    def __init__(self,name,role):
        self.name=name
        self.role=role

class avengers1:
    def __init__(self,name,role):
        self.name=name
        self.role=role

class newmutants(xmen,avengers1):
    def __init__(self,name,role):
        xmen.__init__(self,name,role)
        avengers1.__init__(self,name ,role)
    def display(self):
        print("name:-",self.name,"role:-",self.role)

abcd=newmutants("tony \n","iron man")
abcd.display()





