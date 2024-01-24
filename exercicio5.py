# Iterando strings com while 

# String = Interáveis

nome = input('Digite seu nome:')
simbolo = input('Digite algum símbolo: ')

indice = 0 # Contagem

novo_nome = '' # Variável vazia

while indice < len(nome): # Enquanto o indice for menor que a contagem do nome
    
    letra = nome[indice] # == nome[0] == letra
    novo_nome += f'{simbolo}{letra}' # Variável vazia e seu novo valor e atribua ao novo_nome
    indice += 1 # Atribua mais um

novo_nome += f'{simbolo}'
print(novo_nome)




