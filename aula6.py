# Conversão de valores em Python

print('1') 
print(type('1'))

''' Aqui temos o tipo str e dentro da str tem o número 1 '''

print(1)
print(type(1))

''' Aqui temos o tipo int e dentro dela temos o número 1 '''

''' Se por acaso você estiver em um programa ou crie
uma calculadora por exemplo e a informação que seu código
recebe seja um str mas você tem que somar essa str
com outro valor, podemos usar a conversão do valor'''

print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1.5') + 1)
print(str(15) + ' ' + 'meia 15')
print(bool(  ))

# Se tentarmos colocar

# print ('1' + 1) 

# Voltaria um erro de Type, pois ele não reconhece. 