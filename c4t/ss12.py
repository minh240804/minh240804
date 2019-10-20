from random import randint

maps=['p','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
x=len(maps)

y=randint(1,x)
while True:
    z=randint(1,x)
    if z==y:
        z=randint(1,x)
    else:
        break

maps[y]='k'
maps[z]='e'

temp=0
vt=0
while True:

    for i in range (0,x):
        print(maps[i],end=' ')
        temp+=1
        if temp==4:
            temp=0
            print("\n")

    text=input("your step: a,s,d,w: ")
    if text =="a":
        maps[vt]='-'
        vt-=1
        maps[vt]='p'
    elif text =="d":
        maps[vt]='-'
        vt+=1
        maps[vt]='p'
    elif text =='s':
        maps[vt]='-'
        vt+=4
        maps[vt]='p'
    elif text=='w':
        maps[vt]='-'
        vt-=4
        maps[vt]='p'





