#                                           full name
# ho = input("nhap ho cua ban: ")
# tend =input("nhap ten dem cua ban: ")
# ten = input("nhap ten cua ban: ")

# print (ho,tend,ten )

#                                           capitalize name
# ten = input("nhap ten:  ").upper()

# print(ten)

#                                           square number

# x=int(input("nhap so: "))
# print(x*x)

#                                           turtle with CUSTOM radius
# from turtle import *
# bankinh=int(input("nhap ban kinh: "))

# circle(bankinh)

# mainloop()

#                                           3 to 12 sequance
# for i in range(3,13):
#     print(i)

#                                           0 to n  sequance
# n=int(input("nhap so cua ban: "))
# n=n+1
# for i in range (0,n):
#     print(i)

#                                           0 to n odd sequance
# n=int(input("nhap so cua ban: "))
# n=n+1
# for i in range (0,n):
#     if i%2 !=0:
#         print(i)

#                                           polythoon  with custum edge number

# from turtle import *

# canh=int(input("nhap so canh: "))
# goc=(canh-2)*(180/canh)
# if  canh<=2:
#     forward(100)
# else:

#     for i in range(1,canh+1):
#         print(goc)
#         left(180-goc)
#         forward(100)


# mainloop()

#                               langer than 13
# a=int(input())
# if a<=13:
#     print("true")
# else:
#     print("false")

#                               even check

# a=int(input())
# if a%2==0:
#     print(so chan)
# else:
#     print(so le)

#                               day or month       
# a=int(input)
# if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
#     print(31)           
# elif a==4 or a==6 or a==9 or a==11:
#     print(30)
# elif a==2:
#     print("28 or 29")
# else:
#     print ("false vaulue")

#                               resgsittration
# name=input("nhap ten dang nhap: ")
# password=input("nhap mat khau: ")
# while True:
#     password2=input("nhap lai mat khau: ")
#     if password == password2:
#         break
#     else:
#         print("vui long")

# while True:
#     email=input("nhap email")
#     if "@" in email and "." in email and len(email) =>8:
#         break


#                               freaking number
from random import randint
score=0
while True:

    num1 =randint(0,20)
    num2 =randint(0,20)
    false_result= randint(-3,3)
    sum = false_result + num1 + num2 
    print("{} + {} ={}".format(num1,num2,sum))

    kq = input("F or T ?")

    if false_result ==0:
        if kq == "t":
            print("correct")
            score+=1
            print(score)
        else:
            print("lose")
            break
    else:
        if kq == "f":
            print("correct")
            score+=1
            print(score)
        else:
            print("lose")
            break
            


