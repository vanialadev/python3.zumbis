a = int(input('Digite número 1:\n'))
b = int(input('Digite número 2:\n'))
print(a + b)

metros = int(input('Digite o valor em metros:\n'))
milimetros = metros * 10000
print(milimetros)

dias = int(input('Digite o número de dias\n'))
horas = int(input('Digite o número de horas:\n'))
minutos = int(input('Digite o número de minutos:\n'))
segundos = int(input('Digite o número de segundos:\n'))
segundos_total = segundos + (minutos * 60) + (horas * 3600) + (dias * 3600 * 24)
print('O total de segundos foi %d' % segundos_total)

salario = float(input('Valor do salário?\n'))
porcentagem = int(input('Porcentagem do aumento?\n'))
aumento = (salario * porcentagem) / 100
salario += aumento
print('O valor do aumento foi de %2.f e o salário ficou no valor de %2.f' % (aumento, salario))

valor = float(input('Valor da mercadoria?\n'))
porcentagem = int(input('Percentual de desconto?\n'))
desconto = (valor * porcentagem) / 100
valor -= desconto
print('O valor do desconto é de %2.f e a mercadoria vai sair por %2.f' % (desconto, valor))

distancia = float(input('Qual a distância em km?\n'))
velocidade = float(input('Qual a velocidade em km\h?\n'))
tempo_hora = distancia/velocidade
print('Tempo aproximado em horas: %.1f' %tempo_hora)

celcius = int(input('Temperatura em celcius\n'))
fahrenheit = 9 * celcius / 5 + 32
print(fahrenheit)

fahrenheit = int(input('Temperatura em fahrenheit\n'))
celsius = (fahrenheit - 32) * 5 / 9
print(celsius)

km = int(input('Quantos km?\n'))
dias = int(input('Quantos dias\n'))
valor = dias * 60 + km * 0.15
print('Valor a pagar é %.2f' % valor)

cigarro_dia = int(input('Quantos por dia?\n'))
ano = int(input('Quantos anos\n'))
todos = cigarro_dia * ano * 365
minutos = (todos * 10)
dias = minutos / 1440
print('Perdeu', dias, 'dias')

a = str(2 ** 1000000)
b = len(a)
print(b)
