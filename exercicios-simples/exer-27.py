#Codigo pra fazer a soma dos numeros multiplos de 3 de 1 a 500
lista = []
for c in range (3, 500, 3):

    print(c)

    if c%2 == 1:
        lista.append(c)

soma_total = sum(lista)
print ("A soma de todos os numero é igual a {}".format(soma_total))
print ("VALEU!")


