#Codigo pra saber se 3 retas podem fazer um triangulo 
reta1 = float (input('Digite o valor da reta: '))
reta2 = float (input('Digite o valor da reta: '))
reta3 = float (input('Digite o valor da reta: '))
if reta1 + reta2 > reta3 or reta3 + reta2 > reta1 or reta1 + reta3 > reta2:
    print ('É possivel formar um triangulo.')
else:
    print ('Não é possivel formar um triangulo.')
print ('--FIM--')