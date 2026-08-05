#programa pra calcular possibilidade de emprestimos bancarios 
valor_casa = float (input ('Qual o valor do emprestimo da casa? '))
salario_comprador = float (input ('Qual o valor do seu salario? '))
anos_a_pagar = int (input ('Em quantos anos você vai pagar? '))
meses = anos_a_pagar * 12
taxa_de_juros = float (0.0764)
valor_prestacao = (valor_casa * taxa_de_juros) / (1 - (1 + taxa_de_juros) ** (-meses))
valor_prestacao = round(valor_prestacao, 2)
print ('O valor da prestação será ', valor_prestacao, 'R$')
if valor_prestacao <= 0.3 * salario_comprador:
    print ('Emprestimo aprovado')
else:
    print ('Emprestimo negado')
print ('Valeu')