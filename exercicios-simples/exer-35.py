#Analisador completo de caracteristicas
numero_de_pessoas = int(input("Quantas pessoas vão participar?: "))
idades = []
homens = []
idade_homens = []
mulheres = []
idade_mulheres = []
idade_homem_velho = 0
mulheres_sem_vinte = 0
idade_iguais = False

for c in range (0, numero_de_pessoas):
    nome = input("Digite seu nome: ")
    genero = input("DIgite seu genero (feminino/masculino): ")
    idade = int (input("Digite sua idade: "))
    idades.append(idade)
    genero = genero.upper()
    if genero == "MASCULINO":
        homens.append(nome)
        idade_homens.append(idade)
        if idade_homens[-1] > idade_homem_velho:
            idade_homem_velho = idade_homens [-1]
            homem_velho = homens[-1]
        if idade_homens[-1] == idade_homem_velho:
            idade_iguais = True

    else: 
        mulheres.append(nome)
        idade_mulheres.append(idade)
        if idade_mulheres [-1] < 20:
            mulheres_sem_vinte = mulheres_sem_vinte + 1
    
soma = sum(idades)
media = soma//numero_de_pessoas
print ("A media de idade do grupo é: {}".format(media))
if idade_iguais == True:
    print ("Todos possuem a mesma idade.")
elif not homens:
    print ("Não há homens entre os candidatos.")
else:
    print ("O homem mais velho do grupo é: {}".format(homem_velho))
if not mulheres_sem_vinte:
    print ("Não há mulheres entres os candidatos.")
else:
    print ("A quantidade de mulheres com menos de 20 no grupo é: {}".format(mulheres_sem_vinte))
print("VALEU!")