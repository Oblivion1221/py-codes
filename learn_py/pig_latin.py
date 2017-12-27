from __future__ import print_function

def consonant(c):
    v = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
    if c not in v:
        return True
    else:
        return False
        
def pig_latin_1(word):
    if consonant(word[0]):
        word1 = word[1:] + word[0] + 'a' + 'y'
        return str(word1)
    else:
        return word + 'way'
    
def pig_latin(word):
    if consonant(word[0]) and not consonant(word[1]):
        return pig_latin_1(word)
    elif consonant(word[0]) and consonant(word[1]):
        word = word[2:] + word[0:2] + 'a' + 'y'
        return word
    else:
        return word + 'way'
    
def pig_latin_sentence(sentence):
    s1 = sentence.split(' ')
    res = []
    for word in s1:
        res.append(pig_latin(word))
    return ' '.join(res)
    
def test_pig_latin():
    words = ['pig', 'banana', 'trash', 'happy', 'duck', 'glove', 'eat', 'omelet', 'are']
    for word in words:
        print(word, "->", pig_latin(word))
    
test_pig_latin()

print( pig_latin_sentence("I am talking in pig Latin"))