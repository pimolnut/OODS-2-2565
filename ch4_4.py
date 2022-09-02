class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

Act = { 0: "Eat",
          1: "Game",
          2: "Learn",
          3: "Movie"}

location = {0: "Res.",
           1: "ClassR.",
           2: "SuperM.",
           3: "Home"}

inp = input("Enter Input : ").split(",")
my_q = Queue()
your_q = Queue()
my_act = Queue()
my_loca = Queue()
your_act = Queue()
your_loca = Queue()

count = 0
count1 = 0
count2 = 0
count3 = 0

comma = ""
for i in range(len(inp)):
    x = inp[i].split(" ")
    my_q.enqueue(x[0])
    your_q.enqueue(x[1])

    myact = Act[int(my_q.items[i][0])]
    my_act.enqueue(myact)
    mylocation = location[int(my_q.items[i][2])]
    my_loca.enqueue(mylocation)
    youract = Act[int(your_q.items[i][0])]
    your_act.enqueue(youract)
    yourlocation = location[int(your_q.items[i][2])]
    your_loca.enqueue(yourlocation)

    if myact == youract and mylocation != yourlocation:
        count = count+1
    elif mylocation == yourlocation and myact != youract:
        count1 = count1+2
    elif myact == youract and mylocation == yourlocation:
        count2 = count2+4
    elif myact != youract and mylocation != yourlocation:
        count3 = count3-5
    num = count+count1+count2+count3

print('My   Queue = %s'%', '.join(map(str,my_q.items)))
print('Your Queue = %s'%', '.join(map(str,your_q.items)))
print(f'My   Activity:Location = ',end="")
for i in range(my_act.size()):
    if i != my_act.size()-1:
        print(f"{my_act.items[i]}:{my_loca.items[i]}",end=", ")
    else:
        print(f"{my_act.items[i]}:{my_loca.items[i]} ")
print(f'Your Activity:Location = ',end="")
for j in range(your_act.size()):
    if j != your_act.size()-1:
        print(f'{your_act.items[j]}:{your_loca.items[j]}',end=", ")
    else:
        print(f'{your_act.items[j]}:{your_loca.items[j]} ')
if num >= 7:
    print(f"Yes! You're my love! : Score is {num}.")
elif 0 < num < 7:
    print(f"Umm.. It's complicated relationship! : Score is {num}.")
elif num < 0 :
    print(f"No! We're just friends. : Score is {num}.")





# print(num)
    # print(f'{myact}:{mylocation},{youract}:{yourlocation}')
    # print()
# print(f"my act : {my_act}")
# print(f"your act : {your_act}")
# print()
# print(f"my location ; {my_loca}")
# print(f"you location : {your_loca}")
# print()


# print(f'Your Activity:Location = ')



