import pyautogui,time,random
time.sleep(6)

names = []

messages = []

for i in range(20):
    #print()
    pyautogui.typewrite(random.choice(names)+random.choice(messages),interval = 0.05)
    pyautogui.press('enter')
    
