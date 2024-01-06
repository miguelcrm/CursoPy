# Exercício de comparação de valores usando operadores e if.

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

intprimeiro = int(primeiro_valor)
intsegundo = int(segundo_valor)

''' Fiz a coversão de tipos para que o uso de ''str'' 
    retorne um erro. 
'''

if intprimeiro > intsegundo:
    print(f'O valor {intprimeiro} é maior que o valor {intsegundo}')

elif intprimeiro < intsegundo:
    print(f'O valor {intsegundo} é maior que o valor {intprimeiro}')

elif primeiro_valor or segundo_valor == str:
    print('Os valores não são válidos!')

elif intprimeiro == intsegundo:
    print('Os valores são iguais.')
