def total_euro(sati, satnica):
    return sati * satnica


while(True):
    try:
        sati = float(input("Unesi broj radnih sati: "))
    except:
        print("To nije broj.")
        continue
    try:
        satnica = float(input("Unesi kolika je plaća po satu: "))
    except:
        print("To nije broj.")
        continue

    print("Ukupno:", total_euro(sati, satnica), "eura.")
    break
