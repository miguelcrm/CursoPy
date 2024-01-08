'''
Interpolação básica de str

Seria básicamente outro tipo de formatação para saída de código.

E usamos:

s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF123456)

Para usarmos a interpolação temos que colocar o simbolo de ''%''

'''

nome = 'Miguel'
preco = 1000.808223
saida = '%s, o preço é R$%.2f' % (nome,preco)

# Podemos usar o formato '.2f' para casas decimais.
# E logo após a estruturação dentro da str e colocando em ordem
# irá usar ''% (nome,preco)'' forá da estrutura de str.

print(saida)

# Exemplo de hexadecimais. 

'''
X - Maiúsculo = Hexadecimais maiúsculos.
x - Minúsculo = Hexadecimais minúsculos.

'''

print('O hexadecimal de %d é %X' % (15, 15)) 
