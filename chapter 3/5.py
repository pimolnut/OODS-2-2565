class Stack:
    def __init__(self):
        self.items = []

    def push(self,i):
        self.items.append(i)

    def pop(self,i):
        return self.items.pop(i)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
S = Stack()
new = []
count = 0
for point in range(len(s)):
    if s[point] == ',':
        pass
    elif s[point] == '0':
        pass
    else:
        S.push(s[point])

if 'arrive' == o:
    if m == len(S.items) and str(n) not in S.items:
        print(f"car {n} cannot arrive : Soi full")
        print('[%s] '%', '.join(map(str,S.items)))
    elif m > len(S.items) and str(n) not in S.items:
        S.push(n)
        print(f"car {n} arrive! : Add Car {n}")
        print('[%s] '%', '.join(map(str,S.items)))
    elif str(n) in S.items:
        print(f"car {n} already in soi")
        print('[%s] '%', '.join(map(str,S.items)))
elif 'depart' == o:
    if str(n) in S.items:
        S.pop(0)
        print(f"car {n} depart ! : Car {n} was remove")
        print('[%s] '%', '.join(map(str,S.items)))
    elif str(n) not in S.items:
        if S.size() == 0:
            print(f"car {n} connot depart : Soi Empty ")
            print("[]")
        else:
            print(f"car {n} cannot depart : Don't Have Car {n}")
            print('[%s] ' % ', '.join(map(str, S.items)))





