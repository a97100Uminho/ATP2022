# Modelo=[(anúmero, nome, curso, nota, nota, nota, nota)]

import csv

# (1) Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória.
def le(filename):
    file=open(filename, encoding='UTF8') #Mapear o texto para os bytes. Algoritmo de encoding específico.

    csv_file = csv.reader(file, delimiter=',')
    file.readline()

    lista=[]
    for aluno in csv_file:
        lista.append(tuple(aluno))
    

    return lista

def Imprime(Turma): #Com obras=[(nome, descrição, ano de criação, período, compositor, duração, id)]
    print(f" | {'anúmero':^10} | {'Nome':^25} | {'Curso':^10} | {'Nota1':^10} | {'Nota2':^10} | {'Nota3':^10} | {'Nota4':^10} |")

    for anum, nome, curso, nota1, nota2, nota3, nota4 in Turma:
            
        print(f" | {anum[:10]:^10} | {nome[:25]:^25} | {curso[:10]:^10} | {nota1[:10]:^10} | {nota2[:10]:^10} | {nota3[:10]:^10} | {nota4[:10]:^10} |")

# (2) Crie uma função que calcula a distribuição dos alunos por curso.

def distCurso(Turma):
    dictcursos={}

    for _, nome, curso, *_ in Turma: 
        if curso in dictcursos.keys():
            dictcursos[curso] = dictcursos[curso] + 1
        else: 
            dictcursos[curso] = 1

    
    return dictcursos

# (3) Crie uma função que calcula a média das notas de cada aluno e acrescenta essa nova coluna no dataset em memória.

def media(Turma):
    dictmedias={}

    for _, nome, _, nota1, nota2, nota3, nota4 in Turma:
        media = (int(nota1) + int(nota2) + int(nota3) + int(nota4))/4
        if nome not in dictmedias.keys():
            dictmedias[nome] = float(media)
        
    return dictmedias

# (4) Considere os seguintes escalões de notas: E [1-4], D [5-8], C [9-12], B [13-16], A [17-20], acrescente uma coluna ao dataset com o escalão correspondente a cada aluno.

# (4.1) Cria uma lista com a média do aluno respetivo. 
def notas(Turma):
    dictescaloes={}

    for _, nome, _, nota1, nota2, nota3, nota4 in Turma: 
        if nome not in dictescaloes.keys():
            dictescaloes[nome] = [(int(nota1) + int(nota2) + int(nota3) + int(nota4))/4]

    return dictescaloes

# (4)

def dictmedias(Turma):
    a=media(Turma)
    
    escalaoA = []
    escalaoB = []
    escalaoC = []
    escalaoD = []
    escalaoE = []

    lista=[]


    for aluno in a.keys():

        if (float(a.values) >= 1 and float(a.values)  <= 4.99):
            escalaoE.append(aluno)

        elif (float(a.values) >= 5 and float(a.values) <= 8.99):
            escalaoD.append(aluno)

        if (float(a.values) >= 9 and float(a.values) <= 12.99):
            escalaoC.append(aluno)

        elif (float(a.values) >= 13 and float(a.values) <= 16.99):
            escalaoB.append(aluno)

        if (float(a.values) >= 17 and float(a.values) <= 20):
            escalaoA.append(aluno)
        
        b = (aluno, a.values(aluno))
        
    return b

# (5) Crie uma distribuição dos alunos por escalão.



# (6) Crie uma função que apresenta na forma dum gráfico de linha uma distribuição.



# (7) Crie uma função que imprime na forma de uma tabela uma distribuição.



# (8) Especifique um programa que, ciclicamente, apresenta um menu com todas funcionalidades ao utilizador.






    