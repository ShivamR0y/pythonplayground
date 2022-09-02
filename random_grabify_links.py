import random,string,webbrowser
def randDo():
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters)for i in range(6))

for i in range(25):
    webbrowser.open('https://grabify.link/track/'+randDo())
    print('https://grabify.link/track/'+randDo())
