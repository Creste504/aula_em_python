#Ler ano bissexto
ano = int(input('Digite um ano aleatorio: '))
if ano%100 == 0 and ano%400 == 0:
    print ('O ano é bissexto')
else:
    if ano%100 != 0 and ano%4 == 0:
        print ('O ano é bissexto')
    else:
        print ('O ano não é bissexto')
print ('--FIM--')
