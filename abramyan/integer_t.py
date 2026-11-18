T=int(input("T="))
s=T//3600
d=T%3600
f=d//60
r=T%60
print(s,d,f,r)
