#codigo pra ler a media de um estudante 
nota_1 = float(input('Digite a primeria nota do aluno: '))
nota_2 = float(input('Digite a segunda nota do aluno: '))
media = float (nota_1 + nota_2)/2
if media < 5.0:
    print ("Sua nota foi {}".format(media))
    print ("REPROVADO")
elif media == 5.0 or media <= 6.9:
    print ("Sua nota foi {}".format(media))
    print ("RECUPERAÇÃO")
elif media >= 7.0:
    print ("Sua nota foi {}".format(media))
    print("APROVADO")