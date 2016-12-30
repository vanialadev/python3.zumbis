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

ano = int(input('Informe o ano\n'))
if ano % 4 == 0 and ano % 100 != 0:
    print('é bissexto')
elif ano % 400 == 0:
    print('é bissexto')
else:
    print('não é bissexto')

peso = int(input('peso\n'))
excesso, multa = 0, 0
if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso
print('Excesso: %d, Multa: %d' % (excesso, multa))

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

ganho_hora = int(input('Quanto você ganha por hora?\n'))
hora_mes = int(input('Número de horas por mês?\n'))
salario_bruto = ganho_hora * hora_mes
imposto = salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sindicato = salario_bruto * 5 / 100
salario_liquido = salario_bruto - imposto - inss - sindicato
print('Salário Bruto %.2f,Imposto de Renda %.2f, INSS %.2f, Sindicato %.2f, Salário Líquido = %.2f'
      % (salario_bruto,imposto, inss,sindicato, salario_liquido))

metros = int(input('Tamanho em m2 a ser pintado: '))
litros = metros / 3
latas = litros / 18
if litros % 18 == 0:
    latas = latas
else:
    latas += 1
valor_total = 80 * int(latas)
print('Latas a serem compradas %d Valor total %.2f' % (latas, valor_total))
