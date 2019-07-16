my_marks={}
ans=int(input("9+9:"))
print(ans)

# = assigns the value to the variable
# == compare the known value if answer is already known
if (ans == 18):
    print("welcome to stage 1")
    physics=int(input("enter marks"))
    my_marks["physics"]=physics
    point=physics
    print(physics)
    if physics >=60:
        print("u completed stage 1")
        ans=int(input("4+4:"))
        print(ans)
        if ans==8:
            print("welcome to stage 2")
            maths=int(input("enter marks"))
            my_marks["maths"]=maths
            point+=maths
            print(maths)
            if maths >=50:
                print("u completed stage 2")
                ans=int(input("7+7:"))
                print(ans)
                if ans==14:
                        print("welcome to stage 3")
                        english=int(input("enter marks"))
                        my_marks["english"]=english
                        print(english)
                        if english >=75:
                            print("u have completed the game",my_marks)
                            print(physics+maths+english)
                        else:
                            print("u failed to clear final stage")
                            print(physics+maths)
                else:
                        print("u failed to enter in stage 3")
                        print(physics+maths,my_marks)
                        
            else:
                print("u failed to complete stage 2")
                print(physics)
                
        else:
            print("you failed to enter in stage 2",my_marks)
            print(physics)
                
    else:
        print("you failed to complete stage 1")
        print("0")
    
        
else:
    print("you cant clear stage one")
    print("0")

