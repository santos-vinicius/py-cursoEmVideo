# Desafio 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print('O número digitado foi: {}'.format(num))
print('O dobro deste valor é: {} \nO triplo é: {} \nA raiz quadrada é {}'.format(dobro, triplo, raiz))

