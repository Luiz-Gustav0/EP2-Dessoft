import random 
def cria_pecas():
    numeros = [0,1,2,3,4,5,6]
    lista_usados = []
    lista_pecas = []
    for numero in numeros:
        lista_peca = []
        for n in numeros:
            lista_peca = [numero,n]
            if lista_peca not in lista_usados:
                lista_pecas.append(lista_peca)
                lista_usados.append(lista_peca)
                inverso = [n,numero]
                lista_usados.append(inverso)
            else:
                pass
    lista = random.sample(lista_pecas,28)
    return lista

def verifica_ganhador(dicionario):
    ganhador = 0
    for vencedor,pecas in dicionario.items():
        if len(pecas) == 0:
            return vencedor
            ganhador += 1
    if ganhador == 0:
        return -1

def soma_pecas (lista_pecas):
    soma = 0 
    for numeros in lista_pecas:
        soma += numeros[0]
        soma += numeros[1]
    return soma

#Posições possíveis da mão

def posicoes_possiveis(x,y):
    lista_posicoes = []
    n = 0
    if len(x) == 0:
        for i in y:
            lista_posicoes.append(n)
            n +=1
    else:
        for pecas in y:
            if x[0][0] in pecas or x[-1][1] in pecas:
                lista_posicoes.append(y.index(pecas))
            
    return lista_posicoes