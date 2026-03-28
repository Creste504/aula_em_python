#Codigo pra pegar o primerio e ultimo nome de alguem 
nome = input('Digite seu nome completo: ').strip()
partes = nome.split()
primeiroNome = partes[0]
ultimoNome = partes[-1]
print ('Primeiro nome: {}'.format(primeiroNome))
print ('Ultimo nome: {}'.format(ultimoNome))