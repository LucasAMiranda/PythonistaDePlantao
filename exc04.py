# tabuada

num = int(input('Escolha a tabuada: '))
comeco = int(input('Começa por: '))
fim = int(input('termina em: '))

if comeco > fim:
    comeco = fim
    aux = comeco
print('começar minha tabuada por {} começando por {} e terminando por {}'.format(num, comeco, fim))

for x in range(comeco, fim + 1):
    print(num, 'x', x, '= ', num * x)


