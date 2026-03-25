#Colocar o nome da cidade e ver se tem santo ou não no nome
cidade = input ('Escreva o nome da sua cidade: ')
temSanto = cidade.split()[0].upper().find('SANTO')
print (temSanto)