#Jogo de impar ou par com while
import random 
import time
vitoria = 0
while  True:
    escolha = input("Escolha entre impar ou par: ").upper()
    
    if escolha == "IMPAR":
        maquina = "PAR"
    else:
        maquina = "IMPAR"

    escolha_number = int(input("Escolha um numero de 0 a 10: "))
    sorteado = random.randint (0, 10)
    soma = sorteado + escolha_number
    resultado = soma % 2

    if resultado == 1:
        resposta = "IMPAR"      
    else:
        resposta = "PAR"

    if escolha == resposta :
        print("Vamos arrastaaar!")
        time.sleep(2)
        
        print ("Você: {} X {} :Maquina".format(escolha,maquina))
        
        time.sleep(2)
        print ("Você: {} X {} :Maquina".format(escolha_number,sorteado))
       
        time.sleep(2)
        print (f"A soma das escolhas foi {soma}")
        
        time.sleep(2)
        print ("Você venceu!")
        vitoria += 1

    else:
        print("Vamos arrastaaar!")
        time.sleep(2)
        
        print ("Você: {} X {} :Maquina".format(escolha,maquina))
       
        time.sleep(2)
        print ("Você: {} X {} :Maquina".format(escolha_number,sorteado))
        
        time.sleep(2)
        print (f"A soma das escolhas foi {soma}")
        
        time.sleep(2)
        print ("Você perdeu!")
        break
    print ()

if vitoria == 1:
    print (f"Você ganhou {vitoria} vez")
else:
    print (f"Você ganhou {vitoria} vezes")
print ("VALEU!")