def hindifinder(testText):
    if ('arey','yaar','mai','dekho','kya','kyu','kaha','abe','mera') in testText:
        print('es hindi! ')
    else:
        print('i dont think its hindi')
    
def uwu():
    print('Henwo fren, how awe you')
    print('entew some text pwease')
    text = input()
    bettertext = text.replace('l','w')
    bettertext = bettertext.replace('r','w')
    print('uwuified text bewow! :3 cya!')
    print('-------------------------------------------------')
    print(bettertext)

def paan():
    basicText = input().lower()
    betterText = basicText.replace('r','w')
    print(betterText)

def pyaar():
    basicText = input().lower()
    betterText = basicText.replace('r','l')
    print(betterText)

print('enter text ')
hindifinder(input())
#pyaar()
#paan()
#uwu()
