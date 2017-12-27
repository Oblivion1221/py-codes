def tickets(people):
    tmp = []
    for i in range(len(people)):
        if people[i] == 25:
            tmp.append(people[i])
        elif people[i] == 50:
            if not 25 in tmp:
                return "NO"
            else:
                tmp.remove(25)
                tmp.append(people[i])
        elif people[i] == 100:
            if 25 in tmp and 50 in tmp:
                tmp.remove(25)
                tmp.remove(50)
                tmp.append(people[i])
            elif tmp.count(25) == 3:
                tmp = list(filter(lambda a: a != 25, tmp))
                tmp.append(people[i])
            else:
                return "NO"
    return "YES"