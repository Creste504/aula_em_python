#Codigo pra ler uma tabuada com o for
valor_tabuada = int(input("Digite o numero que você deseja ver a tabuada: "))
for c in range(0,11):
    multiplicacao = valor_tabuada * c
    print ("{} * {} = {}".format(valor_tabuada, c, multiplicacao))
print ("VALEU!")