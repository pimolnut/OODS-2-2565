def odd_even(type,data,mode):
    if type == 'S':
        if mode == 'Odd':
            for x in range(len(data)):
                if x % 2 == 0:
                    print(data[x],end='')
        elif mode == 'Even':
            for i in range(len(data)):
                if i % 2 == 1:
                    print(data[i],end='')
    elif type == 'L':
        data = data.split()
        list_data = []
        if mode == 'Odd':
            for y in range(len(data)):
                if y % 2 == 0:
                    list_data.append(data[y])
        elif mode == 'Even':
            for item in range(len(data)):
                if item % 2 == 1:
                    list_data.append(data[item])

        print(list_data)

print("*** Odd Even ***")
check = input("Enter Input : ").split(',')
odd_even(check[0],check[1],check[2])
