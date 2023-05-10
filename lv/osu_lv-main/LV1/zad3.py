import math

numbers = []

while(True):
    try:
        number = input("Unesi broj: ")
        if(number == "Done"):
            break
        else:
            number = float(number)

        numbers.append(number)

    except:
        print("To nije broj.")

print("Broj brojeva:", len(numbers))
print("Prosjek brojeva:", sum(numbers)/len(numbers))
print("Najmanji broj:", min(numbers))
print("Najveći broj:", max(numbers))

numbers.sort()
print("Brojevi:", numbers)
