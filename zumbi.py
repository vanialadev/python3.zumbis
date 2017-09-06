x = 'abacate'
y = "MacDonald's"
z = '''
<html>
    <head>
        <title>Teste</title>
    </head>
    <body>
        <p>Testando</p>
    </body>
</html>
'''

print(x)
print(y)
print(z)

x = '0123456789'
print(x[0:2])
print(x[1:2])
print(x[2:4])
print(x[0:5])
print(x[1:8])
print(x[0:11])
print(x[:2])
print(x[4:])
print(x[4:-1])  # -1 último
print(x[-4:-1])  # -2 antipenúltimo
print(x[-4:-2])
print(x[:])

texto = 'batatinha quando nasce'
print(texto[::2])  # pulando de 2 em 2
print(texto[::-1])  # invertando a str

palavra = input('Qual a palavra? ')
nova_string = palavra[::-1]
# if palavra = palavra[::-1]
if palavra == nova_string:
    print('É palíndrome')
else:
    print('Não é palíndrome')

texto = 'Alô Mundo'
texto = '@' + texto[1:]
print(texto)
