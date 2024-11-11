start=input("Enter a first number: ")
end=input("Enter a second number: ")
start=int(start)
end=int(end)

for i in range(start,end+1):
    swap=0
    x=0
    original=i
    while original > 0:
        x=original%10
        original=int(original/10)
        swap=swap*10+x
    if i==swap:
        print(i)