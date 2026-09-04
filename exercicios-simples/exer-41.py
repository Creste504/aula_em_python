#codigo de leitura de PA (Progressão aritimetica) com while melhorado
import time
primeiro_termo = int (input("Digite o primerio termo da PA: "))
razao = int (input("Digite a razao da PA: "))
n = 1
contador = 0
ultimo_numero = 0
escolha_do_user = int(input("Digite até que termo deseja que sua P.A vá: "))
while escolha_do_user != 0:
    print ("Sua P.A ficou assim: ")
    while contador != escolha_do_user:
        ultimo_numero = (primeiro_termo) + (n - 1) * (razao)
        n += 1
        print (ultimo_numero)
        contador += 1
    time.sleep(2)
    print ()
    escolha_do_user = int(input("Se quiser ver mais termos digite o numero de termos que deseja ver, Caso não digite 0: "))
    print ()
    n = 1
    contador = 0
    ultimo_numero = 0
print ("VALEU!")