person={'name':'tony','age':22}

print('before dictionary is updated')
keys=person.keys()
print(keys)

person.update({'salary':35000.05})#to update an item
print('\n after dictionary is updated')
print(keys)

person={'name':'tony','age':22,'salary':35000.05}
print(person.keys())

empty_dict={}
print(empty_dict.keys())



sales={'apple':3,'orange':8,'grapes':20}

element=sales.pop('apple')
print('the poped element list:',element )
print('the dictionary is sales:',sales)

sales={'apple':3,'orange':8,'grapes':20}
element=sales.pop('guava','banana')
print('the poped element is:',element)
print('the dictionary is:',sales)


d={1:"one",2:"three"}
d1={2:"two"}

d.update(d1)
print(d)

d1={3:"four"}
d.update(d1)
print(d)

d2={3:"three"}#update 
d.update(d2)
print(d)

sales={'apple':3,'orange':8,'grapes':20}#prints the value of items
print(sales.values())


"""sales={'apple':3,'orange':8,'grapes':20}
element=sales.pop('guava')
print(sales)"""

