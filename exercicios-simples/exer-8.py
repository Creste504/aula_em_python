#codigo pra ler a quilometragem de um carro
velocidade = float(input('Indique a velocidade que você atingiu na pista: '))
if velocidade > 80:
    muta = (velocidade - 80) * 7
    print ('Você ira pagar uma muta de {}R$'.format(muta))
else:
    print ('Ta tudo bem, você não foi multado.')