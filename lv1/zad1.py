def total_euro(sat, satnica):
    print(sat*satnica)
while True:
    try: 
        sat = float(input())
        satnica = float(input())
        total_euro(sat, satnica)
        break
    except ValueError:
        print("Nije broj")




