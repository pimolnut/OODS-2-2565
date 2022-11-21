def StraightSelectionSort(n, k, m, i):
    if n == len(inp) - 1:
        return
    if k == len(inp) - n:
        inp[i], inp[len(inp) - n - 1] = inp[len(inp) - n - 1], inp[i]
        if len(inp) - n - 1 != i:
            print(f'swap {inp[i]} <-> {inp[len(inp) - n - 1]} : {inp}')
        StraightSelectionSort(n+1, 0, -1, -1111111111)
        return
    if inp[k] > m:
        StraightSelectionSort(n, k+1, inp[k], k)
    else:
        StraightSelectionSort(n, k+1, m, i)

inp = list(map(int, input('Enter Input : ').split()))
StraightSelectionSort(0, 0, -1, 0)
print(inp)