def globalCheck():
    global globalvar
    globalvar = 'global variable edited in a function'
    localvar = 'local variable'
    print(localvar)

globalvar = 'global variable'
print(globalvar)
globalCheck()
print(globalvar)
