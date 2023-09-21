# Desafio 015
# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

tempC = float(input('Informe a temperatura ºC: '))
tempF = (tempC * 9 / 5) + 32
print('A temperatura de {}ºC corresponde a {}ºF.'.format(tempC, tempF))
