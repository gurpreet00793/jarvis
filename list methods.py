a=["hello",5,8]
print(a)

a.append(3)
print(a)

a.extend("python")#it seprates the string into single characters
print(a)

a.insert(2,"program")#it doesn"t seprates the string into characters
print(a)

a.remove("h")#it removes H of p,y,t,h,o,n becuz here H is a single charcter
print(a)

a.pop(0)#removes the element which is located on 0 index
print(a)

a.pop()#removes the last object from the list 
print(a)

b=a.count(5)#counts the value how many time it is available 
print(b)

a.reverse()#reverse the whole list
print(a)

a=[4,5,7,2,5]#sort the given set 
a.sort()
print(a)

print(a.index(7))#find the index at which 7 is located

