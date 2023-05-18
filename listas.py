# LISTAS

#Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com Lista
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = []
lista = list()
lista = [26, 'Frank', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# Indexação e Slices -- acessando um elemento da lista

lista = [10, 'Frank', 3.14159, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4])

print(lista[-1])  # ultimo indice da lista

# Slice - fatiamento, pedaçõs da lista

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])

print(lista[3:])
print(lista[2:6:2])

# iteração com FOR
# 1 utilizando os proprios elementos da lista

for elemento in lista:
    print(elemento)

# 2 utilizando os indices

print('Comprimento da lista:', len(lista))

for i in range(len(lista)):
    print(lista[i])

# Métodos de lista

lista = [1, 3, 12, 8, 2]

# append

print(lista)

print('Antes do append: ', lista)

lista.append(3)

print('Depois do append: ', lista)

# Insert

lista.insert(2, 10)

print('Depois do insert: ', lista)

# extend

lista2 = [1, 2, 3]

lista.extend(lista2)
print('Depois do extend: ', lista)

# pop remove elementos

lista.pop()

print('Depois do pop: ', lista)

lista.pop(0)

print('Depois do pop: ', lista)

# remove (vc diz qual valor quer retirar)

lista.remove(3) # remove item 3, o primeiro que ele encontra, nao posicao 3

print('Depois do remove: ', lista)

# count

print(" Quantidade de 2 na lista: ", lista.count(2))

# index

print("indice do elemento 12: ", lista.index(12))

# sort - ordenar a lista

lista.sort(reverse=True)

print(lista)


# FUNÇÕES PARA LISTAS

# LEN
print(len(lista))

# SUM
print(sum(lista))

#MAX
print("maior elemento da lista: ", max(lista))

#MIN
print("menor elemento da lista: ", min(lista))