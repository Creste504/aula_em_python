#Analise do ano de nascimento de 7 pessoas e quantas faltam atingir a maioridade 
ano_atual =  int (input("Em que ano estamos?: "))
maiores = []
menores = []

for c in range (1, 8):
    nome = input("Digite seu nome: ")
    ano_de_nascimento = int(input("Digite seu ano de nascimento: "))

    idade = ano_atual - ano_de_nascimento

    if idade < 18:
        menores.append(nome)
    else:
        maiores.append(nome)

numero_de_menores = len(menores)
numero_de_maiores = len(maiores)


if numero_de_menores >= 2:
    print ("Um total de {} pessoas ainda não atingiram a maioridade!".format(numero_de_menores))
elif numero_de_menores == 1:
    print ("Apenas {} pessoa ainda não atingiu a maioridade!".format(numero_de_menores))
else:
    print ("Todos já são de atingiram a maioridade")


if numero_de_menores >= 2:
    print ("Um total de {} pessoas já atingiram a maioridade!".format(numero_de_maiores))
elif numero_de_menores == 1:
    print ("Apenas {} pessoa já atingiu a maioridade!".format(numero_de_menores))
else:
    print ("Todos já são de atingiram a maioridade")
