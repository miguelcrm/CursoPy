# Conversão de valores em Python

print('1') 
print(type('1'))

''' Aqui temos o tipo str e dentro da str tem o número 1 '''

print(1)
print(type(1))

''' Aqui temos o tipo int e dentro dela também temos o número 1 '''

''' E aqui utilizamos a coersão de tipos usando qualquer tipo
de dado.'''

print(int('1') + 1)
print(float('1.5') + 1)
print(str(15) + ' ' + 'meia 15')


# Se tentarmos colocar

# print ('1' + 1) 

# Voltaria um erro de Type, pois ele não reconhece. 