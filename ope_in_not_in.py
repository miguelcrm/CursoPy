# Operadores Lógicos

# in e not in

# Strings são iteráveis 

''' Significa que podemos navegar item por item 
    por exemplo: M i g u e l 
    
    Nossos podemos navegar pelo ''M'' e assim e adiante usando
    indíces, sendo tanto indíces positivos ou negativos.

    Então o ''M'' estaria no índice 0

    0 1 2 3 4 5
    M I G U E L
   -6-5-4-3-2-1
    
    Índices negativos: começamos contar do -1

    '''
'''

Variável utilizado até o próximo bloco de código:

 nome = 'Miguel'

'''

# Prints com indíces

#print(nome[0])
#print(nome[-5])
#print(nome[2])
#print(nome[-3])
#print(nome[4])
#print(nome[-1])

# O operador IN significa ''está entre''

# Nesse print temos uma condição dizendo se ''g'' está entre letras
# da variável nome.

'''
print('g' in nome)
print('guel' in nome)

'''

# Retornando ''True''.

# O operador NOT IN é ao contrário e significa ''Não está entre''
# Ele irá conferir se a condição repassada não irá estar entre
# a variável repassada. 

'''
print('g' not in nome)

'''

# Essa será a única condição ''False'' por ''g'' está entre as str
# da variável ''nome''

'''

# Exemplo de um print como ''False''

print('fael' not in nome)

'''

# Podemos fazer um pequeno jogo com esses operadores, por exemplo:
# Se uma letra está ou não no nome escolhido.
# Se por exemplo tivessemos Mayara com ''y'' e com ''i''.

nome = input('Digite o nome desejado: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'A letra {encontrar} está em {nome}')
else:
    print(f'A letra {encontrar} não está em {nome}')








