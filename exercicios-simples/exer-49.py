#Codigo de leitura de produtos e preços

lista_de_produtos = []
produto_barato = 9999999999999999999999999999999999999999999
nome_produto_barato = " "
produtos_que_mais_de_mil = 0

while True:
    nome_produto = input("Qual o nome do produto que deseja comprar: ")
    valor_produto = int(input("Qual o valor do produto que deseja comprar: "))
    lista_de_produtos.append(valor_produto)

    if lista_de_produtos[-1] < produto_barato:
        produto_barato = lista_de_produtos [-1]
        nome_produto_barato = nome_produto

    if lista_de_produtos [-1] > 1000:
         produtos_que_mais_de_mil += 1

    resposta_user = input("Deseja adicionar mais algo ao carrinho?(S/N): ").upper()
    if resposta_user == "N":
        break


total_gasto = sum(lista_de_produtos)
print (f"Foi gasto um total de {total_gasto} R$.")

if produtos_que_mais_de_mil == 0:
    print ("Não existem produtos que valem mais que 1000 R$.")
elif produtos_que_mais_de_mil == 1:
    print ("Existe um produto que vale mais que 1000 R$.")
else:
    print (f"Existem {produto_barato} produtos que valem mais que 1000 R$.")

print (f"Este foi o produto mais barato de seu carrinho: {nome_produto_barato}.")

print ("VALEU!")