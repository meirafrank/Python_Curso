# FUNÇÕES

"""
print() #imprime a mensagem (int, float, str, no console do terminal)
input() #retorna um dado informado pelo usuario
len() #recebe uma lista e retorna o tamanho dela
max()#retorna o maior valor de uma lista

"""
# Criação de Função - Função inicial
def saudacao():
    print("Seja bem vindo")
    print("olá")

saudacao()

# Função com parâmetros
def saudacao(nome, curso):
    print(f"Seja bem vindo, {nome} !")
    print(f"curso, {curso}")

saudacao("Frank", "python")


# Função com parâmetros default
def saudacao(nome, curso="Python"):
    print(f"Seja bem vindo, {nome} !")
    print(f"seu curso é: {curso}")

saudacao("Frank")


# Funções com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5,7)
print("O resultado da soma é: ", resultado)


# exercicio

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20, '-')

print(resultado)
