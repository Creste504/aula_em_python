#Codigo para comparar dois numeros inteiros
primeiro_valor = int (input('Digite o primeiro numero inteiro: '))
segundo_valor = int (input('Digite o segundo numero inteiro: '))
if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior.')
elif primeiro_valor < segundo_valor:
    print('O segundo valor é maior.')
elif primeiro_valor == segundo_valor:
    print ('Os dois valores são iguais.')