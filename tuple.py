my_tuple=("mouse",[8,4,6],(1,2,3))

#output:("mouse",[8,4,6],(1,2,3))
print(my_tuple)
print(my_tuple[0:2])#output:-mouse,[8,4,6]
print(my_tuple[0][3])#element 0=mouse 3=3rd element of mouse
print(my_tuple[1][1])#same as above

t=('p','e','r','m','i','t')
print(t[0])
print(t[5])

t=('p','e','r','m','i','t','e')#used to count how many times a element is repeated in it
print(t.count('e'))#count

t=('p','e','r','m','i','t','e')#locate and tell the index of given element
print(t.index('e'))#index


a=[5]
print(type(a))
b={5}
print(type(b))
c=("h",5)
print(type(c))
d=(5,)
print(type(d))
a='tony'
print(type(a))
a=5
print(type(a))
