import operators

print("select")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
print("5.power")

choice=input("enter choice 1/2/3/4/5 :")

x=(int(input("enter 1st")))

y=(int(input("enter 2nd value")))


if choice == "1":
    operators.add(x,y)
    
elif choice == "2":
    operators.subtract(x,y)


elif choice== "3":
    operators.multiply(x,y)

elif choice== "4":
    operators.divide(x,y)

elif choice== "5":
    operators.power(x,y)

else:
    print("invalid")

    
