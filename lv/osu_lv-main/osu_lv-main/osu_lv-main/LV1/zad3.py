numbers = []
while True:
    i = input('Input a number: ')
    if i == 'Done':
        break
    try:
        i = float(i)
    except:
        print('Please input a number or "Done"!')
        continue
    numbers.append(i)
print(f'Count: {len(numbers)}')
if len(numbers) != 0:
    print(f'Average: {sum(numbers)/len(numbers)}')
    print(f'Min: {min(numbers)}')
    print(f'Max: {max(numbers)}')
    print(sorted(numbers))
else:
    print('Average: N/A')
    print('Min: N/A')
    print('Max: N/A')
