def init():
    print('''
    [1] Português
    [2] English
    ''')
    return int(input('Escolha o idioma / Choose the language: ').strip())

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
            pass
    elif send == 2:
        if recept == 1:
            res = dec_to_bi(num1)
        elif recept == 3:
            pass
    elif send == 3:
        if recept == 1:
            pass
        elif recept == 2:
            pass
    
    print()
    print(f'{num1} ({base_list[send]}) ==> {res} ({base_list[recept]})')
    
elif opc == 2:
    print('''
    [1] Binary - Base 2
    [2] Decimal - Base 10
    [3] Hexadecimal - Base 16
    ''')