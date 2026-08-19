#Codigo de leitura de numero inteiro e dizer se é primo ou não 
lista = []
numero = int(input("digite um número: ")) 
for divisor in range (2 , numero):
    restos = numero % divisor
    lista.append(restos)
if all(valor >= 1 for valor in lista):
    print ("Parabéns, {} é um número primo!".format(numero))
else:
    while True:
        lista = []
        
        for divisor in range (2 , numero):
            restos = numero % divisor
            lista.append(restos)
       
        if all(valor >= 1 for valor in lista):
            print ("Parabéns, {} é um número primo!".format(numero))
            break
        else:  
            print ("O número que você digitou não é primo!")
            numero = int(input("digite um número: ")) 

print("VALEU!")