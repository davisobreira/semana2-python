print('****** MONITORAMENTO DE TRÂNSITO ******')
print('LIMITE DA RODOVIA: 80Km/h')

speed = int((input('Informe a velocidade do veículo: ')))
result = speed - 80
multa = (0)

if speed >= 80:
    multa = multa + (result*7)
    print('Sua velocidade é de: {}Km/h. Veículo multado! Sua multa será de R${}'.format(speed, multa))
else:
    print('Sua velocidade é de: {}Km/h. Continue a viagem sem preocupação!'.format(speed))