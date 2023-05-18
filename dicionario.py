# Dicionarios

# Criando dicionario
dicionario = {}
dicionario = dict()

dicionario = {'nome': "Frank", 'idade': 26, 'altura': 1.77}

print(dicionario)
print(dicionario['idade'])


#Adicionando elementos em um dicionario
dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 2
print(dicionario)


#Iterando sobre um dicionario
for chave in dicionario:  # o for percorre as chaves
    print(chave, dicionario[chave])


# testando existencia de uma chave
print('peso' in dicionario)
print('altura' in dicionario)