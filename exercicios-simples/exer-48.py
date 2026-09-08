#Analisador completo de caracteristicas com while
idades = []
homens = []
mulheres = []
idade_mulheres = []
idade_iguais = False
pessoa_com_mais_de_18 = 0
mulheres_sem_vinte = 0

while True:
    nome = input("Digite seu nome: ")
    genero = input("Digite seu genero (F/M): ").upper()
    idade = int (input("Digite sua idade: "))
    idades.append(idade)

    if idade > 18:
        pessoa_com_mais_de_18 += 1

    if genero == "M":
        homens.append(nome)

    else: 
        mulheres.append(nome)
        idade_mulheres.append(idade)
        if idade_mulheres [-1] < 20:
            mulheres_sem_vinte += 1

    resposta_user = input ("Deseja continuar?(N/S): ").upper()

    if resposta_user == "N":
        break

qtd_homens = len(homens)


if pessoa_com_mais_de_18 == 0:
    print ("Não há pessoas com mais de 18 anos entres os candidatos.")
else:
    print (f"A quantidade de  pessoas com mais de 18 anos no grupo é {pessoa_com_mais_de_18}.")

if qtd_homens == 0:
    print ("Não há homens entres os candidatos.")
else:
    print (f"A quantidade de homens no grupo é {qtd_homens}.")

if mulheres_sem_vinte == 0:
    print ("Não há mulheres com menos de 20 anos entres os candidatos.")
else:
    print ("A quantidade de mulheres com menos de 20 no grupo é: {}".format(mulheres_sem_vinte))
print("VALEU!")