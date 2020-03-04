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
    print(defintion, "\n")

    defintion = defintion + "\n"

    final.write(defintion)

for i in range(len(words)):
    final.write(words[i])
    finder(words[i])

file.close()