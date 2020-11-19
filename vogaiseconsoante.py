#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = input("informe a letra digitada: ")
vogal = ['a', 'e', 'i', 'o', 'u']
letra = vogal
consoante = []
letra = consoante

for i in letra:
    if i == vogal:
        print("A letra digitada é vogal {}".format(i))
    else:
        print("A letra digitada é consoante{}".format(i))

'''
#Função
def vogal(z):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if z in vogais:
        print('Vogal')
        return True
    else:
        print('Consoante')
        return False

#Debugando
resultado = vogal("A")
print(resultado) #True

resultado = vogal("N")
print(resultado) #False
