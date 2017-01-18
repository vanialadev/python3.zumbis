edificio = ['Família Souza', 'Família Brito', 'Família Almeida', 'Família Rodrigues']
print(edificio[0])
print(edificio[1])
print(edificio[2])
print(edificio[3])

my_array = [7, '24', 'Fish', 1.45]
print(type(my_array[0]))
print(type(my_array[1]))
print(type(my_array[2]))
print(type(my_array[3]))
print(type(my_array))

my_words = ['Dudes', 'and']
my_words.append('Betty')
print(my_words)

lista = []

notas = [7.5, 9, 8.3]
print(notas[0])
notas[0] = 10
print(notas[0])

notas = [10, 9.3, 8.7, 8.2, 9]
contador = 0
soma = 0
while contador < len(notas):
    soma += notas[contador]
    contador += 1
media = soma/5
print('Média é %.2f' % media)

vetor = []
x = 0
while x < 5:
    numero = int(input('Informe um número '))
    vetor.append(numero)
    x += 1
print('Vetor lido: ', vetor)

vetor = []
novo_vetor = []
x = 0
while x < 10:
    numero = int(input('Informe um número '))
    vetor.append(numero)
    x += 1
x = len(vetor) - 1
while x >= 0:
    novo_vetor.append(vetor[x])
    x -= 1
print('Vetor lido: ', novo_vetor)

vetor = []
x = 0
while x < 10:
    numero = int(input('Informe um número '))
    vetor.append(numero)
    x += 1
x = 9
while x >= 0:
    print(vetor[x])
    x -= 1

notas = []
contador = 0
soma = 0
while contador < 4:
    nota = float(input('Informe a nota '))
    notas.append(nota)
    soma += nota
    contador += 1
media = soma/4
print('Notas: ', notas)
print('Média é %.2f' % media)

letras = []
n = 0
while n < 5:
    caractere = input('Informe o caractere ')
    letras.append(caractere)
    n += 1
print(letras)
x = 0
total = len(letras)
while x < len(letras):
    if letras[x] == 'a' or letras[x] == 'a' or letras[x] == 'e' or letras[x] == 'i' or letras[x] == 'o' or letras[x] == 'u':
        total -= 1
    x += 1
print('Foram lidas %d consoantes' % total)

letras = []
n = 0
while n < 5:
    caractere = input('Informe o caractere ')
    letras.append(caractere)
    n += 1
print(letras)
x = 0
total = 0
while x < len(letras):
    if letras[x] not in 'aeiou':
        total += 1
    x += 1
print('Foram lidas %d consoantes' % total)
