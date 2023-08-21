import random
from time import sleep

print('===== PAR ou ÍMPAR =====')
resp = 'S' and 's'
continua = resp
while continua == resp:
    option = input('Escolha "par" ou "ímpar": ')
    match option:
        case 'par':
            print('Então eu escolho ímpar')
            nr = random.randint(1, 10)
            num = int(input('Qual o seu número? '))
            print('Meu número é: {}'.format(nr))
            print('RESULTADO...')
            sleep(1)
            s = nr + num
            result = 'par' if s % 2 == 0 else 'ímpar'
            if result == 'par':
                print('Parabéns vocẽ venceu! {} é par.'.format(s))
                continua = input('Quer jogar mais uma vez? [S/N] ')
            else:
                print('Sinto muito! Eu venci pois o número {} é ímpar.'.format(s))
                continua = input('Quer jogar mais uma vez? [S/N] ')

        case 'ímpar' | 'impar':
            print('Então eu escolho par')
            nr = random.randint(1, 10)
            num = int(input('Qual o seu número? '))
            print('Meu número é: {}'.format(nr))
            print('RESULTADO...')
            sleep(1)
            s = nr + num
            result = 'par' if s % 2 == 0 else 'ímpar'
            if result == 'ímpar':
                print('Parabéns vocẽ venceu! {} é ímpar.'.format(s))
                continua = input('Quer jogar mais uma vez? [S/N] ')
            else:
                print('Sinto muito! Eu venci pois o número {} é par.'.format(s))
                continua = input('Quer jogar mais uma vez? [S/N] ')
print('Obrigado por jogar! Até o próximo jogo!')
