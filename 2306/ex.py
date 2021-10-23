carteira = float(input('Informe o seu salário mensal: R$'))
km = float(input('Quantos km faz o seu carro com um litro? '))
distancia = float(input('Quantos km você percore em um dia de trabalho? '))
diastrabalho = int(input('Quantos dias você trabalha? '))
print('------------------')

gasolinalitro = 7.99
calckm = distancia / km
calcgas = calckm * gasolinalitro
calcmes = calcgas * diastrabalho
param = ''

while True:

    if carteira > calcmes :
        print(f'Por dia você precisará de {calckm:.2f} litros de gasolina que irão custar R$ {calcgas:.2f}')
        print(f'E por mês usará para trabalhar {calckm*diastrabalho:.2f} litros de gasolina que irão custar R$ {calcmes:.2f}')
        print(f'Gasolina: R$ {gasolinalitro}')
        print(f'Sobra R$ {carteira-calcmes:.2f} do seu salário.')
        break

    emprestimo = input('Parece que Você não tem dinheiro suficiente, quer fazer um empréstimo? (s/n)')

    if emprestimo != 's' and emprestimo != 'n':
        print('Informe apenas s ou n !')
        continue
    if emprestimo == 's':
        valoremprestado = float(input('Quanto deseja fazer de empréstimo? R$'))
        calcemprestimo = calcmes - carteira
        taxa = valoremprestado * 0.08
        carteiraNova = carteira + valoremprestado
        if carteiraNova < calcmes:
            print('Você não conseguirá pagar a gasolina com esse valor, tente outro empréstimo!')
        else:
            print('------------------')
            print(f'Empréstimo concluído')
            print(
                f'O valor emprestado sera cobrado com uma taxa de 8%, você ficará nos devendo {valoremprestado + taxa:.2f}')
            print('------------------')
    elif emprestimo == 'n':
        print('Não podemos fazer nada!!')
        break

    if carteiraNova > calcmes:
        print(f'Por dia você precisará de {calckm:.2f} litros de gasolina que irão custar R$ {calcgas:.2f}')
        print(
            f'E por mês usará para trabalhar {calckm * diastrabalho:.2f} litros de gasolina que irão custar R$ {calcmes:.2f}')
        print(f'Gasolina: R$ {gasolinalitro}')
        print(f'Sobra R$ {carteiraNova-calcmes:.2f} no seu bolso.')
        break
