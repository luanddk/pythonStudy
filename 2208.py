import random

lista = ['luan','lucas']
secreto = random.choice(lista)
digitadas = []
escolhidas = []
chances = 3

while True:

    if chances <= 0:
        print(f'Você perdeu!! a palavra era {secreto}')
        break

    letra = input('Informe uma letra: ')

    if len(letra) > 1:
        print('Apenas uma letra!!')
        continue

    if letra in digitadas:
        print(f'a letra "{letra.upper()}" já foi escolhida!')
        print(f'Letras escolhidas : {escolhidas}')
        print(secreto_temporario)
        continue

    digitadas.append(letra)
    escolhidas.append(letra)

    if letra in secreto:
        print(f'a letra "{letra.upper()}" existe no nome!')
    else:
        print('Letra errada!')
        print(f'Letras escolhidas : {escolhidas}')
        digitadas.pop()
        chances -= 1

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns !! a palavra era {secreto.upper()}')
        break
    else:
        print(secreto_temporario)
    print(f'Chances: "{chances}"')



