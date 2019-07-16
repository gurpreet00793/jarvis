#while loop:
'''
i=1
while i<=10:
    print(i)
    i+=1

list1=['apple','mango','guava','litchi','orange','pineapple','tomato']
i=0
while i<len(list1): #i<7
    print(list1[i])
    i+=1


i=1
while i<=10:
    if i==5:
        i+=1
        continue
    print(i)
    i+=1

i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1

i=5
while i>=1:
    print('*'*i)
    i-=1

i,k=5,0
while i>=1:
    print(' '*k,' *'*i)
    i-=1
    k+=1
'''
'''
num=1
while num<=10:
    i=1
    print('\nTable of ',num,' : ')
    while i<=10:
        print(num,' * ',i,' = ',num*i)
        i+=1
    num+=1
'''

que=['Grand Central Terminal, Park Avenue, New York is the world\'s','Entomology is the science that studies',\
     'Eritrea, which became the 182nd member of the UN in 1993, is in the continent of','Garampani sanctuary is located at',\
     'For which of the following disciplines is Nobel Prize awarded?','Hitler party which came into power in 1933 is known as','FFC stands for',\
     'Fastest shorthand writer was','Epsom (England) is the place associated with','Galileo was an Italian astronomer who']
opt1=['largest railway station','Behavior of human beings','Asia','Junagarh, Gujarat','Physics and Chemistry','Labour Party','Foreign Finance Corporation',\
      'Dr. G. D. Bist','Horse racing','developed the telescope']
opt2=['highest railway station','Insects','Africa','Diphu, Assam','Physiology or Medicine','Nazi Party','Film Finance Corporation','J.R.D. Tata','Polo',\
      'discovered four satellites of Jupiter']
opt3=['longest railway station','The origin and history of technical and scientific terms','Europe','Kohima, Nagaland','Literature, Peace and Economics',\
      'Ku-Klux-Klan','Federation of Football Council','J.M. Tagore','Shooting','discovered that the movement of pendulum produces a regular time measurement']
opt4=['None of the above','The formation of rocks','Australia','Gangtok, Sikkim','All of the above','Democratic Party','None of the above','Khudada Khan',\
      'Snooker','All of the above']
ans=[1,2,2,2,4,2,2,1,1,4]
ans1=[]

i=0
print('Each question carry 2 marks\nAnswer by entering numbers [1-4]')
while i<10:
    print(chr(65+i),' ',que[i],'\n1->',opt1[i],'\n2->',opt2[i],'\n3->',opt3[i],'\n4->',opt4[i],'\n')
    val=int(input('Your Answer : '))
    ans1.append(val)
    print('\n')
    i+=1

#Calculating Result:
t=i=0
print('--------Results--------')
print('Question No.\tCorrect Ans\tYour Answer\tStatus')
while i<10:
    value=(ans[i]==ans1[i])
    print('Q',i+1,'\t\t',ans[i],'\t\t',ans1[i],'\t\t',value)
    if value:
        t+=1
    i+=1
print('Score : ',t*2)



