a={'name':'john doe','age':25,'subject':('physics','math','chemistry')}
print(a['subject'][0][2:7])

d={1:"one",2:"two"}
d.clear()
print('d=',d)

person={'name':'phill','age':22}
print('name:',person.get('name'))
print('age:',person.get('age'))
print('salary:',person.get('salary',50000))


keys={'a','e','i','o','u'}
vowels=dict.fromkeys(keys)
print(vowels)
vowels=dict.fromkeys('seq',10)
print(vowels)
vowels=dict.fromkeys(keys,10)
print(vowels)
dict.get

"""items:-returns a bit of dict (keys,value)tuple pairs
ex:-"""

#random sales dictionary

sales={'apple':2,'orange':3,'grapes':45}

print(sales.items())

"""keys()-returns a new view of the dictionary"s keys.

ex:-"""
person={'name':'tony','age':22}

print('before dictionary is updated')
keys=person.keys()
print(keys)

"""adding an element to the dictionary"""
person.update({'salary':35000.05})
print('\n after dictionary is updated')
print(keys)

#ex:-
person={'name':'tony','age':22,'salary':35000.05}
print(person.keys())

empty_dict={}
print(empty_dict.keys())

"""pop(key['d']):-removes the item with key and returns its value
or d if key is not found if d is not provided any key is not found it will give key error"""

#random sales dictionary
sales={'apple':3,'orange':8,'grapes':20}

element=sales.pop('apple')
print('the poped element list:',element )
print('the dictionary is sales:',sales)

#eg:-
#random sales dictionary
#sales={'apple':3,'orange':8,'grapes':20}
#element=sales.pop('guava')
#output:-key error

#eg:-
sales={'apple':3,'orange':8,'grapes':20}
element=sales.pop('guava','banana')
print('the poped element is:',element)
print('the dictionary is:',sales)

"""set default(key[d]):-
if key is the dictionary returns its value.if not insert
d as the key and return d(default to none)

eg:-"""

sales={'apple':3,'orange':8,'grapes':20}
elements=sales.setdefaults('guava','banana')
print('the poped element is:',element)
print('the dictionary is:',sales)

"""->update([other]):-update the dictionary with the key 1 value pairs from the others
overwriting existing key"""

d={1:"one",2:"three"}
d1={2:"two"}

#update the value of key2
d.update(d1)
print(d)

d1={3:"four"}

#add element with value four

d.update(d1)
print(d)

"""->returns a new views of the dictionary value"""

#random sales dictionary

sales={'apple':3,'orange':8,'grapes':20}
print(sales.values())
