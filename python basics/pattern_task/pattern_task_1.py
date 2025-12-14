n= int(input("enter the number of rows: "))
m=(n+1)*n//2

start=m
for i in range(n):
    current=start 
    for j in range(i+1):
        print(format(current, "<3"), end="  ") 
        current+=1
    print()

    start=start-(i+2)