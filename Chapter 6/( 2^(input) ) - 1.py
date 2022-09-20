def Binary(num, count):
    if len(bin(num).replace("0b", "")) < count:
        s = count - len(bin(num).replace("0b", ""))
        return ("0"*s) + str(bin(num).replace("0b", ""))
    else:
        return bin(num).replace("0b", "")


def printBinary(n, i=0):
    t = (2**n) - 1
    if i <= t:
        print(Binary(i, n))
        printBinary(n, i+1)


inp = int(input('Enter Number : '))
# print(bin(inp))
if inp >= 0:
    printBinary(inp)
else:
    print('Only Positive & Zero Number ! ! !')