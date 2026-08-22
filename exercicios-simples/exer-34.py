#Codigo pra ler o peso de 5 pessoas e dizer qual é o mais e menos pesado
pesos = []
nomes = []
quantidade_pessoas = int(input("Digite quantas pessoas vão fazer o teste: "))
n = quantidade_pessoas
maior_peso = 0
menor_peso = 10000000000000000000000000000000000000000000000000000000000000000000
pesos_iguais = False
for c in range (0, quantidade_pessoas):
    nome = input("Digite seu nome: ")
    peso = int(input("Digite seu peso: "))
    pesos.append(peso)
    nomes.append(nome) 
    if pesos[c] > maior_peso:
        maior_peso = pesos[c]
        pessoa_pesada = nomes [c]
    if pesos[c] < menor_peso : #or  pesos[c-1] < menor_peso :
        menor_peso = pesos[c]
        pessoa_leve = nomes [c]
    if pesos [c] == maior_peso and maior_peso == menor_peso:
        pesos_iguais = True
    else:
        pesos_iguais = False
        

if pesos_iguais == False:
     
    print ("O maior peso é de {} pesando {} kg".format(pessoa_pesada, maior_peso))

    print ("O menor peso é de {} pesando {} kg".format(pessoa_leve, menor_peso))
    
else:
    print ("vocês pesam o mesmo peso!")