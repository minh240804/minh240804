
#s =['br','spc','coc']

#                       append
# s=['l', 'o' , 'l']
# m=input()
# s.append(m)

#                       read & index

# s =['l', 'o', 'l']

# more=input()
# s.append(more)
# for i in range(0,4):
#     s[i]=s[i].upper()
#     print(s[i],sep='\n')

#                      update
# s =['br','spc','coc']

# new=input("nhap thay doi: ")
# index=int(input("nhap vi tri: "))
# s[0]=new
# s[-1]=new
# s[index]=new
# print(s,sep='\n')

#                     delete


# index=int(input("nhap vi tri: ")
# s.pop(index)

# gt=input("nhap vao gia tri loai bo: ")

# if gt in s:
#     s.remove(gt)
# print(s)


#                    for and list

#new=str(input("nhap them 3 phan tu: "))
# more=new.split(',')

# for i in range (0,3):
#     new=input('nhap them ky tu moi: ')
#     s.append(new)

# nindex=len(s)

# for j in range (0,nindex):
#     # s[j]=s[j].upper()
#     # print(j+1,s[j],'\n')
#     ap=list(s[j])
#     ap2=len(ap)
#     for k in range (0,ap2):
#         if 'e' in ap or 'E' in ap:
#             print(s[j])

#                         CRUD SUMARY

# n=[]
# while True:
#     ap=0
#     text=input("nhap c,r,u,d,b:")
#     if text=='c':
#         new=input("nhap so thich cua ban: ")
#         n.append(new)
#     elif text == 'r':
#         ap=int(len(n))
#         if ap==0:
#             print("danh sach rong")
#         else:
#             for i in range(0,ap):
#                 print(n[i],sep='\n')
#     elif text == 'u':
#         ap=int(input("nhap vi ti muon thay doi: "))
#         n[ap]=input("nhap vao thay doi: ")
#     elif text =='d':
#         ap=int(input('nhap vi tri ban muon xoa: '))
#         n.pop(ap)
#     elif text=='b':
#         break

#              one input list

# inp=input("nhap ten voi dau (,)")
# n=inp.split(',')
# print(*n,sep='\n')

#             shuflle word             ,          word jumper
import random
from random import randint
while True:

    words = ['good','bad','new']
    num= randint(0,2)
    word= words[num]
    check= words[num]
    
    shuffled = list(word)
    random.shuffle(shuffled)
    shuffled = ''.join(shuffled)
    print (shuffled)

    res=input("nhap tu dung: ")
    if check!=res :
        print("fail")
        break
