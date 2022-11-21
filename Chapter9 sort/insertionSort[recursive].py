def findPlace(lis, value, index=0):
    if index == len(lis):
        return index
    if lis[index] >= value:
        return index
    return findPlace(lis, value, index+1)


def insertionSort(st, lis, index=0):
    if len(lis) == 0:
        return st
    placeIndex = findPlace(st,lis[index])
    if placeIndex == -1:
        temp = []
        temp.append(lis[index])
        st = temp+st
        num=lis.pop(0)
        print('insert {0} at index {1} : '.format(num,0)+str(st),end='')
        if len(lis)!=0:
            print(' '+str(lis))
        else:
            print('')
    elif placeIndex == len(st):
        st.append(lis[index])
        num=lis.pop(0)
        print('insert {0} at index {1} : '.format(num,len(st)-1)+str(st),end='')
        if len(lis)!=0:
            print(' '+str(lis))
        else:
            print('')
    else:
        temp1=st[:placeIndex]
        temp2=st[placeIndex:]
        temp3=[]
        temp3.append(lis[index])
        st=temp1+temp3+temp2
        num=lis.pop(0)
        print('insert {0} at index {1} : '.format(num,placeIndex)+str(st),end='')
        if len(lis)!=0:
            print(' '+str(lis))
        else:
            print('')
    return insertionSort(st, lis)


inp = [int(e) for e in input('Enter Input : ').split()]
lis1 = inp[0:1]
lis2 = inp[1:]
sorted_list = insertionSort(lis1, lis2)

print('sorted')
print(sorted_list)