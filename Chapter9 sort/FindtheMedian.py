def selection_sort(l):
    size = len(l)
    for t in range(size - 1):
        swap = 0
        for i in range(size - t):
            if l[i] > l[swap]:
                swap = i
            if i == size - t - 1 and i != swap:
                temp = l[i]
                l[i] = l[swap]
                l[swap] = temp
    return l


inp = input("Enter Input : ").split()
if inp[0] == 'EX':
    answer = "merge sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + answer)
else:
    data = list(map(int, inp))
    for i in range(len(data)):
        sub_data = data[0:(i + 1)]
        sub_data_sorted = selection_sort(data[0:(i + 1)])
        sub_data_len = len(sub_data)
        print("list = " + str(sub_data), end="")
        if len(sub_data) % 2 == 0:
            median = (sub_data_sorted[int(sub_data_len / 2) - 1] + sub_data_sorted[int(sub_data_len / 2)]) / 2
        else:
            median = sub_data_sorted[int(sub_data_len / 2)]

        print(" : median = %.1f" % median)

