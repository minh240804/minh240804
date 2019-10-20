
color=['red','blue','green','teal']

numbers=['1','428','-4','0','1']
n=len(numbers)


#more=input("new coler: ")
#color.append(more)
#print(*color,sep="; ") # list part1


# num=int(input("nhap vi tri: "))# list part 1
# print(color[num])

# while True:                       #list part 2
#     num= len(color)   
#     delete = input("")
#     if delete in color:
#         color.remove(delete)
#         print(*color,sep=", ")
#     else :
#         delete=int(delete)
#         color.pop(delete)
#         print(*color,sep=", ")



# while True:
#     tf = 0
#     num=input()
#     n=len(numbers)
#     for i in range(0,n):
#         if num == numbers[i]:
#             print ("foud",i,sep="\n")
#             tf=1
#             break
#         else:
#             tf=0
#     if tf ==0:
#         print("no number")


# s=0
# num=[]
# for i in range(0,n):
#     ap=int(numbers[i])
#     num.append(ap)
#     s=s+ap
# print (s)

# num=input("")
# num=num.split(" ")
# n=len(num)
# for i in range(0,n):
#     num[i]=int(num[i])

# print (sum(num))


# for i in range(0,n): # part 4
#     numbers[i]=int(numbers[i])
#     if numbers[i]%2==0:
#         print (numbers[i])

# num=input("")
# num=num.split(",")
# n=len(num)
# for i in range(0,n):
#     num[i]=int(num[i])
#     if num[i]%2==0:
#         print(num[i],sep=" ")


# part 6

# quan=['st','bd','btl','cg','dd','hbt']
# s=[11743,9224,4335,1204,996,1009]
# dan =[15300,247100,333300,266800,420900,318000]

# mx=0
# mn=9999999
# vtmx=0
# vtmn=0

# for i in range (0,6):
#     if dan[i] >mx:
#         vtmx=i
#         mx=dan[i]
#     if dan[i] <=mn:
#         vtmn=i
#         mn=dan[i]

# print(" dan so max la: ",quan[vtmx])
# print(" dan so min la: ",quan[vtmn])


# part 7

# quan=['st','bd','btl','cg','dd','hbt']
# s=[11743,9224,4335,1204,996,1009]
# dan =[15300,247100,333300,266800,420900,318000]

# matdo=[]

# for i in range (0,6):
#     ap=dan[i]/s[i]
#     matdo.append(ap)

# tmd=sum(matdo)
# tmd=tmd/6
# print (tmd)


# part 8
hightscore=[2314,67,92,3,8323]
new=int(input("enter new score:"))
hightscore.append(new)
hightscore.sort(reverse=True)
n=len(hightscore)
for i in range(0,5):
    print(i+1,hightscore[i],sep=". ")