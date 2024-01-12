'''
Faça um algoritmo que pergunte a hora ao usuário e, baseando-se
no horário de o cumprimento adequado: 00-11 = Bom dia,
12-17 = Boa tarde e 18-23 = Boa noite.

'''

# Algoritmo feito com ''IF'' 

'''
hora = input('Hora atual:')
horaint = int(hora)

bomdia = horaint >= 00 and horaint <= 11
boatarde = horaint >= 12 and horaint <= 17

if bomdia:
    print('Bom dia!')

elif boatarde:
    print('Boa tarde!')
 
else:
    print('Boa noite!')

'''

# Try e Except

hora = input('Digite uma hora em número inteiro: ')

try:

    hora = int(hora)

    bomdia = hora >= 00 and hora <=11
    boatarde = hora >= 12 and hora <= 17
    

    if bomdia:
        print('Bom dia!')

    elif boatarde:
        print('Boa tarde')
    
    else:
        print('Boa noite!')

    
except:
    print('Desculpe, escreva apenas a hora em números inteiros.')

