# 1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um
# triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
a = int(input('Lado 1\n'))
b = int(input('Lado 2\n'))
c = int(input('Lado 3\n'))
if a > b + c or b > a + c or c > a + b:
    print('Não pode ser um triângulo')
elif a == b and b == c:
    print('equilátero')
elif a == b or b == c or c == a:
    print('isósceles')
else:
    print('escaleno')


# 2. Determine se um ano é bissexto. Verifique no Google como fazer isso...
ano = int(input('Informe o ano\n'))
if ano % 4 == 0 and ano % 100 != 0:
    print('é bissexto')
elif ano % 400 == 0:
    print('é bissexto')
else:
    print('não é bissexto')


# 3. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
# que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na
# variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.
peso = int(input('peso\n'))
excesso, multa = 0, 0
if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso
print('Excesso: %d, Multa: %d' % (excesso, multa))


# 4. Faça um Programa que leia três números e mostre o maior deles.
a = int(input('a\n'))
b = int(input('b\n'))
c = int(input('c\n'))
if a >= b and a >= c:
    maior = a
elif b >= c:
    maior = b
else:
    maior = c
print('Maior número é %d' % maior)


# 5. Faça um Programa que leia três números e mostre o maior e o menor deles.
a = int(input('a\n'))
b = int(input('b\n'))
c = int(input('c\n'))
if a >= b and a >= c:
    maior = a
elif b >= c:
    maior = b
else:
    maior = c
if a <= b and a <= c:
    menor = a
elif b <= c:
    menor = b
else:
    menor = c
print('Maior número é %d, Menor número é %d' % (maior, menor))


# 6. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e
# mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
# quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
# descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$
ganho_hora = int(input('Quanto você ganha por hora?\n'))
hora_mes = int(input('Número de horas por mês?\n'))
salario_bruto = ganho_hora * hora_mes
imposto = salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sindicato = salario_bruto * 5 / 100
salario_liquido = salario_bruto - imposto - inss - sindicato
print('Salário Bruto %.2f,Imposto de Renda %.2f, INSS %.2f, Sindicato %.2f, Salário Líquido = %.2f'
      % (salario_bruto,imposto, inss,sindicato, salario_liquido))


# 7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
# pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
# preço total. Obs. : somente são vendidos um número inteiro de latas.
metros = int(input('Tamanho em m2 a ser pintado: '))
litros = metros / 3
latas = litros / 18
if litros % 18 == 0:
    latas = latas
else:
    latas += 1
valor_total = 80 * int(latas)
print('Latas a serem compradas %d Valor total %.2f' % (latas, valor_total))
