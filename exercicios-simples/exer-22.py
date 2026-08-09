#Codigo pra leitura de IMC e avaliação de situação corporal
altura = float (input("Escreva sua altura em metros: "))
peso = float (input("Escreva seu peso: "))
imc = float (peso/(altura**2))
if imc < 18.5:
    print ("Seu IMC é {:.2f}".format(imc))
    print ("Você esta abaixo do peso!")

elif imc >= 18.5 and imc < 25:
    print ("Seu IMC é {:.2f}".format(imc))
    print ("Você esta no peso ideal!")

elif imc >= 25 and imc < 30:
    print ("Seu IMC é {:.2f}".format(imc))
    print ("Você esta no sobrepeso!")

elif imc >= 30 and imc <= 40:
    print ("Seu IMC é {:.2f}".format(imc))
    print ("Você está com obesidade!")

elif imc > 40:
    print ("Seu IMC é {:.2f}".format(imc))
    print ("Você está com obesidade morbida")
print ("VALEU!")