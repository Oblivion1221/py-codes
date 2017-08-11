# Consider 1st, middle, and final elements of the array
def median(A, l, r):
    print('l =', l, 'r =', r)

    mp = int((l + r - 1) / 2)

    # A1 = [A[l], A[mp], A[r - 1]]
    if (A[l] - A[mp]) * (A[r-1] - A[l]) >= 0:
        A[l], A[l] = A[l], A[l]
    elif (A[mp] - A[l]) * (A[r-1] - A[mp]) >= 0:
        A[mp], A[l] = A[l], A[mp]
    else:
        A[r-1], A[l] = A[l], A[r-1]
    # print("The median3 array is:", A1)

    # print("swap the pivot to 1st element of the rest of the array:\n", A[mp], "and", A[l])
    # print(A)
    return A[l]


def partition(A, l, r):
    p = median(A, l, r)
    print("pivot:", p)
    i = l + 1
    for j in range(l + 1, r):
        if A[j] < p:
            print("swap:", A[j], "and", A[i])
            A[j], A[i] = A[i], A[j]
            i += 1
    print("swap:", A[l], "and", A[i - 1])
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1


def qs(A, l, r):
    global tot_comp
    if l < r:
        print("Sort:", A)
        t = partition(A, l, r)
        tot_comp += r - l - 1
        print("tot_comp:", tot_comp, '\n')
        qs(A, l, t)
        qs(A, t + 1, r)
        return tot_comp

if __name__ == '__main__':
    tot_comp = 0

    with open('/Users/yangyaoxian/Desktop/pythoncodes/pycodes/Coursera-Stanford-Algorithms-Programming-Assignment/Divide-and-Conquer-Week-3/QuickSortInPython/QuickSort.txt') as f:
        A = f.read().splitlines()
        f.close()
    for i in range(len(A)):
        A[i] = int(A[i])
    # with open('/Users/yangyaoxian/Downloads/QsTest.txt') as f:    #8921
    #     A = f.read().splitlines()
    #     f.close()
    # for i in range(len(A)):
    #     A[i] = int(A[i])
    res1 = qs(A, 0, len(A))
    print('total:', res1, '\n')

    test = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
    res2 = qs(test, 0, len(test))
    print(test)
    print(res2 - res1)    # 21

"""
debug:

Sort: [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
l = 0 r = 10
pivot: 3
swap: 2 and 9
swap: 1 and 8
swap: 3 and 1
tot_comp: 9

Sort: [1, 2, 3, 4, 6, 10, 9, 5, 7, 8]
l = 0 r = 2
pivot: 1
swap: 1 and 1
tot_comp: 10

Sort: [1, 2, 3, 4, 6, 10, 9, 5, 7, 8]
l = 1 r = 2
pivot: 2
swap: 2 and 2
tot_comp: 10

Sort: [1, 2, 3, 4, 6, 10, 9, 5, 7, 8]
l = 3 r = 10
pivot: 8
swap: 6 and 6
swap: 5 and 10
swap: 7 and 9
swap: 4 and 10
swap: 8 and 4
tot_comp: 16

Sort: [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]
l = 3 r = 7
pivot: 6
swap: 4 and 4
swap: 5 and 5
swap: 6 and 5
tot_comp: 19

Sort: [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
l = 3 r = 5
pivot: 5
swap: 4 and 4
swap: 5 and 4
tot_comp: 20

Sort: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 3 r = 4
pivot: 4
swap: 4 and 4
tot_comp: 20

Sort: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 6 r = 7
pivot: 7
swap: 7 and 7
tot_comp: 20

Sort: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 8 r = 10
pivot: 9
swap: 9 and 9
tot_comp: 21

Sort: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 9 r = 10
pivot: 10
swap: 10 and 10
tot_comp: 21

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
21

Process finished with exit code 0
"""
