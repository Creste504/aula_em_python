#Codigo de custo de viagem
kmRodados = float(input('Quantos kms a sua viagem terá? '))
if kmRodados < 200:
    preco = kmRodados * 0.5
    print ('Sua passagem custou {}R$'.format(preco))
else:
    preco = kmRodados * 0.45
    print ('Sua passagem custou {}R$'.format(preco))
print('--FIM--')