import funcoes as ep2

print('Insper Dominó')
print('=> Design de Software \n')
print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores. \n')
print('Vamos Começar!!! \n')

a = input('Quantos jogadores? (2-4)')

pecas = ep2.cria_pecas

if a == 2:
    comeco = ep2.inicia_jogo(2,pecas)
