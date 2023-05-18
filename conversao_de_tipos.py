# CONVERSAO DE TIPOS

"""
Como python tem uma tipagem forte, ele converte
a variavel inteira para str, após identificar que o que
ele vai receber é um string
"""

idade = '10'
idade2 = '20'

print(idade + idade2) # resultado = 1020

# Como faço para transformar e converter os tipos

idade = '26'
print(idade, type(idade))

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

# int()
# str ()
# float ()
# bool()

altura = input('informe sua altura: ')

print(altura, type(altura))


x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)