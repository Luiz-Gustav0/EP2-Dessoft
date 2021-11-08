#Criando peças de dominó

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

#Quem ganhou no dominó?

def verifica_ganhador(dicionario):
    ganhador = 0
    for vencedor,pecas in dicionario.items():
        if len(pecas) == 0:
            return vencedor
            ganhador += 1
    if ganhador == 0:
        return -1

#Soma peças de dominó

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

#Iniciando o Jogo de Dominó

def inicia_jogo(quant_jog, lista_pecas):
    i = 0
    participantes = {}
    x = []
    y = []
    pecas = 0
    numero_pecas = 28
    peca_jogador = 0

    while i < quant_jog:
        pecas += 7
        lista_pecas_jog = []
        while peca_jogador < pecas:
            lista_pecas_jog.append(lista_pecas[peca_jogador])
            participantes[i] = lista_pecas_jog
            peca_jogador += 1
            numero_pecas -= 1
        i+=1
    
    while numero_pecas > 0:
        x.append(lista_pecas[peca_jogador])
        peca_jogador +=1
        numero_pecas -= 1

    dicionario = {}

    dicionario['jogadores'] = participantes
    dicionario['monte'] = x
    dicionario['mesa'] = y

    return dicionario

#Adicionando peças a mesa num jogo de dominó
def adiciona_na_mesa(peca,situacao_mesa):
    nova_situacao_mesa = []

    if situacao_mesa == []:
        nova_situacao_mesa.append(peca)
    elif peca[1] == situacao_mesa[0][0] :
        nova_situacao_mesa.append(peca)
        nova_situacao_mesa.append(situacao_mesa[0])
    elif peca[1] == situacao_mesa[-1][-1] :
        peca.reverse()
        for valor in range (0 , len(situacao_mesa)):
            nova_situacao_mesa.append(situacao_mesa[valor])
        nova_situacao_mesa.append(peca)
    elif peca[0] == situacao_mesa[0][0] :
        peca.reverse()
        nova_situacao_mesa.append(peca)
        for valor in range (0 , len(situacao_mesa)):
            nova_situacao_mesa.append(situacao_mesa[valor])
    elif peca[0] == situacao_mesa[-1][-1] :
        for valor in range (0 , len(situacao_mesa)):
            nova_situacao_mesa.append(situacao_mesa[valor])
        nova_situacao_mesa.append(peca)

    return nova_situacao_mesa