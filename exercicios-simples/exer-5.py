#Codigo de quantas vezes aparece a letra "A" e quando ela apareceu primeiro e por ultimo
frase = input ('Digite uma frase aleatorio: ')
quantosTem = frase.upper().count('A')
primeiro = frase.upper().find('A')
ultimo = frase.upper().rfind('A')
print ('A letra "A" aparece {} vezes'.format(quantosTem))
print ('O primeiro aparece na posição {}'.format(primeiro))
print ('O ultimo aparece na posição {}'.format(ultimo))