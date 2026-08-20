#identificador de palindromos
frase = input("Digite um palindromo: ")
frase = frase.upper()
frase = frase.replace(" ", "")
numero_de_caracteres = len(frase)
palindromo = True
for c in range (0, numero_de_caracteres//2):
    
    if frase[c] == frase[numero_de_caracteres - 1 - c]:
        palindromo = True
    else:
        palindromo = False 
        
if palindromo == True:
    print ("Parabéns você escreveu um palindromo!")
else:
    print ("Você não escreveu um palindromo")
print ("VALEU!")