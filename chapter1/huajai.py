print("*** Fun with Drawing ***")
num = int(input("Enter input : "))
w = (num * 4 - 3)
h = w-(num - 1)

l1 = r1 = num
l2 = r2 = num * 3 - 2
for row in range(1, num + 1):
    for col in range(1, w + 1):
        if col == l1 or col == r1 or col == l2 or col == r2:
            print('*',end='')
        elif col > l1 and col < r1:
            print('+',end='')
        elif col > l2 and col < r2:
            print("+",end='')
        else:
            print('.',end='')
    l1 -= 1
    l2 -= 1
    r1 += 1
    r2 += 1
    print()

l1 = 2
l2 = w - 1
for row in range(w // 2):
    for col in range( 1 , w + 1):
        if col == l1 or col == l2:
            print('*', end='')
        elif col > l1 and col < l2:
            print("+", end='')
        else:
            print(".", end='')
    l1 += 1
    l2 -= 1
    print()


