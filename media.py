print('****** NOTAS ******')
print('Média para aprovação: 8.5')

continua = ('s')

while continua == 's':

    name = input('Informe o nome do aluno: ')
    name = name.upper()

    n1 = float(input('Nota do primeiro semestre: '))
    n2 = float(input('Nota do segundo semestre: '))

    media = (n1 + n2)/2

    if media >= 8.5:
        print('{}, sua média é {}. Portanto você está aprovado!'.format(name, media))
        continua = input('Para consultar outro aluno digite "s", para sair digite "x" ')
    else:
        print('{}, sua média é {}. Portanto você está reprovado!'.format(name, media))
        continua = input('Para consultar outro aluno digite "s", para sair digite "x" ')

print(" SAINDO...")
