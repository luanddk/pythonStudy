"""
* CRIAR VARIAVEIS PARA NOME (STR), IDADE (INT),
* ALTURA (FLOAT) E PESO (FLOAT) DE UMA PESSOA
* CRIAR VARIAVEL COM O ANO ATUAL (INT)
* OBTER O ANO DE NASCIMENTO DA PESSOA (BASEADO NA IDADE E NO ANO ATUAL)
* OBTER O IMC DA PESSOA COM 2 CASAS DECIMAIS (PESO E NA ALTURA DA PESSOA)
* EXIBIR UM TEXTO COM TODOS OS VALORES NA TELA USANDO F-STRINGS (COM AS CHAVES)

"""

nome = 'Luan'
idade = 22
altura = 1.70
peso = 65.5
ano = 2021 - idade
imc = peso/(altura**2)

print(f'{nome} tem {idade} anos de idade, tem {altura} de altura e pesa {65} kg. \n O IMC de {nome} é {imc:.2f}. \n {nome} nasceu em {ano}.')
