# codigo de adivinhação de um numero de 0 a 10 até a pessoa acertar
import random
palpites = 0
adivinha = "j"
print ('Tente adivinhar o numero que eu pensei de 0 a 10.')
numero = random.randint(0 , 10)
while adivinha != "ACERTOU":
    chute = int(input('Digite seu chute: '))
    if chute == numero:
        adivinha = "acertou".upper()
        print ('acertou')
    else:
        adivinha = "errou".upper
        print ('errou')
    palpites += 1
if palpites == 1:
    print ("Você acertou em apenas 1 tentativa, PARABÉNS! ")
else:
    print ("Você acertou em {} tentativas".format(palpites))
print('VALEU!')