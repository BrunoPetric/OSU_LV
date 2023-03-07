spam = 0
spam_words = 0
ham = 0 
ham_words = 0
ex_counter = 0
fhand = open ('SMSSpamCollection.txt')
for line in fhand:
    line = line.rstrip ()
    words = line.split ()
    if( line.startswith ('spam')):
        spam += 1
        spam_words += len(words)
        if(line[-1] == '!'):
            ex_counter += 1

    elif(line.startswith ('ham')):
        ham += 1
        ham_words += len(words)

print('Prosijek spam poruka: ', spam_words/spam)
print('Prosijek ham poruka: ',ham_words/ham)
print('Broj spam poruku koje zavrsavaju usklicnikom je: ', ex_counter)