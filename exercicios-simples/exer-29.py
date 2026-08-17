#Codigo pra ler 6 numeros inteiros e somar apenas o pares
lista_pares = []
lista_total = []
for c in range (0, 6):
    numero_escolhido = int(input("Digite um numero inteiro: "))
    if numero_escolhido % 2 == 0:
        lista_pares.append(numero_escolhido)
    lista_total.append(numero_escolhido)
soma = sum(lista_pares)
print ("Você digitou esses numeros: {}".format(lista_total))
print ("E a soma dos numeros pares desse conjunto é: {} ".format(soma))
