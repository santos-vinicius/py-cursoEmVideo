# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Qual é o preço do produto? R$'))
desconto = preco - (preco * 5/100)


print('O produto custava R${} e com o desconto de 5% passa a custar R${}'.format(preco, desconto))
