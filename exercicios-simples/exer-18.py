#Codigo de verificação de idade para alistamento
ano_nascimento = int (input("Informe seu ano de nascimento: "))
ano_atual = int (input('Informe em que ano estamos: '))
idade = ano_atual - ano_nascimento
if idade < 18:
    anos_que_faltam = 18 - idade
    if anos_que_faltam == 1:
        print ("Você tem apenas {} anos, ainda falta {} ano para seu alistamento.". format(idade, anos_que_faltam))
    else:
        print  ("Você tem apenas {} anos, ainda falta {} anos para seu alistamento.". format(idade, anos_que_faltam))
elif idade == 18:
    print ("Tá na hora de se alistar!")
elif idade > 18:
    anos_que_passaram = idade - 18
    if anos_que_passaram == 1:
        print ("Já passou da hora de se alistar, você tem {} anos, já se passou {} ano.". format(idade, anos_que_passaram))
    else:
        print ("Já passou da hora de se alistar, você tem {} anos, já se passou {} anos.". format(idade, anos_que_passaram))
print ("VALEU!")