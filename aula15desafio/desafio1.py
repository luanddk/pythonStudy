"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar, Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
(numero % 2) == 1:
"""

numero = input('Informe o número inteiro: ')

if numero.isnumeric() and (int(numero)%2) == 0:
    print(f'O número {numero} é par')
elif numero.isnumeric() and (int(numero)%2) == 1:
    print(f'O número {numero} é impar')
else:
    print(f'O valor {numero} não é um inteiro!')
