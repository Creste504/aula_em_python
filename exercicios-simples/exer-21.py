#Codigo pra ler a possibilidade de formar triangulos e se são equilateros, isoceles ou escalenos
reta1 = float (input('Digite o valor da reta: '))
reta2 = float (input('Digite o valor da reta: '))
reta3 = float (input('Digite o valor da reta: '))
if reta1 + reta2 > reta3 and reta3 + reta2 > reta1 and reta1 + reta3 > reta2:
    print ('É possivel formar um triangulo.')
    if reta1 == reta2 == reta3:
        print ("É um triangulo equilatero!")

    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta3 == reta2 != reta1:
        print ("É um trinagulo isoceles!")

    elif reta1 != reta2 != reta3:
        print ("É um triangulo escaleno!")
else:
    print ('Não é possivel formar um triangulo.')
print ("VALEU!")