A={1,2,3,4}#clear all the elemets from the set
A.clear()
print(A)

num={2,3,4,5}#delete a number from the set which is given by user
num.discard(3)
num.discard(10)
num.discard(4)
print('num=',num)

A={10,20,25,30,35}#delete a number from the set randomly

print(A.pop())
print(A)
print(A.pop())
print(A)

A={'a','b','c','d'}#remove a selected number from the set
A.remove('b')#but if a element doesn't exits if will give error
A.remove('d')
print('A=',A)

A={1,2,3,4,5,6}#difference is used to remove the elemets with are available in both sets
B={2,3,9,10,11}
print(A-B)
#{1,4}
print(B-A)
#{9}

A={'a','c','g','d'}
B={'c','f','g'}
print(A.difference_update(B))#returns none
print(A)#(a,d)
print(B)#(c,g,f)
print(B.difference_update(A))
print(A)#(a,d)
print(B)#(c,d,f)
print('\n')

a={1,2,3,4,5}
b={2,4,5,8,9}
print(a.intersection(b))
print(b.intersection(a))

a1={1,2,3,4,5}
b1={2,4,5,8,9}
print(a1.isdisjoint(b1))#if it doesn't contain anything common returns true
print(b1.isdisjoint(a1))#if it contain common elements returns false
      
A={1,2,3}
B={1,2,3,4,5}
C={1,2,4,5}
print(A.issubset(B))#true bcuz A contains all elements present in B
print(B.issubset(A))#false bcuz B contains extra elements than A
print(C.issubset(B))#true bcuz C contains all elements present in B


d={}
print(d.issubset(A))
