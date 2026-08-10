#Codgio pra ler o preço de um produto e ver o desconto em cima dele
preco = float (input("Qual o preço do produto desejado: "))
forma_de_pagamento = int (input("Qual a forma de pagamento desejada(à vista dinheiro/cheque: 1, à vista no cartão: 2,v2x no cartão: 3, 3x ou mais no cartão: 4)? "))
if forma_de_pagamento == 1:
    print ("Você ganhou 10% de desconto")
    preco_final =  (preco - (preco * 0.1))
    print ("Você vai pagar {}R$".format(preco_final))

elif  forma_de_pagamento == 2:
    print ("Você ganhou 5% de desconto")
    preco_final =  (preco - (preco * 0.05))
    print ("Você vai pagar {}R$".format(preco_final))

elif forma_de_pagamento == 3:
    print ("Você pode dividir até duas vezes sem juros")
    preco_final =  (preco/2 )
    print ("Você vai pagar {}R$ divido em 2 meses".format(preco_final))   

elif forma_de_pagamento == 4:
    vezes_a_dividir =  int(input("Você pode dividir em 3 vezes ou mais com 20% de juros, enquantas vezes deseja dividir? "))
    preco_final =  ((preco + (preco * 0.2))/vezes_a_dividir)
    print ("Você vai pagar {}R$ em {} meses".format(preco_final, vezes_a_dividir))
print ("VALEU!")
