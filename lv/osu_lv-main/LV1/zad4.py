file = open("C://Users//student//Desktop//OSU//LV1//song.txt", "r")

dictionary = {}

for line in file:
    line = line.rstrip()
    words = line.split()

    for word in words:
        if(dictionary.__contains__(word)):
            dictionary[word] += 1
        else:
            dictionary[word] = 1

file.close()

for key, value in dictionary.items():
    if(value == 1):
        print(key)
