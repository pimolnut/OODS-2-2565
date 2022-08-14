def odd_even(type,data,mode):
    if type == 'S':
        if mode == 'Odd':
            odd_list = []
            for x in data:
                if x % 2 == 1:
                    odd_list.append(int(x))
                    print(x, end='')
                else:
                    print("no")
        elif check[2] == 'Even':
            print("Even")
    elif type == 'L':
        if mode == ' Even':
            list = []
            data.split()
            print(data)
            for item in data:
                if item % 2 == 1:
                    list.append(int(item))
                    print(item,end='')
                else:
                    print("List")


print("*** Odd Even ***")
check = input("Enter Input : ").split(',')

odd_even(check[0],check[1],check[2])
