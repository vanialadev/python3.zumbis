a = int(input('Primeiro valor: \n'))
b = int(input('Segundo valor: \n'))

if a > b:
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior')

idade = int(input('Digite a idade do seu carro: \n'))
if idade <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')

velocidade = int(input('Qual a velocidade do carro?\n'))
if velocidade > 110:
    print('Usuário foi multado!')
    multa = 5 * (velocidade - 110)
    print('Sua multa foi de %.2f reais' % multa)

seus_minutos = int(input('Quantos minutos você gastou?\n'))
if seus_minutos < 200:
    valor = 0.2
elif seus_minutos < 400:
    valor = 0.18
elif seus_minutos < 800:
    valor = 0.15
else:
    valor = 0.08
total = valor * seus_minutos
print('Você pagará %.2f reais' % total)

x = 1
while x <= 3:
    print(x)
    x += 1

x = 1
numero = int(input('Até que número você quer imprimir?\n'))
while x <= numero:
    print(x)
    x += 1

numero = int(input('Até que número você quer imprimir?\n'))
x = 0
while x <= numero:
    if x % 2 == 0:
        print(x)
    x += 1

numero = int(input('Até que número você quer imprimir?\n'))
x = 0
while x <= numero:
    print(x)
    x += 2

numero = int(input('Até que número você quer imprimir?\n'))
x = 1
while x <= numero:
    print(x)
    x += 2

contador = 1
while contador <= 10:
    print(3 * contador)
    contador += 1

contator = 1
soma = 0
while contator <= 10:
    x = int(input('Digite o %d número\n' % contator))
    soma += x
    contator += 1
print('Soma = %d' % soma)

contator = 1
soma = 0
while contator <= 10:
    x = int(input('Digite o %d número\n' % contator))
    soma += x
    contator += 1
media = soma / contator
print('Média igual a %.2f' % media)

fat = 1
contador = 1
while contador <= 10:
    fat *= contador
    contador += 1
print('Fatorial de 10 é %d ' % fat)

fat = 1
contador = 1
x = int(input('Até que número você quer o fatorial?\n'))
while contador <= x:
    fat *= contador
    contador += 1
print('Fatorial de %d é %d ' % (x, fat))

soma = 0
while True:
    x = int(input('Número pra somar\n'))
    if x == 0:
        break
    soma += x
print('Soma total de %d ' % soma)

soma = 0
x = 1
while x != 0:
    x = int(input('Número pra somar (0 sai)\n'))
    soma += x
print('Soma total de %d ' % soma)

tabuada = 1
while tabuada <= 10:
    numero = 1
    print('Tabuada de %d' % tabuada)
    while numero <= 10:
        total = tabuada * numero
        print('%d x %d = %d' % (tabuada, numero, total))
        numero += 1
    tabuada += 1

