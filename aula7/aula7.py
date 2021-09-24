"""
Iniciar com letra, pode conter, números, separar _, letras minúsculas
"""

nome = 'Luan Silva'
idade = 22
altura = 1.70
e_maior = idade > 18
peso = 60
imc = peso/(altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome,idade,imc))