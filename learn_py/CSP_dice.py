import random

side = int(input('Enter the number of sides:'))
dice = int(input('Enter the number of dices:'))
hist = [0] * side * dice


def roll(times, dice):
    for i in range(times):
        res = 0
        for j in range(dice):
            res += random.randrange(1, side)
        hist[res] += 1


def mean(arr):
    tot1 = tot2 = 0
    for i in range(len(arr)):
        tot1 += arr[i] * i
        tot2 += arr[i]
    res = tot1 / tot2
    return res

if __name__ == '__main__':
    t = int(input('Enter the number of execution times:'))
    roll(t, dice)
    print(hist)
    for i in range(len(hist)):
        print('*' * hist[i])
    print(mean(hist))
