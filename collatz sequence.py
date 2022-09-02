print('Enter number:')
while True:
    try:
        num = int(input())
        break
    except ValueError:
        print('Pls enter a number')
        continue
while num !=1:
    if num % 2 ==0:
        print (str(num//2))
        num = num//2
    else:
        print(str(3*num+1))
        num = 3*num+1
