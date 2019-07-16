my_dict={}#empty dictionary
print(my_dict)
my_dict={1:'apple',2:'ball'}#dictionary with integer key
my_dict={'name':'john',1:[2,4,3]}#dictionary with mixed key
print(my_dict)
print(my_dict['name'])
print(my_dict[1])
print(my_dict.get('name'))
print(my_dict[1][0:2])
print(my_dict['name'][0:3])


my_dict=dict({1:'apple',2:'ball'})
print(my_dict[1])#print the value above 
print(my_dict[2])
my_dict=dict([(1,'apple'),(2,'ball')])
print(my_dict.get(1))#print with help of get function

my_dict={'name':'jack','age':26}
print(my_dict['name'])#output:jack

print(my_dict['age'])#output: 26


