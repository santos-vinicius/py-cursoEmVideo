# Desafio 005
# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))
sucessor = num + 1
antecessor = num - 1

print('O valor digitado foi: {} \nSeu sucessor é:  {} \nE seu antecessor é: {}'.format(num, sucessor, antecessor))
