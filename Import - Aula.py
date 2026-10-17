#------------------------------ importando o módulo math ------------------------------#

import math

numero = 25

print(math.sqrt(numero))
#retorna a raiz quadrada do número
print(math.sqrt(81))
#retorna a raiz quadrada do número

print(math.pow(2, 3))
#retorna o número elevado a potência
print(math.ceil(4.2))
#arredonda para cima
print(math.floor(4.8))
#arredonda para baixo

#------------------------------ importando o módulo random ------------------------------#

import random

print("------- Exemplo de uso do módulo random -------")
numero = random.randint(1, 10)
print(numero) #retorna um número inteiro aleatório entre 1 e 10


print("\n------- Jogo de adivinhação -------")
secreto = random.randint(1, 10)
tentativa = int(input("Digite um número: "))

if tentativa == secreto:
    print("Você acertou!")
else:
    print("Você errou!")
    print("O número era:", secreto)


print("\n------- Exemplo de uso/variações do módulo math -------")
import math
print(math.sqrt(25)) #importa o módulo math e retorna a raiz quadrada do número

from math import sqrt
print(sqrt(25)) #importa apenas a função sqrt do módulo math e retorna a raiz quadrada do número

import math as m
print(m.sqrt(25)) #renomeia o módulo math para m e retorna a raiz quadrada do número

