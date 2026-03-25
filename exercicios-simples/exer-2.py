#Codigo pra ler um numero e destrinchar ele
numero = input ('Digite um numero de 0 a 9999: ')
unidade = numero [3]
dezena = numero [2:4]
centena = numero [1:4]
milhar = numero [0:4]
print ("""Unidade: {}
Dezena : {} 
Centena: {} 
milhar : {}""".format(unidade, dezena, centena, milhar))