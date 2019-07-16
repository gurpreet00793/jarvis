"""scope of variable :-the scope os a variable determines the portion
of the program where you can access a particular identifier.

there are two basic scope of variables in python -
1.global variable:- variables that are defined outside have a global scope.

2.local variable:-variables that are defined inside a function body have a local
scope."""

#total =0; #this is a variable.

#def sum(arg1,arg2):
    #total=arg1+arg2 #here total is local variable
    #print("inside the function local total :",total)
    #return total;

#sum(10,20);
#print("outside the function local total :",total)

""""module:- a module is a file consisting of python code. a module can define
    function,classes and variable.a module can also include runnable code>

    ex:-
    module name-calculation.py
    def myfirstfunction(list):
        sum=0
        for x in list:
            sum=sum+x
        print(sum)

    file name -abcd.py
    import calculation
    abc=[20,78,30]
    calculation.myfirstfunction(abc)"""

#total =0; #this is a variable.

def sum(arg1,arg2):
    #global total
    total=arg1+arg2 #here total is local variable
    print("inside the function local total :",total)
    return total;

print(sum(10,20));
print("outside the function local total :",total)

def multiply(arg1,arg2):
    #global total
    total=arg1*arg2 #here total is local variable
    print("inside the function local total :",total)
    return total;
 
print(multiply(5,7))
print("outside the function local total :",total)
