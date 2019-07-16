"""LOOP

   A LOOP STATEMENT ALLOWS US TO EXCECUTE A STATEMENT OR GROUP OF STATEMENT MULTIPLE
   TIMES

types of loop
1.while loop
2.for loop

1.while loop:-repeats a statement or group of statements
while a given condition is true .it tests the condition before executing the loop body
or a while loop statement in python programming language
repetadly executes a target statement as long as a given condition is true

syntax:-
while operation
    statement()
"""

li=[1,2,3,4,5,6,7,8,9]
listeven=[]
listodd=[]
i=0
while i<len(li):
    if li[i]%2==0 :
        listeven.append(li[i])
    else:
        listodd.append(li[i])
    i=i+1

print("listeven: ",listeven)
print("listodd: ",listodd)
        
