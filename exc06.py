#Digite um número de 1 a 100 e faça a contagem perguntando se ele é um número primo ou não



for num in range(1, 100):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        print(x, resto)

        if resto == 0:
            div = div + 1

    if div == 2:
        print('O número {} é primo'.format(num))
    else:
        print('O número {} não é primo'.format(num))