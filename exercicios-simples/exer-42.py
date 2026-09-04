# Codigo de leitura de uma sequência de fibonnaci 
numero1 = int(input("Digite um numero inteiro para sua sequência de fibonacci: "))
numero0 = 0
fibonacci = 0
elementos = int(input("Quantos elementos você deseja ver?: "))
contador = 0
print (numero0)
print (numero1)
while contador != (elementos - 2):
    fibonacci = numero0 + numero1
    print (fibonacci)
    if contador >= 2:
        numero1 = numero0
    numero0 = fibonacci
    contador += 1
print("VALEU!")
