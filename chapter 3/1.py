def Create():
    stack = []
    return stack

def push(stack,item):
    stack.append(item)
    print(f"Add = {item} and Size = {len(stack)}")

def pop(stack):
    if len(stack) == 0:
        print("-1")
    else:
        return print(f"Pop = {stack.pop()} and Index = {len(stack)}")

def Valueindex(stack):
    for x in stack:
        print(x,end=" ")

num = input("Enter Input : ").split(",")
s = Create()
for x in range(len(num)):
    if len(num[x]) == 4:
        if 'A' in num[x]:
            push(s, str(num[x][-2]+num[x][-1]))
    else:
        if 'P' in num[x]:
            pop(s)

if len(s) != 0:
    print("Value in Stack = ", end="")
    Valueindex(s)
else:
    print("Value in Stack = Empty")


