rijeci = {}
counter = 0     
fhand = open ('song.txt')
for line in fhand:
    line = line.rstrip ()
    print ( line )
    words = line.split ()

    for word in words:
        if word in rijeci:
            rijeci[word] += 1
        else:
            rijeci[word] = 1

fhand.close ()

for words in rijeci:
    if(rijeci[words] == 1):
        print(words)
        counter += 1

print(counter)