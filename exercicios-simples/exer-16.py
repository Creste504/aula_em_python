#Codigo de conversão em binario, octal ou hexadecimal
numero = int (input('Digite um numero inteiro: '))
escolha = int (input('Escolha para qual deseja converter (1 é binario, 2 é octal e 3 é hexadecimal): '))
if escolha == 1:
    print ('Seu numero é {}'.format (numero))
    binario = bin (numero)
    print  ('Seu numero convertido para binario é: {}'.format(binario[2:]))
elif escolha == 2:
    print ('Seu numero é {}'.format (numero))
    octal = oct (numero)
    print  ('Seu numero convertido para octal é: {}'.format(octal[2:]))
elif escolha == 3:
    print ('Seu numero é {}'.format (numero))
    hexadecimal = hex (numero)
    print  ('Seu numero convertido para hexadecimal é: {}'.format(hexadecimal[2:]))