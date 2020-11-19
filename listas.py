alunos = [
    "Rafael1",
    "Rafael2"
]
bimestres = [
    "1 Bim",
    "2 Bim",
    "3 Bim",
    "4 Bim",
    "5 Bim",
    "6 Bim",
]
pesos = {
    "1 Bim": 2.0,
    "2 Bim": 3.0,
    "3 Bim": 3.0,
    "4 Bim": 4.0,
    "5 Bim": 5.0,
    "6 Bim": 5.0,
}
numerador = {}
denominador = sum(pesos.values())
media = 6

for aluno in alunos:
    print("Aluno: ", aluno)
    numerador[aluno] = 0
    for bimestre in bimestres:
        nota = input("Digite a nota do {}: ".format(bimestre))
        nota = float(nota)
        numerador[aluno] += nota * pesos[bimestre]

    media = numerador[aluno] / denominador
    print("Nota final {}: {:.2f}".format(aluno, media))

    if media > 9:
        print("Nota A")
    elif 9 >= media > 7:
        print("Nota B")
    elif 7 >= media > 5:
        print("Nota C")
    else:
        print("Nota D")

    print("*"*20)