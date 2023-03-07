while True:
    try:     
        ocjena = float(input())
        break
    except ValueError:
        print("Nije broj")


if(ocjena > 1.0):
    print('pogresan unos')
elif(ocjena >= 0.9):
    print('A')
elif(ocjena >= 0.8):
    print('B')
elif(ocjena >= 0.7):
    print('C')
elif(ocjena >= 0.6):
    print('D')
elif(ocjena >= 0):
    print('F')