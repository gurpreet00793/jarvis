"""i=["apple","mango","graphes"]
a=0
while a<3:
    print(i)
    a=a+1

j=0
while j<6:
    j=j+1
    if j==2:
        continue
    print(j)

i=0
while i<6:
    print(i)
    if i==3:
        break
    i=i+1


i=5
while i>=1:
    print('*'*i)
    i=i-1

i=1
while i<=5:
    print('*'*i)
    i=i+1

i=5
j=0
while i>=1:
    print(" "*j," *"*i)
    i=i-1
    j=j+1"""


"""num=1
while num<=5:
    i=1
    while i<= 10:
        ans=num*i
        print(num,"*",i,"=",ans,"\n")
        i=i+1
    num=num+1  """  


list1=["1.Write function converts a string to all uppercase?",
      "2.Which of the following function of dictionary gets all the keys from the dictionary?",
      "3.What is the output of print list[0] if list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]?",
      "4.Which of the following function checks in a string that all characters are in lowercase?",
      "5.Which of the following function merges elements in a sequence?",
      "6.Which of the following function convert an object to a string in python?",
      "7.Which of the following function checks in a string that all characters are in uppercase?",
      "8.Which of the following is correct about Python?",
      "9.What is the output of L[2] if L = [1,2,3]?",
      "10.What is the following function sorts a list?"]

list2=["1.upper()",
       "1.getkeys()",
       "1.[ 'abcd', 786 , 2.23, 'john', 70.2 ]",
       "1.islower()",
       "1.isupper()",
       "1.int(x [,base])",
       "1.isupper()",
       "1.It supports automatic garbage collection",
       "1.1",
       "1.list.reverse()"]

list3=["2.isdecimal()",
       "2.key()",
       "2.abcd",
       "2.isnumeric()",
       "2.join(seq)",
       "2.long(x [,base] )",
       "2.join(seq)",
       "2.It can be easily integrated with C, C++, COM, ActiveX, CORBA, and Java.",
       "2.2",
       "2.list.sort([func])"]

list4=["3.swapcase()",
      "3.keys()",
      "3.Error",
      "3.isspace()",
      "3.len(string)",
      "3.float(x)",
      "3.len(string)",
      "3.Both of the above.",
      "3.3",
      "3.list.pop(obj=list[-1])"]

list5=["4.title()",
       "4.None of the above.",
       "4.None of the above",
       "4.istitle()",
       "4.ljust(width[, fillchar])",
       "4.str(x)",
       "4.ljust(width[, fillchar])",
       "4.None of the above.",
       "4.None of the above",
       "4.list.remove(obj)"]

list6=["1",
       "3",
       "2",
       "1",
       "2",
       "4",
       "1",
       "2",
       "3",
       "2"]

total=0
i=0
while i<len(list2):
    print(list1[i])
    print(list2[i])
    print(list3[i])
    print(list4[i])
    print(list5[i])
    

    ans=input("enter")
    if list6[i] == ans:
        total+=2
    i=i+1
print("result",total)
   
      
       
