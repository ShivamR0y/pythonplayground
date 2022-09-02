import pyautogui,time
print('started!')
time.sleep(8)
#f = open("/home/shivamr/Documents/PythonPlayground/EmojiMovie",'r')

num=['zero','one','two','three','four','five','six','seven','eight','nine']
iit =['IIT Tirupati',
'IIT Dhanbad (ISM)',
'IIT Bhilai',
'IIT Dharwad',
'IIT Jammu',
'IIT Goa']
for i in range(6):
    pyautogui.typewrite(":"+num[i]+": "+iit[i],interval = 0.13)
    pyautogui.press('enter')
    time.sleep(2)
"""a = 0
f = f.split()
with f as n:
    for line in n:
       if a%2==0:
            pyautogui.typewrite('you cant just '+line,interval=0.13)
            pyautogui.press('enter')
            a+=1
        else:
            a+=1

       # for word in line.split():
           # pyautogui.typewrite(word,interval=0.13)
           # pyautogui.press('enter')
#for word in f:
    #pyautogui.typewrite(word,interval=0.25)
    #pyautogui.press('enter')
    #print(word+'++')
"""
