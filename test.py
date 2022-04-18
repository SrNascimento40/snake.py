import funca
import random

maxn = 10
n = random.randint(1, maxn)
print('Seja bem-vindo ao jogo de advinhação numérica, meu parça !')
print('Chute um número de 1 a %d' % maxn)
guess = None
while guess != n:
    guess = int(input('Seu chute: '))
    if guess > n:
        print('Altão, mané :(')
    if guess < n:
        print('Baixo pacarai :(')

print('Aí sim, zika, tu venceu! :)')
#Programa do Patrick


tot = int(input('Qual o valor total?\t'))
porc = int(input('Quantos % você deseja?\t'))
result = funca.porcentagem(tot, porc)
print(f'{porc}% de {tot} é igual à {result}')

