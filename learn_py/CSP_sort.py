import random


def random_list():
    list1 = [0] * 20
    for i in range(20):
        list1[i] = random.randrange(-30, 30)
    return list1


def bubble_sort_list(list1):
    swapped = 1
    while swapped:
        swapped = 0
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                swapped = 1
    return list1


# def selection_sort_list(list1):
#     for i in range(len(list1)-1):   # [-13, -4, -8, -10, 25, 14, 22, 28, 25, 15, 20, 3, -2, -28, 6, -15, 4, -29, 5, -11]
#         mini = i
#         for j in range(i+1, len(list1)):
#             if list1[j] < list1[mini]:
#                 mini = j
#         list1[i], list1[mini] = list1[mini], list1[i]
#     return list1


def main():
    list1 = random_list()
    print('Random list:\n' + str(list1))
    list2 = bubble_sort_list(list1)
    # list3 = selection_sort_list(list1)
    print('Bubble sort result:\n' + str(list2))
    # print('Selection sort result:\n' + str(list3))

if __name__ == '__main__':
    main()
