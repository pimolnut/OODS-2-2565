def staircase(s, e):
    if s > 0:
        if e > s:
            pass
        else:
            line1 = "_" * (s - e)
            charp1 = "#" * e
            print(line1 + charp1)
            return staircase(s, e+1)
    elif s < 0:
        if e > -s:
            pass
        else:
            line1 = "_" * (e - 1)
            charp1 = "#" * ((-s)-(e-1))
            print(line1 + charp1)
            return staircase(s, e + 1)
    elif s == 0:
        print("Not Draw!")


staircase(int(input("Enter Input : ")), 1)
