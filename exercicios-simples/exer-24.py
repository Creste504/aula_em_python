#Jogo de pedra papel e tesoura 
import random 
import time
escolha = input("Escolha entre pedra, papel ou tesoura: ")
chutes = ["PEDRA", "PAPEL", "TESOURA"]
sorteado = random.choice(chutes)
escolha = escolha.upper()
if escolha == sorteado:
    print("Vamos arrastaaar!")
    time.sleep(2)
    print ("Você: {} X {} :Maquina".format(escolha,sorteado))
    time.sleep(2)
    print ("Empatou!")
elif escolha == "PEDRA" and sorteado == "TESOURA" or escolha == "TESOURA" and sorteado == "PAPEL" or escolha == "PAPEL" and sorteado == "PEDRA":
    print("Vamos arrastaaar!")
    time.sleep(2)
    print ("Você: {} X {} :Maquina".format(escolha,sorteado))
    time.sleep(2)
    print ("Você venceu!")
elif  sorteado == "PEDRA" and escolha == "TESOURA" or sorteado == "TESOURA" and escolha == "PAPEL" or sorteado == "PAPEL" and escolha == "PEDRA":
    print("Vamos arrastaaar!")
    time.sleep(2)
    print ("Você: {} X {} :Maquina".format(escolha,sorteado))
    time.sleep(2)
    print ("Você perdeu!")
print("VALEU!")