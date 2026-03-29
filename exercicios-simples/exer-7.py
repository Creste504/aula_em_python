#Codigo pra tentar adivinhar o numero
import random
print ('Tente adivinhar o numero que eu pensei de 0 a 5.')
numero = random.randint(0 , 5)
chute = int(input('Digite seu chute: '))
if chute == numero:
    print ('acertou')
else:
    print ('errou')
print('--FIM--')