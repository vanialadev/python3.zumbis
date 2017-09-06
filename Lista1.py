# 1) Faça um programa que peça dois números inteiros e imprima a soma desses dois números
a = int(input('Digite número 1:\n'))
b = int(input('Digite número 2:\n'))
print(a + b)


# 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
metros = int(input('Digite o valor em metros:\n'))
milimetros = metros * 10000
print(milimetros)


# 3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em
# segundos.
dias = int(input('Digite o número de dias\n'))
horas = int(input('Digite o número de horas:\n'))
minutos = int(input('Digite o número de minutos:\n'))
segundos = int(input('Digite o número de segundos:\n'))
segundos_total = segundos + (minutos * 60) + (horas * 3600) + (dias * 3600 * 24)
print('O total de segundos foi %d' % segundos_total)


# 4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do
# aumento. Exiba o valor do aumento e do novo salário.
salario = float(input('Valor do salário?\n'))
porcentagem = int(input('Porcentagem do aumento?\n'))
aumento = (salario * porcentagem) / 100
salario += aumento
print('O valor do aumento foi de %2.f e o salário ficou no valor de %2.f' % (aumento, salario))


# 5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
valor = float(input('Valor da mercadoria?\n'))
porcentagem = int(input('Percentual de desconto?\n'))
desconto = (valor * porcentagem) / 100
valor -= desconto
print('O valor do desconto é de %2.f e a mercadoria vai sair por %2.f' % (desconto, valor))


# 6) Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input('Qual a distância em km?\n'))
velocidade = float(input('Qual a velocidade em km\h?\n'))
tempo_hora = distancia/velocidade
print('Tempo aproximado em horas: %.1f' %tempo_hora)


# 7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32
celcius = int(input('Temperatura em celcius\n'))
fahrenheit = 9 * celcius / 5 + 32
print(fahrenheit)


# 8) Faça agora o contrário, de Fahrenheit para Celsius.
fahrenheit = int(input('Temperatura em fahrenheit\n'))
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)


# 9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a
# quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,
# 00 por dia e R$ 0,15 por km rodado.
km = int(input('Quantos km?\n'))
dias = int(input('Quantos dias\n'))
valor = dias * 60 + km * 0.15
print('Valor a pagar é %.2f' % valor)

# 10) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros
# fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
# calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
cigarro_dia = int(input('Quantos por dia?\n'))
ano = int(input('Quantos anos\n'))
todos = cigarro_dia * ano * 365
minutos = (todos * 10)
dias = minutos / 1440
print('Perdeu', dias, 'dias')


# 11) Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.
a = str(2 ** 1000000)
b = len(a)
print(b)
