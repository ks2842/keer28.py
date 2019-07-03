p=input()
k=[]
for i in p:
    if i.isdigit():
        p.append(str(i))
print("".join(k))
