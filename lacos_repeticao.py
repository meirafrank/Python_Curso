# LAÇOS DE REPETIÇÃO - WHILE

"""
numero_sorteado = 15
numero_escolhido = int(input("informe um numero de 1 a 20: "))

if numero_sorteado == numero_escolhido:
    print("Voce acertou")
else:
    print("Voce errou, tente novamente")
"""
numero_sorteado = 15
numero_escolhido = int(input("informe um numero de 1 a 20: "))

while numero_escolhido != numero_sorteado:
    print("Voce errou, tente novamente")

    numero_escolhido = int(input( 'informe um numero de 1 a 20: '))
print("Parabéns, você acertou!")

# Estrutura com contador

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1