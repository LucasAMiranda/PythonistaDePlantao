
num_alunos = 3
nomes = []
notas = []
media = 0

for i in range(num_alunos):
    nomes.append(input('Informe o nome do aluno: '))
    notas.append(float(input('Informe a nota de ' + nomes[i] + ': ')))
    media = media + notas[i]

    media = media / num_alunos
    print('A media da turma eh {}'.format(media))

for i in range(num_alunos):
    if notas[i] > media:
        print('Parabens', nomes[i])









'''

notas = [8.0, 5.5, 1.5]
for i in range(3):
    print(notas[i])
'''