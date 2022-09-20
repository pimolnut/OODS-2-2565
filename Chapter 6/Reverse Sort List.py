list_int = []
def mySort(l, m, n):
    if m == n:
        return
    ll = l[m:n + 1]
    maxNum = max(ll)
    # print( f'maxNum = {maxNum}' )
    swap_from = ll.index(maxNum) + m
    swap_to = m
    #   swap
    buff = l[swap_from]
    l[swap_from] = l[swap_to]
    l[swap_to] = buff
    # print( l )
    mySort(l, m + 1, n)


def numList_int(i, n, l):
    if i < n:
        list_int.append(int(l[i]))
        numList_int(i+1, n, l)
#   1,2,3,4,5,6,7,8
#   4,1,3,4,6,9,5,6,7,8
#   0,0,0,0,0
inStr = input('Enter your List : ').split(',')
l = len(inStr)
# numList = [int(str) for str in inStr]
# print(numList)
numList_int(0, l, inStr)
mySort(list_int, 0, len(list_int) - 1)
print(f'List after Sorted : {list_int}')
