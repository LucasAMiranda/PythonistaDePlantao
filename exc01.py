n1 = int(input('informe o primeiro número: '))
n2 = int(input('informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

maior = n1
menor = n1

if maior < n2:
    maior = n2

if maior < n3:
    maior = n3

if menor > n2:
    menor = n2

if menor > n3:
    menor = n3

print('O número {} é o maior'.format(maior))
print('O número {} é o menor'.format(menor))