n1 = int(input('informe o primeiro número: '))
n2 = int(input('informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))


if (n3 < n2):
   aux = n3
   n3 = n2
   n2 = aux

if(n2 < n1):
    aux = n2
    n2 = n1
    n1 = aux

if(n3 < n1):
    aux = n3
    n3 = n2
    n2 = aux

print('\n', n3)
print('\n', n2)
print('\n', n1)
