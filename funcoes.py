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