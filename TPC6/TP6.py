#Molelo: [nome, desc, periodo, ano,...]

import csv

# (1) Carrega o dataset para uma estrutura de dados pensada por ti
def leObras(filename):
    file=open(filename, encoding='UTF8') #Mapear o texto para os bytes. Algoritmo de encoding específico.

    csv_file = csv.reader(file, delimiter=';')
    file.readline()

    lista=[]
    for obra in csv_file:
        lista.append(tuple(obra))
    
    return lista


# (2) Quantas obras existem catalogadas no dataset?
def NObras(obras):
    return len(obras)


# (3) Imprime no monitor uma tabela com o título da obra, a sua descrição, o seu compositor e ano de criação;
def Imprime(obras): #Com obras=[(nome, descrição, ano de criação, período, compositor, duração, id)]
    print(f" | {'nome':^20} | {'Descrição':^25} | {'Ano':^8} | {'Compositor':^15} | ")
    for nome, desc, ano, _, comp, *_ in obras:
        #print(nome, desc, ano, comp)

        print(f" | {nome[:20]:^20} | {desc[:25]:^25} | {ano:^8} | {comp[:15]:^15} | ")


# (4) Produz uma lista de tuplos `(título, ano)` ordenada alfabeticamente por título
def Ordem(tuplo):
    return tuplo[0]

def titleAno(obras):
    lista=[]
    for nome, _, ano, _, *_ in obras:
        lista.append((nome,ano))
    
    lista.sort(key=Ordem) # OU key=lambda tuplo: tuplo[1]

    return lista


# (5) Produz uma lista de tuplos `(título, ano)` ordenada crescentemente por ano
def titleAno_2(obras):
    lista=[]
    for nome, _, ano, _, *_ in obras:
        lista.append((nome,ano))
    
    lista.sort(key=lambda tuplo: tuplo[1]) 

    return lista

# (6) Produz uma lista ordenada dos compositores
def OrdComp(obras):
    lista=[]
    for _, _, _, _, comp, *_ in obras:
        lista.append(comp)
    
    lista.sort(key=Ordem) # OU key=lambda tuplo: tuplo[1]

    return lista


# (7) Calcula uma distribuição das obras por período
def distribPeriodo(obras):
    dict={}
    for _, _, _, periodo, *_ in obras:
        if periodo in dict.key():
            dict[periodo] = dict[periodo] + 1
        else: 
            dict[periodo] = 1
    
    return dict
      

# (8) Calcula uma distribuição das obras por ano
def titPorAno(obras):
    dict={}
    for nome, _, ano, _, *_ in obras:
        if ano in dict.keys(): #procura nas keys
            dict[ano].append(nome)
        else: 
            dict[ano]=[nome]

    return dict


# (9) Calcula uma distribuição das obras por compositor
def titPorComp(obras):
    dict={}
    for nome, _, _ , _, comp, *_ in obras:
        if comp in dict.keys(): #procura nas keys
            dict[comp].append(nome)
        else: 
            dict[comp]=[nome]

    return dict

# (10) Especifica uma função que recebendo uma distribuição desenha o seu gráfico. Aplica-a às distribuições anteriores

def distPeriodo(obras): 
    dict1 = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dict.keys():
            dict1[periodo] = dict1[periodo] + 1
        else:
            dict1[periodo] = 1
    return dict1    

def distAno (obras): 
    dict2 = {}
    for _, _, ano, *_ in obras:
        if ano in dict2.keys():
            dict2[ano] = dict2[ano] + 1
        else:
            dict2[ano] = 1
    return dict2  

def distCompositores(obras):
    dict3 = {}
    for _, _, _, _, comp, *_ in obras:
        if comp in dici3.keys():
            dict[comp] = dict3[comp] + 1
        else:
            dict3[comp] = 1
    return dict3


def Grafico1(obras):
    
    dict=distPeriodo(obras)
    periodo = dict.keys()
    obras = dict.values()

    plt.bar(periodo, obras)   
    plt.xlabel('Período')
    plt.ylabel('Obras')
     
    plt.title("Distribuição das Obras por período")
    plt.show()



def Grafico2(obras): 

    dict =distAno(obras)
    ano = dict.keys()
    obras = dict.values()

    plt.bar(ano, obras)
    plt.xlabel('Ano')
    plt.ylabel('Obras')
     
    plt.title("Distribuição das Obras por Ano")
    plt.show()


def Grafico3(obras): 
    
    dicit=distCompositores(obras)
    compositor = dicit.keys()
    obras = dicit.values()

    plt.bar(compositor, obras)
    plt.xlabel('Compositor')
    plt.ylabel('Obras')
     
    plt.title("Distribuição das Obras por Compositor")
    plt.show()

# (11) Problema da inversão estrutural: calcula uma estrutura de dados que corresponde a uma lista dos compositores em que cada compositor tem a ele associado uma lista dos títulos das obras que compôs

def inversao(obras): 
    dici = {}
    lista1=[]
  
    for nome, _, _,_,compositor, *_ in obras:
        if compositor in dici.keys():
            dici[compositor].append(nome)
        else:
            dici[compositor] = [nome]
    for keys,values in dici.items():
        lista1.append([keys] + [values])
    
   
    return lista1
