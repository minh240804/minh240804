from random import randint

nv={
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2
}

skills=[
    {
        "Name": "Tackle",
        "Minimum level": 1,
        "Damage": 5,
        "Hit rate": 0.3
    },
    {
        "Name": "Quick attack",
        "Minimum level": 2,
        "Damage": 3,
        "Hit rate": 0.5
    },
    {
        "Name": "Strong Kick",
        "Minimum level": 4,
        "Damage": 9,
        "Hit rate": 0.2
    }
]



# x=input("nhap key: ")
# y=input("nhap value:")
# dic[x]=y

# stt= len(dic)
# z=randint(0,stt)

# for i in range(0,z):
#     ap1=0
#     num=0
#     ap=bangluong[i]
#     for j in ap:




# point=0
# while True:
#     liss = {
#         "Q"     :["1+1","100.10"],
#         "true"  :[1,100.1],
#         "false1":[2,1000],
#         "false2":[3,100]
#     }

#     ap=liss["Q"]
#     as1=liss["true"]
#     as2=liss["false1"]
#     as3=liss["false2"]
#     x=len(ap)
#     y=randint(0,x-1)
#     print(ap[y])
#     print(as1[y])
#     print(as2[y])
#     print(as3[y])

#     asp=int(input("nhap tt: "))

#     intast=int(as1[y])

#     if asp==intast:
#         print("corect")
#         point=point+1
#     else:
#         print("false")
#         print(point)
#         break



# key=input("")
# print(dic[key])

# dicn["d"]=4

# sum=0
# for i in dicn:
#     ap=dicn[i]
#     sum+=ap
    
# print(sum)

# hangmay=input("nhao hang: ")
# ap=int(dicn[hangmay])
# gia=ap*sm
# print(gia)

# x=input("")
# x=x.split(":")
# hangmay=x[0]
# sm=int(x[1])
# ap=int(dicn[hangmay])
# gia=ap*sm
# print(gia)


# smsm=0
# for i in dicn:
#     temp1=int(dicn[i])
#     temp2=int(dicp[i])
#     sumg=temp1*temp2
# #   print(sumg)
#     smsm+=sumg
# print(smsm)



temp=nv["Gold"]
nv["Gold"]:temp+50
# print(nv)
temp=nv["Backpack"]
temp.append("FlintStone")
nv["Backpack"]=temp
# print(nv)
temp=["MonsterDex","Flashlight"]
nv["Pocket"]=temp
# print(nv)

z=len(skills)
sk1=skills[1]
sk2=skills[2]
sk3=skills[3]
temp=nv["Level"]

for i in range(0,z):
    temp=skills[i]
    print(i+1,end=" ")
    print(temp["Name"])

a=int(input("nhap skill: "))
if a==1:
    sk1[""]


