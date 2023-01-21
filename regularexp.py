#Regular Expression Exercise
import re
mystrings = '''My name is harry. My mobile no. is +919096555570. and I am happy.
                and brother have also mobile. He also have mobile no +918422445566. 
                I love my country. And I am proud of it's rich. And very heritage.
                +918888073502 '''
patt = re.compile(r'\b91\d{10}')
matches = patt.finditer(mystrings)
for match in matches:
    print(match)