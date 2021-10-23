import random

nomes = ['luan', 'lucas']
secreto = random.choice(nomes)
guardarletra = []
chances = 3

while True:
    if chances <= 0:
        print(f'Você perdeu! a palavra era {secreto}')
        break;

    letra = input('Informe uma letra: ')

    if len(letra) > 1:
        print('Apenas uma letra!')
        continue

    guardarletra.append(letra)

    if letra in secreto:
        print(f'a letra "{letra}" existe no nome!')
    else:
        print(f'a letra informada não existe !!')
        guardarletra.pop()
        chances -= 1

    nometemporario = ''

    for letra_secreta in secreto:
        if letra_secreta in guardarletra:
            nometemporario += letra_secreta
        else:
            nometemporario += '*'

    if nometemporario == secreto:
        print(f'Você concluiu o nome, ele era "{secreto}" !!')
        break
    else:
        print(nometemporario)

    print(f'Chances: "{chances}"')