#função para converter qualquer número em uma base para o seu correspondente em Decimal

def número_para_decimal(número, base):

    # o número decimal correspondente
    decimal = int(número, base)

    binário = bin(decimal)
    octal = oct(decimal)
    hexadecimal = hex(decimal)

    print('Decimal :' +str(decimal))
    print('Binário :' +str(binário[2:]))
    print('Octal:' +str(octal[2:]))
    print('Hexadecimal :' +str(hexadecimal[2:].upper()))

# número a ser convertido e a sua base
número = '010111'
base = 2

número_para_decimal(número, base)