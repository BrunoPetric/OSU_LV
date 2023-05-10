messages = []
ham_count = 0
spam_count = 0
ham_words = 0
spam_words = 0
ex_count = 0
text = open('LV1\SMSSpamCollection.txt')
for line in text:
    line = line.rstrip()
    words = line.split()
    if words[0] == 'ham':
        ham_count += 1
        ham_words += len(words[1:])
    else:
        if line.endswith("!"):
            ex_count += 1
        spam_count += 1
        spam_words += len(words[1:])  
print(f'Average number of words in ham messages: {ham_words/ham_count}')
print(f'Average number of words in spam messages: {spam_words/spam_count}')
print(f'Number of spam messages that end with "!": {ex_count}')