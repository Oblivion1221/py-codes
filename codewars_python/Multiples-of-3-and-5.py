def solution(number):
    return sum(list(filter(lambda a: a % 3 == 0 or a % 5 == 0, [i for i in range(number)])))