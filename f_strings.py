'''
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF123456)

# Estrutura:

(Caracteres) = (><^) = (quantidade)

> - Esquerda
< - Direita
^ - Centro

Sinal - + ou -
Ex: 0>-100, .1f

Conversion flags - !r !s !a

'''

variavel = 'ABC'
print(f'{variavel}')

# O segundo print aparecerá com 10 caracteres ou espaços a lado correspondente (><)

print(f'{variavel: >15}')
print(f'{variavel: <15} .')
print(f'{variavel: ^15}')

print(f'{1000.02020320:,.2f}')
print(f'{-1000.02020320:-,.2f}')
print(f'{+1000.02020320:+,.2f}')

