# Fatiamento de str

''' 
Sendo outra formatação de str, o fatiamento de str podemos pegar
o começo de uma str, o final, e por partes, também usando índices.

No uso de índices, geralmente o índice final não é incluso
e por isso usasse um indíce a mais.

Fatiamento = [i:f:p]

O fatiamento é caracterizado pelo '':''

'''

# Temos um simples exemplo usando um ''print''

#           123 45678
variavel = 'Olá mundo'

# Se pedirmos que pegue 4 de começo e 7 no final, ele retornará
# ''mund''

print(variavel[4:8:])

''' Se não ditarmos o final, ele entende que deve pegar tudo
até o final da str.
'''

print(variavel[4:])

# A mesma coisa para o começo.

print(variavel[:8:])

''' Já o ''p'' de passo, será quantos caracteres ele irá contar
por vez, se é de 1 em 1 ou de 2 em 2.
'''
# Se colocarmos de 2 em 2, ele irá contar 1 letra e pular 1 letra.

print(variavel[::2])

''' A função ''len'' ela irá servir para a contagem dos caracteres
de uma str.
'''

print(len(variavel))

'''
Podemos utilizar os índices negativos também, na mesma lógica
aprendida nas aulas anteriores, para o [i:f] usando os índices
negativos, somente mudará o [p]

Se usarmos índices negativos no [p], ele começara contar a str
ao contrário. 
'''

print(variavel[::-1])

