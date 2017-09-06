# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.
nota = -2
while nota > 11 or nota < 0:
    nota = float(input('Informe uma nota de 0 a 10: '))


# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.
nome = 'a'
senha = 'a'
while nome == senha:
    nome = input("Informe seu nome: \n")
    senha = input('Informe sua senha: \n')
    if nome != senha:
        break
    print('senha não pode ser igual a nome')


# 3. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e
#  que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento
pop_a = 80000
tx_a  = 0.03
pop_b = 200000
tx_b = 0.015
anos = 0
while pop_b > pop_a:
    pop_a += pop_a * tx_a
    pop_b += pop_b * tx_b
    print('pop a: %d' % pop_a)
    print('pop b: %d' % pop_b)
    anos += 1

print('Total de %d anos' % anos)


# 4. A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os
#  dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo
# que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
f1, f2 = 1, 1
numero = int(input('Informe um numero: '))
# cont = 3
# if numero == 1 or numero == 2:
#     print('Fibo é %d' % f2)
# else:
#     while cont <= numero:
        # fibo = f2 + f1
        # f1 = f2
        # f2 = f2 + f1
        # print('Fibo de %d é %d' % (cont,fibo))
        # cont += 1
# outra maneira de se fazer
cont = 1
while cont <= numero - 2:
    f1, f2 = f2, f2 + f1
    cont += 1
print('Fibo de %d é %d' % (numero, f2))


# 5. Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.
num1 = int(input('num1: '))
num2 = int(input('num2: '))

while num1 % num2 != 0:
    num1, num2 = num2,  num1 % num2

print('MDC é %d' % num2)
