#codigo de leitura de PA (Progressão aritimetica) com while
primeiro_termo = int (input("Digite o primerio termo da PA: "))
razao = int (input("Digite a razao da PA: "))
n = 1
contador = 0
ultimo_numero = 0
print ("A sua progressão aritimetica é a seguinte: ")
while contador != 10:
    ultimo_numero = (primeiro_termo) + (n - 1) * (razao)
    n += 1
    print (ultimo_numero)
    contador += 1
print ("VALEU!")