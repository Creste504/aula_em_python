#Codigo de analise de nomes
nome = ('Cristhian Matheus Freitas da Silva')
#input('Digite o seu nome completo')
#Deica maisculo
maiusc = nome.upper()
#Deixa minusculo
minusc = nome.lower()
#Essa variavel vai substituir os espaços em branco e juntar todos os nomes e depois fazer a contagem dos caracteres
contg = len(nome.replace(' ', ''))
#Essa variavel vai ler o primeiro nome q eu colocar e contar o numero de caracteres contidos nela
primeiroNome = len(nome.split()[0])
print ('Seu nome em letras maiusculas fica: {}'.format(maiusc))
print ('Seu nome em letras minusculas fica: {}'.format(minusc))
print ('O total de caracteres do seu nome é: {}'.format(contg))
print ('O numero de caracteresd do seu primeiro nome é: {}'.format(primeiroNome))