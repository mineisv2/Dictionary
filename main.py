from PyDictionary import PyDictionary

dictionary=PyDictionary()

file = open("Vocabu.txt", "r")
words = file.readlines()

final = open("Vocab.txt", "w")

i = 0

def finder(word):
    global defintion
    defintion = (dictionary.meaning(word))
    try:
        defintion = defintion["Noun"]
    except KeyError:
        defintion = defintion["Verb"]
    defintion = (defintion[0])
    print(defintion)

    final.write(word)
    final.write(defintion)

print(words[1])


for i in len(words):
    finder([words[i]])

file.close()