from random import randint

x1=randint(1,3)
y1=randint(1,3)
x2=randint(1,3)
y2=randint(1,3)
x3=randint(1,3)
y3=randint(1,3)

while True:
    if y3!=y2 :
        break
    else:
        y3=randint(1,3)
while True:
    if x3!=x2 :
        break
    else:
        x3=randint(1,3)
while True:
    if x1!=x2 and x2!=x3:
        break
    else:
        x2=randint(1,3)
while True:
    if y1!=y2 and y2!=y3:
        break
    else:
        y2=randint(1,3)


player={# khai bao
    'x':0,
    'y':0
}
exits={
    'x':x1,
    'y':y1
}
key={
    'x':x2,
    'y':y2
}
vatcan={
    'x':0,
    'y':2
}

picked=bool(False)


while True:
    for i in range(0,4):#in ra ban do
        for j in range(0,4):
            if i==player['y'] and j==player['x']:#in ra p
                print("p",end=" ")
            elif i==key['y'] and j==key['x']:#in ra key
                if picked==True:
                    print('-',end=" ")
                else:
                    print('k',end=' ')
            elif i==exits['y'] and j==exits['x']:#in ra exit
                print("e",end=" ")
            elif i==vatcan['y'] and j==vatcan['x']:#in ra exit
                print("w",end=" ")
            else:
                print("-",end=" ")
        
        print("\n")

    text=input("your steps: ")#di chuyen
    if text=='a':
        player['x']=player['x']-1
    elif text =='d':
        player['x']=player['x']+1
    elif text=='s':
        player['y']=player['y']+1
    elif text=='w':
        player['y']=player['y']-1
    if text=='b':
        break
   
   
    if player['x']==key['x'] and player['y']==key['y']:#kiem tra chia khoa
        picked=True
        print("you have picked the key")
    
    
    if player['x']==exits['x'] and player['y']==exits['y']:#kiem tra loi ra
        if picked==True:
            print("you win")
            break
        else:
            print("you don't have the key")
            if text=='a':
                player['x']=player['x']+1
            elif text =='d':
                player['x']=player['x']-1
            elif text=='s':
                player['y']=player['y']-1
            elif text=='w':
                player['y']=player['y']+1

    if 3<player['x'] or player['x']<0 or 3<player['y'] or player['y']<0:#kiem tra 
        print("over the wall")
        if text=='a':
                player['x']=player['x']+1
        elif text =='d':
                player['x']=player['x']-1
        elif text=='s':
                player['y']=player['y']-1
        elif text=='w':
                player['y']=player['y']+1
    
        if player['x']==vatcan['x'] or player['y']==vatcan['y']:#kiem tra vat can
            print("can,t move ")
            if text=='a':
                    player['x']=player['x']+1
            elif text =='d':
                    player['x']=player['x']-1
            elif text=='s':
                    player['y']=player['y']-1
            elif text=='w':
                    player['y']=player['y']+1