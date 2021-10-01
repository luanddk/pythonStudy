secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break
    
    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:  # Verifica se o usuário digitou apenas uma string.
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)  # A letra é guardada na lista até verificação.
    
    if letra in secreto:  # Verifica a existência da letra na variável secreto.
        print(f'Uhhuul, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Afffz a letra "{letra}" não existe na palavra secreta!')
        digitadas.pop()  #  Caso letra seja não identificada ela é removida, 'pop' remove a última posição da lista.

    secreto_temporario = ''  # Variável temporária criada para ser usada no FOR.
    for letra_secreta in secreto:  # For criado para percorrer a palavra enquanto jogador insere as letras.
        if letra_secreta in digitadas:  # IF a letra_secreta estiver dentro da variável secreto 'TRUE'.
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*' # String que esconde as letras ainda não inseridas.
    if secreto_temporario == secreto:  # Fora do escopo for a variável temporária serve de final ou preview.
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()