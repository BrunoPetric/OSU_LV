file = open("C://Users//student//Desktop//OSU//LV1//SMSSpamCollection.txt", "r")
spamLines = 0
hamLines = 0
spamSum = 0
hamSum = 0
spamAvg = 0
hamAvg = 0
spamExclamation = 0

for line in file:
    line = line.rstrip()

    if(line.startswith("spam")):
        spamLines += 1
        if(line.endswith("!")):
            spamExclamation += 1
        spamSum += len(line.split()) - 1
    elif(line.startswith("ham")):
        hamLines += 1
        hamSum += len(line.split()) - 1

print("Spam average: ", spamSum/spamLines)
print("Ham average: ", hamSum/hamLines)

print("Exclamations at the end:", spamExclamation)
