import re
frase = (input('Ingrese la frase: ')).lower().split().replace(",",".",":",":")
palabra = (str(input('Ingrese la palabra a contar: '))).lower()
cant = 0
for i in frase:
    if i == palabra:
        cant += 1

print(cant)