#Codigo pra ler uma tabuada com o while

while True:
    resposta_user = input("Deseja ver a tabuada de algum numero?(N/S): ").upper()
    contador = 1
    print()
    if resposta_user != "N":
        valor_tabuada = int(input("Digite o numero que você deseja ver a tabuada: "))

        print ()

        if valor_tabuada < 0:

            break

        while contador != 11:

            multiplicacao = valor_tabuada * contador

            print ("{} * {} = {}".format(valor_tabuada, contador, multiplicacao))

            contador += 1
    else:
        break
    print ()
    
print ("VALEU!")