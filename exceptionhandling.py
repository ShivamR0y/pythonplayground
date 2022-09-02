def divide():
    
    print('enter numerator')

    while True:
        try:
            numOne = int(input())
            break
        except ValueError:
            print('enter a number mate')
            continue
            
    print('enter denominator')

    while True:
        try:
            numTwo = int(input())
            break
        except ValueError:
            print('enter a number mate')
            continue
        
    try:
        print('the numbers divided results is :')
        print(numOne/numTwo)
    except ZeroDivisionError:
        print('Ooops! cant divide by zero!')

more = True
print('enter two numbers to divide them ')
divide()
while more:
    print('continue? [Y/N]')
    check = input().lower()
    if check == 'y':
        divide()
        continue
    elif check == 'n':
        break
    else:
        print('Sorry mate wrong input')
        continue
