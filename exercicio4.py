'''
Faça um algoritmo que peça ao usuário para digitar um número 
inteiro, informe se este número é par ou ímpar. Caso o usuário
não digite um número inteiro, informe que não é um número inteiro.
'''

# Podemos fazer esse algoritmo de duas formas, com ''isdigit'' e if

# ''IF''  e ''isdigit''

'''
numero = input('Digite um número inteiro:')

if numero.isdigit():
    
    numeroint = int(numero)
    print(f'O número é: {numeroint}')

    par_impar = numeroint % 2 == 0    
    
    if par_impar:
        print(f'O número {numeroint} é par')
    else:
        print(f'O número {numeroint} é ímpar')

else: 
    print('Digite apenas números inteiros')
    
'''

# Ou podemos fazer com try e except

numero = input('Digite um número inteiro:')

try:
    numeroint = int(numero)
    numero_par_impar = numeroint % 3 == 0
    par_impar = 'par'

    if numero_par_impar:
        par_impar = 'ímpar'

    print(f'O número é {numeroint} e ele é {par_impar}')
    
except:
    print('Porfavor, digite apenas números inteiros!')

