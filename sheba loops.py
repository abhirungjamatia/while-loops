i=65
while i<=69:
    b=65
    while b<=69-i:
        print("  ",end=" ")
        b=b+1
    j=65
    while j<=i:
        print(chr(i),end=" ")
        j=j+1
    print( )
    i=i+1