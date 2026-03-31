#Aumento de salario
salario = float (input('Digite quanto você ganha: '))
if salario > 1250:
    aumento = salario + (salario * 0.10)
    print ('Você recebeu um aumento, seu salario atual é {}R$'.format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print ('Você recebeu um aumento, seu salario atual é {}R$'.format(aumento))
print ('--FIM--')