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