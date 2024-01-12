'''
Faça um programa que peça o primeiro nome de usuário. Se o nome
tiver 4 letras ou menos escreva ''Seu nome é curto'', de 5 a
6 letras escreva ''Seu nome é normal'' e maior que 6 escreva
''Seu nome é grande''

'''

# ''IF''

'''
nome = input('Digite seu nome: ')

nomecount = len(nome)

pequeno = nomecount <= 4
medio = nomecount >= 5 and nomecount <= 6
grande = nomecount >= 7
  

if pequeno:
    print('Seu nome é curto')
    
if medio: 
    print('Seu nome é médio')
    
if grande:
    print('Seu nome é grande')
    
'''

# Outra maneira de resolver com ''IF''

nome = input('Digite seu nome:')

nomecount = len(nome)

if nomecount > 1:
    if nomecount <= 4:
            print('Seu nome é curto!')
    
    elif nomecount >= 5 and nomecount <= 6: 
            print('Seu nome é médio!')
    
    else:
            print('Seu nome é grande!')
else:
    print('Digite mais de uma letra')


