def generator(n):
    for i in range(n):
        if i%2==0:
            yield i
n=int (input("Enter a number:\n"))
lst=[]
for i in generator(n):
    lst.append(i)
print(*lst,sep=",")
