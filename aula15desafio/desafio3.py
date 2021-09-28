"""
Faça um programa que peça o primeiro nome do usuário, se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 a 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Insira o seu primeiro nome: ')

if nome.isalpha():
    if len(nome) <= 1:
        print('Isso não é um nome!')
    elif len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) <= 5 or len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Isso não é uma letra!')
