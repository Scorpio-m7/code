c=[]
with open("1.txt", "r") as f:
    c+= f.read()
f=''
o=''
for s in c:
    if ord(s)<=90 and ord(s)>=65:
        f+=s
        if ord(s)==90:
            o+='0'
        if ord(s)==78:
            o+='1'
print(f)
print(o)
