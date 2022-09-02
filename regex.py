import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('hello fren plas get my number at 901-655-3683.')
print('phone number found : '+mo.group())
