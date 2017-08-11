# 1st element as pivot
def partition(A, l, r):
    p = A[l]
    i = l + 1
    for j in range(l + 1, r):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1


def qs(A, l, r):
    global tot_comp
    if l < r:
        t = partition(A, l, r)
        tot_comp += r - l - 1
        qs(A, l, t)
        qs(A, t + 1, r)
        return tot_comp

if __name__ == '__main__':
    tot_comp = 0

    with open('/Users/yangyaoxian/Downloads/QuickSort.txt') as f:
        A = f.read().splitlines()
    for i in range(len(A)):
        A[i] = int(A[i])
    res1 = qs(A, 0, len(A))
    print(res1)

    test = [3, 9, 8, 4, 6, 10, 2, 5, 7, 1]
    print(test)
    res2 = qs(test, 0, len(test))
    print(test)
    print(res2 - res1)
