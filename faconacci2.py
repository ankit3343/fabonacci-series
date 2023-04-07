num=int(input("Enter a number:"))
a=0
b=1
c=a+b
print(a)
print(b)
for i in range(0,num):
    print(c)
    a=b
    b=c
    c=a+b