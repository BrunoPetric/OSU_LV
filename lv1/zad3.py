import statistics

polje = []
while True:
    a = input()
    if(a == 'Done'):
        break
    try:     
        broj = float(a)
        polje.append(broj)
    except ValueError:
        print("Nije unesen broj")

print('Duljina: ', len(polje))
print('Prosijek: ', statistics.mean(polje))
print('Max: ', max(polje))
print('Min: ', min(polje))