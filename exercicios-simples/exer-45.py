# Codigo de leitura de varios numeros inteiros e dizer a soma total deles com break
resposta_correta = 0
lista = []
while True:
    resposta_correta = int(input("Digite um numero inteiro: "))
    if resposta_correta == 999:
        break
    lista.append(resposta_correta)
soma = sum(lista)
numero_de_chutes = len(lista)
print ("A soma total dos numeros que você digitou foi {}".format(soma))
print ("O numero total de chutes que você fez foi {}".format(numero_de_chutes))
print("VALEU!")