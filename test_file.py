
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

x = dec_to_bi(str(input()))
print(x)