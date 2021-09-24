"""
Operadores relacionais

== Igualdade
> Maior que
>= Maior ou igual
< Menor que
<= Menor ou igual
!= Diferente
"""

nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

# Limite para pegar empréstimo
idade_menor = 20 #Jovem
idade_maior = 30 #Passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar empréstimo.')
else:
    print(f'{nome} Não pode pegar empréstimo.')
