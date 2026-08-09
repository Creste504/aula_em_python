#Codigo pra recrutamento para o time de natação nacional
ano_nascimento = int (input("Informe seu ano de nascimento: "))
ano_atual = int (input('Informe em que ano estamos: '))
idade = ano_atual - ano_nascimento
if idade <=9:
    print ("Você tem {} anos".format(idade))
    print ("Parabéns você faz parte do time MIRIM!")
elif idade > 9 and idade <=14:
    print ("Você tem {} anos".format(idade))
    print ("Parabéns você faz parte do time INFANTIL!")
elif idade > 14 and idade <=19:
    print ("Você tem {} anos".format(idade))
    print ("Parabéns você faz parte do time JUNIOR!")
elif idade == 20:
    print ("Você tem {} anos".format(idade))
    print ("Parabéns você faz parte do time SENIOR!")
elif idade > 20:
    print ("Você tem {} anos".format(idade))
    print ("Parabéns você faz parte do time MASTER!")
print ("VALEU!")