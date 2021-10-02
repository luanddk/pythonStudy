import random

lista = ['luan','lucas','hudson']
secreto = random.choice(lista)
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print(f'Você perdeu! a palavra era "{secreto}"')
        break

    letra = input('Informe uma letra: ')

    if len(letra) > 1:
        print('Informe apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print('Letra correta!')
    else:
        print('Letra não existe!')
        digitadas.pop()
        chances -= 1

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns!!! a palavra era "{secreto}"')
        break
    else:
        print({secreto_temporario})

    print(f'chances: {chances}')