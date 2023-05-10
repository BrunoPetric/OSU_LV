while True:
    grade = input('Input a grade between 0.0 and 1.0: ')
    try:
        grade = float(grade)
    except:
        print('Please input a number!')
        continue
    if grade >= 0.0 and grade <= 1.0:
        break
    print('Please input a valid number!')
if grade >= 0.9:
    print('Category: A')
elif grade >= 0.8:
    print('Category: B')
elif grade >= 0.7:
    print('Category: C')
elif grade >= 0.6:
    print('Category: D')
else:
    print('Category: F')