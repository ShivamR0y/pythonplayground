import string
letters = string.ascii_lowercase
vovels = 'aeiou'
numbers = int(input())
sentences = []
key = 6
for i in range(numbers):
    sentences.append(str(input()).lower())
for i in range (numbers):
    decrypted =  ''
    count= 0
    for c in sentences[i]:
        if c in letters:
            pos = letters.find(c)
            new_pos = (pos - key)%26
            new_letr = letters[new_pos]
            decrypted+=new_letr
    for c in decrypted:
        if c in vovels:
            count+=1
    print(count)
        
