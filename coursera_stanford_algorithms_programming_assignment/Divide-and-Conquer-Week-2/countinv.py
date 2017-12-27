def sort_and_count(A):
    if len(A) <= 1:
        return A, 0
    else:
        B, x = sort_and_count(A[:int(len(A) / 2)])
        C, y = sort_and_count(A[int(len(A) / 2):])
        D, z = merge_and_countsplitinv(B, C)
        return D, x + y + z


def merge_and_countsplitinv(B, C):
    i, j, tot = 0, 0, 0
    D = []
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            D.append(B[i])
            i += 1
        elif B[i] > C[j]:
            D.append(C[j])
            j += 1
            tot += len(B) - i
    D += B[i:]
    D += C[j:]
    return D, tot


if __name__ == '__main__':

    with open('/Users/yangyaoxian/Downloads/IntegerArray.txt') as f:
        A = f.read().splitlines()
    for i in range(len(A)):
        A[i] = int(A[i])
    print(sort_and_count(A))

