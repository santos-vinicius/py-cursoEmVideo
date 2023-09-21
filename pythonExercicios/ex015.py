# Desafio 015
# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado.
# Calcule o preço a pagar sabendo que o carro custa R$ 60 por dia e R$0.15 por KM rodado.

dias = int(input('Quantos dias foram alugados: '))
km = float(input('Quantos KM foram rodados: '))
divida = (dias * 60) + (km * 0.15)

print('O valor a ser pago pelo aluguel de {} dias e {}KM rodados é: R${:.2f}'.format(dias, km, divida))