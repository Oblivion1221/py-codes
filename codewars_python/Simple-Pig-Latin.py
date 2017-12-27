def pig_it(sentence):
    s1 = sentence.split(' ')
    res = []
    for word in s1:
        res.append(str(word[1:] + word[0] + 'a' + 'y')) if word.isalpha() else res.append(word)
    return ' '.join(res)