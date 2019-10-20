#ss6
# while validate input: ex2,3
# while True:
#     num = input("enter your password: ")
#     if num.isalpha or len(num)<=8: #.isalpha kiem tra str toan chu; len() kiem tra do dai str
#         print ("false")
#     else:
#         print ("true")
#         break

# isvalid=False
# while True:
#     s=input(" enter password")
#     for i in range(0,10):
#         if str(i) in s:
#             isvalid=True
#     if isvalid:


# while digit count ex1   
# dem = 0
# s= int(input("nhap so cua ban: "))
# while s != 0:
#         s //= 10 #= s=s//10
#         dem +=1
# print (dem)

# while alarm clock

import pyglet
import datetime

music = pyglet.resource.media('sample.wav')

time = datetime.datetime.now()
n=0
while True:
    time = datetime.datetime.now()
    if time.hour == 14 and time.minute == 9 :
        music.play()
    if time.hour == 14 and time.minute == 9 and time.second == 20:
        break




pyglet.app.run()
