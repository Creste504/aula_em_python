#programa de leitura de fatorial de um numero
numero = int(input('Digite um numero inteiro: '))
contador = 1
fatorial = numero
while contador != numero:
    fatorial = (fatorial) * (numero - contador)
    contador += 1
print ("O fatorial de {} é igual a {}".format(numero, fatorial))
print ("VALEU!")