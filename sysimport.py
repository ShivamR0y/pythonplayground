import sys
name = ''
while True:
    print('Type exit to exit.')
    name = input()
    if name=='exit':
        sys.exit()
    print('you typed '+name)
