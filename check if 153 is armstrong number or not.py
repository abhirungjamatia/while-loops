a=input("enter number")
i=0
z=0
while i<len(a):
    c=a[i]
    z=c+z**3
    i=i+1
if z==int(a):
    print("armstrong")
else:
    print("not armstrong")
