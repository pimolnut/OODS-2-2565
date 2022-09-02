class Queue:
    def __init__(self,inp = None):
        if inp == None:
            self.items = []
        else:
            self.items = inp
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[0]


def encodemsg(q1,q2):
    k = 0
    for x in range(q1.size()):
        num1 = ord(q1.items[0]) + int(q2.items[k])
        if q1.items[0].islower():
            if chr(num1) <= 'z':
                q1.enqueue(chr(num1))
                q1.dequeue()
            else:
                q1.enqueue(chr(num1-26))
                q1.dequeue()
        elif q1.items[0].isupper():
            if chr(num1) <= 'Z':
                q1.enqueue(chr(num1))
                q1.dequeue()
            else:
                q1.enqueue(chr(num1-26))
                q1.dequeue()
        k += 1
        if k == q2.size():
            k = 0

    return print(f"Encode message is :  {q1.items}")


def decodemsg(q1,q2):
    k = 0
    for x in range(q1.size()):
        num1 = ord(q1.items[0]) - int(q2.items[k])
        if q1.items[0].islower():
            if chr(num1) >= 'a':
                q1.enqueue(chr(num1))
                q1.dequeue()
            else:
                q1.enqueue(chr(num1 + 26))
                q1.dequeue()
        elif q1.items[0].isupper():
            if chr(num1) >= 'A':
                q1.enqueue(chr(num1))
                q1.dequeue()
            else:
                q1.enqueue(chr(num1 + 26))
                q1.dequeue()
        k += 1
        if k == q2.size():
            k = 0

    return print(f"Decode message is :  {q1.items}")


string,number = input("Enter String and Code : ").split(",")
string = string.replace(" ", "")
string = [i for i in string]
number = [i for i in number]
q1 = Queue(string)
q2 = Queue(number)
# print(q1.items)
# print(q2.items)
encodemsg(q1,q2)
decodemsg(q1,q2)

# c = 'h'
# t = 'z'
# x = ord(c)
# y = chr(x)
# k = chr((ord(t)+2)-26)
# print(x,y,k)
#
