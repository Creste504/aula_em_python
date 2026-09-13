#Caixa eletronico com while

#50, 20, 10 e 1 

while True:
    while True:

        print ("===================================")
        print ("             BANCO DEV             ")
        print ("===================================")
        valor_sacado = int(input("Quanto deseja sacar?: "))

        qtd_notas50 = valor_sacado // 50
        novo_valor = (valor_sacado) - (qtd_notas50 * 50)

        qtd_notas20 = novo_valor // 20
        novo_valor = (novo_valor) - (qtd_notas20 * 20 )

        qtd_notas10 = novo_valor // 10
        novo_valor = (novo_valor) - (qtd_notas10 * 10)

        qtd_notas1 = novo_valor // 1 
       

        if qtd_notas50 != 0:
            print (f"Total de {qtd_notas50} cédulas de R$50 ")

        if qtd_notas20 != 0:
            print (f"Total de {qtd_notas20} cédulas de R$20 ")
        
        if qtd_notas10 != 0:
            print (f"Total de {qtd_notas10} cédulas de R$10 ")

        if qtd_notas1 != 0:
            print (f"Total de {qtd_notas1} cédulas de R$1 ")


        break
    print ()
    resposta_user = input ("Deseja continuar (S/N)?: ").upper()
    if resposta_user == "N":
        break
print ("VALEU!")

