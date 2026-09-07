#Jogo de pedra papel e tesoura com while
import random 
import time
vitoria = 0
empate = 0
while  True:
    escolha = input("Escolha entre pedra, papel ou tesoura: ").upper()
    chutes = ["PEDRA", "PAPEL", "TESOURA"]
    sorteado = random.choice(chutes)
    if escolha == sorteado:
        print("Vamos arrastaaar!")
        time.sleep(2)
        print ("Você: {} X {} :Maquina".format(escolha,sorteado))
        time.sleep(2)
        print ("Empatou!")
        empate += 1
    elif escolha == "PEDRA" and sorteado == "TESOURA" or escolha == "TESOURA" and sorteado == "PAPEL" or escolha == "PAPEL" and sorteado == "PEDRA":
        print("Vamos arrastaaar!")
        time.sleep(2)
        print ("Você: {} X {} :Maquina".format(escolha,sorteado))
        time.sleep(2)
        print ("Você venceu!")
        vitoria += 1
    elif  sorteado == "PEDRA" and escolha == "TESOURA" or sorteado == "TESOURA" and escolha == "PAPEL" or sorteado == "PAPEL" and escolha == "PEDRA":
        print("Vamos arrastaaar!")
        time.sleep(2)
        print ("Você: {} X {} :Maquina".format(escolha,sorteado))
        time.sleep(2)
        print ("Você perdeu!")
        break
if empate == 1:
    print (f"Você empatou {empate} vez")
else:
    print (f"Você empatou {empate} vezes")
if vitoria == 1:
    print (f"Você ganhou {vitoria} vez")
else:
    print (f"Você ganhou {vitoria} vezes")
print ("VALEU!")