while(True):
    try:
        number = float(input("Unesi broj između 0.0 i 1.0: "))

        while(number > 1.0 or number < 0.0):
            print("Broj nije u intervalu.")
            number = float(input("Unesi broj između 0.0 i 1.0: "))

        if(number >= 0.9):
            print("A")
        elif(number >= 0.8):
            print("B")
        elif(number >= 0.7):
            print("C")
        elif(number >= 0.6):
            print("D")
        else:
            print("F")

        break

    except:
        print("To nije broj.")
