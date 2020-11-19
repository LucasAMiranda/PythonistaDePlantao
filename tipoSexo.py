
#8.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Informe seu sexo: ")

if(sexo == 'f' or sexo=='F'):
    print("O tipo do sexo é Feminino.")
elif(sexo == 'm' or sexo == 'M'):
    print("O tipo do sexo é Masculino.")
else:
    print("O tipo de sexo informado é inválido!")