def init():
    print('''
    [1] Português
    [2] English
    ''')
    return int(input('Escolha o idioma / Choose the language: ').strip())

def translate(x):
    b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    h = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

    if x in b:
        for j, k in enumerate(b):
            if x == k:
                return h[j]
    elif x in h:
        for j, k in enumerate(h):
            if x == k:
                return b[j]    

def bi_to_dec(x):
    l = [int(i) for i in x]
    r = 0
    for j, k in enumerate(l[::-1]):
        if k == 1:
            r += (2**j)
    return r

def dec_to_bi(x):
    n = int(x)
    l = []
    num = n
    if n in [0, 1]:
        return (x)
    else:
        while True:
            quo = num // 2
            if quo == 1:
                l.append(str(num % 2))
                l.append('1')
                break
            else:
                l.append(str(num % 2))
                num = quo
        nl = l[::-1]
        return ''.join(nl)

def bi_to_hex(x):
    if len(x) % 4 != 0:
        add = len(x) % 4
        x = '0'*(4-add) + x
    
    l = []
    item = ''
    for j, k in enumerate(x):
        item += k
        if (j+1) % 4 == 0:
            l.append(item)
            item = ''
    
    r = ''
    for i in l:
        r += translate(i)

    return r

def hex_to_bi(x):
    r = ''
    for i in x:
        r += translate(i)
    r = int(r)
    return (str(r))
    
opc = init()
if opc == 1:
    print('''
    [1] Binário - Base 2
    [2] Decimal - Base 10
    [3] Hexadecimal - Base 16
    ''')
    base_list = [0, 'Binário', 'Decimal', 'Hexadecimal']
    send = int(input('Qual a base inicial? '))
    num1 = str(input('Digite o número: '))
    recept = int(input('Para qual base quer mudar? '))
    res = None

    if send == 1:
        if recept == 2:
            res = bi_to_dec(num1)
        elif recept == 3:
            res = bi_to_hex(num1)
    elif send == 2:
        if recept == 1:
            res = dec_to_bi(num1)
        elif recept == 3:
            r = dec_to_bi(num1)
            res = bi_to_hex(r)
    elif send == 3:
        if recept == 1:
            res = hex_to_bi(num1)
        elif recept == 2:
            r = hex_to_bi(num1)
            res = bi_to_dec(r)
    
    print()
    print(f'{num1} ({base_list[send]}) ==> {res} ({base_list[recept]})')
    
elif opc == 2:
    print('''
    [1] Binary - Base 2
    [2] Decimal - Base 10
    [3] Hexadecimal - Base 16
    ''')
    base_list = [0, 'Binary', 'Decimal', 'Hexadecimal']
    send = int(input('Which is the initial base? '))
    num1 = str(input('Type the number: '))
    recept = int(input('To which base do you want to change? '))
    res = None

    if send == 1:
        if recept == 2:
            res = bi_to_dec(num1)
        elif recept == 3:
            res = bi_to_hex(num1)
    elif send == 2:
        if recept == 1:
            res = dec_to_bi(num1)
        elif recept == 3:
            r = dec_to_bi(num1)
            res = bi_to_hex(r)
    elif send == 3:
        if recept == 1:
            res = hex_to_bi(num1)
        elif recept == 2:
            r = hex_to_bi(num1)
            res = bi_to_dec(r)
    
    print()
    print(f'{num1} ({base_list[send]}) ==> {res} ({base_list[recept]})')
