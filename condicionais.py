# ESTRUTURAS CONDICIONAIS

idade = 18

if idade  >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')

"""
Imprimir "aprovado" caso tenha uma média
superior ou igual a 7 e "reprovado se for inferior a 7
"""

media = float(input("informe sua média:  "))
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

#########

media = 10
presenca = 100

if media >=7 and presenca >= 70:
    print("Aprovado")
    print("Parabens")
else:
    print("Reprovado")
    print('Tente novamente')

