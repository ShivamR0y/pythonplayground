import pyautogui,time
time.sleep(10)
print ('press ctrl c to stop')
try:
    while True:
        if pyautogui.pixelMatchesColor(834,244,(83,83,83)):
            pyqutogui.typewrite('space')
except KeyboardInterrupt:
    print('\n quit!')
