# um programa de leitura de dois valores e vai mostra um menu com: soma, multiplicação, maior, novos numeros e fechar o programa
import math
import time
maior = 0
valores = []
opcoes = 0
numero = int(input("Digite um numero inteiro: "))
valores.append(numero)
numero = int(input("Digite um numero inteiro: "))
valores.append(numero)
while opcoes != 5:
    print ("""
Aqui está os numeros que você escreveu até agora:""",valores
)
    opcoes = int(input("""----------------------
[1]Somar
[2]Multiplicar 
[3]Maior
[4]Novos números
[5]Sair do programa 
---------------------
Selecione uma das opções: """))

    if opcoes == 1:
        soma = sum(valores)
        print ("" \
        "Essa foi a soma dos valores: ",soma)
    if opcoes == 2:
        multiplicacao = math.prod(valores)
        print ("" \
        "Esse foi o resultado da multiplicação dos valores: ",multiplicacao)
    if opcoes == 3:
        for c in range (0, len(valores)):
            if valores [c] > maior:
                maior = valores [c]
        print ("O maior é ", maior)
    if opcoes == 4:
        numero = int(input("Adicione um novo numero inteiro: "))
        valores.append(numero)
        
    if opcoes == 5:
        print ("Fim do programa")
        break
        time.sleep (2)     
    time.sleep (2)
print("VALEU!")