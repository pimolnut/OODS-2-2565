def bubble_sort(L1):
    if len(L1) <= 1:
        return L1
    if len(L1) == 2:
        if L1[0] < L1[1]:
            return L1
        else:
            return [L1[1], L1[0]]
    a = L1[0]
    b = L1[1]
    bs = L1[2:]
    new1 = []
    if a < b:
        new1 = [a] + bubble_sort([b] + bs)
    else:
        new1 = [b] + bubble_sort([a] + bs)
    return bubble_sort(new1[:-1]) + new1[-1:]


inp = [int(x) for x in input('Enter Input : ').split()]
x = bubble_sort(inp)
print(x)