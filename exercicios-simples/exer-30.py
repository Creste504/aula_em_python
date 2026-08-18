#codigo de leitura de PA (Progressão aritimetica)
primeiro_termo = int (input("Digite o primerio termo da PA: "))
razao = int (input("Digite a razao da PA: "))
n = razao * 11
for c in range (primeiro_termo, n , razao):
    print (c)