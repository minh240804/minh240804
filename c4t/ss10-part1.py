# dic={
#     "1A": "a",
#     "2B": "bb",
#     "3C": "ccc",
#     "4D": "4*d"
# }




#new=input("nhap moi")

# dic["3c"] = "ccc"
# dic["3c"] = new
# print(dic,sep=" ; ")

# dic["2b"] = "BB"
# dic["2b"] = new
# print(dic,sep=" ; ")

# del dic["3c"]
# del dic[new]
# print(dic,sep=" ; ")

# print(dic,sep=" ; ")



# x=input("nhap ky tu: ")
# if x in dic:
#     print("true")
# else:
#     print("false")



# x=input("nhap ky tu: ").upper()
# ss=len(dic)
# print(x)
# while True:
#     x=input("nhap ky tu: ").upper()
#     # ss=len(dic)
#     for i in dic:
#         if i ==x:
#             print(x)
#             print(dic[x])
#         else:
#             break

    

bangluong =[
    {
        "name":"huy",
        "role":"waiter",
        "hour":12,
        "luong h":0.8
    },
    {
        "name": "tung",
        "role":"cook",
        "hour":24,
        "luong h":1.5
    },
    {
        "name":"m.duc",
        "role":"manager",
        "hour":20,
        "luong h":2
    }
]

nw1={
    "name":"don",
    "role":"waiter",
    "hour":12,
    "luong h":0.9
}
nw2={
    "name":"h.duc",
    "role":"waiter",
    "hour":14,
    "luong h":0.7
}
bangluong.append(nw1)
bangluong.append(nw2)
ss=len(bangluong)

# for i in range(0,ss):
#     num=0
#     ap=bangluong[i]
#     for j in ap:
#         num +=1
#         if num==3:
#             print(ap[j])

# dictn={
#     "name"="huyen",
#     "role"="waitress",
#     "hour"=14,
    
# }
# ap=bangluong[0]

for i in range(0,ss):
    ap1=0
    num=0
    ap=bangluong[i]
    for j in ap:
        num +=1
        if num==3:
            ap1=ap[j]

