#Codigo pra ler um numero e destrinchar ele
numero = input ('Digite um numero de 0 a 9999: ')
indice = (len(numero))
if indice == 1:
    unidade = numero [-1]
elif indice == 2:
    unidade = numero [-1]
    dezena = numero [0:2]
elif indice == 3:
    unidade = numero [-1]
    dezena = numero [1:3]
    centena = numero [0:3]
elif indice == 4:
    unidade = numero [-1]
    dezena = numero [2:4]
    centena = numero [1:4]
    milhar = numero [0:4]
if indice == 1:
    print ("Unidade: {}".format(unidade))
elif indice == 2:
    print ("""Unidade: {}
Dezena : {} """.format(unidade, dezena))
elif indice == 3:
    print ("""Unidade: {}
Dezena : {} 
Centena: {} """.format(unidade, dezena, centena))
elif indice == 4:       
    print ("""Unidade: {}
Dezena : {} 
Centena: {} 
milhar : {}""".format(unidade, dezena, centena, milhar))