file = open("Vocabu.txt", "r")
words = file.readlines()

print(words[0])

for i in range(len(words)):
    print("cows are cool")


file.close()