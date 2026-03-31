#Codigo pra ler qual entre entre 3 numeros é o maior e o menor
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))
if n1 > n2 and n1 > n3:
    print ('{} é o maior numero'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print ('{} é o maior numero'.format(n2))
    else:
        if n3 > n1 and n3 > n2:
            print ('{} é o maior numero'.format(n3))
if n1 < n2 and n1 < n3:
    print ('{} é o menor numero'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print ('{} é o menor numero'.format(n2))
    else: 
        if n3 < n1 and n3 < n2:
            print ('{} é o menor numero'.format(n3))
print ('--FIM--')