# Codigo de leitura de numeros variados
contador = 0
resposta_do_user = ("S")
lista = []
maior_numero = 0
menor_numero = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
while resposta_do_user != "N":

    if contador <= 2:
        numero = int(input("Digite um numero inteiro: "))
        lista.append(numero)
    
        if lista[-1] > maior_numero:
            maior_numero = lista[-1]

        if lista[-1] < menor_numero:
             menor_numero = lista[-1]
            
    if contador >= 2:
        while resposta_do_user != "N":

            resposta_do_user = input("Deseja continuar (N/S)?: ").upper()

            if resposta_do_user != "N":


                numeros_extras = int(input("Deseja digitar mais quantos numeros?: "))

                sub_contador = 0    

                while sub_contador != numeros_extras:

                    numero = int(input("Digite um numero inteiro: "))
                    lista.append(numero)
                        
                    if lista[-1] > maior_numero:
                       maior_numero = lista[-1]

                    if lista[-1] < menor_numero:
                        menor_numero = lista[-1]
                               
                    contador += 1
                    sub_contador += 1

    media = (sum(lista)) / len(lista)
    contador += 1
    
print ("A media é igual a: {}".format(media))
print ("O maior numero foi: {}".format(maior_numero))
print ("O menor numero foi: {}".format(menor_numero))    
print("VALEU!")