"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. ex.
bom dia 0-11, boa tarde 12-17 e boa noite 18-23.
"""

hora = input('Informe uma hora entre 0 - 23 horas: ')

if hora.isnumeric():
    if int(hora) >= 0 and int(hora) <=11:
        print('Bom dia!')
    elif int(hora) >= 12 and int(hora) <=17:
        print('Boa tarde!')
    elif int(hora) >= 18 and int(hora) <= 23:
        print('Boa noite!')
    else:
        print('Hora não existe!')
elif hora.isalnum():
    print('Você tá inserindo uma letra!')
