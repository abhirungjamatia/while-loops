num=int(input("enter number"))
rev=0
c=num
while c>=0:
    a=c%10
    rev=rev*10+a
    c=c//10
print(rev)
if num==rev:
    print("palindrome number")
else:
    print("not a palindrome number")