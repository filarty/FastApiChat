def anagrams(word, words):
    array = []
    for i in words:
        result = ""
        for j in i:
            if j not in word:
                    break
            if word.count(j) == i.count(j):
                result += j
        if len(result) == len(word):
            array.append(result)
        result = ""
    return array




word = 'racer'
word_list = ['crazer', 'carer', 'racar', 'caers', 'racer']
a = anagrams(word, word_list)
print(a)