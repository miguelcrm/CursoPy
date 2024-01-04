a = 'A'
b = 'B'
c = 2.55

''' Podemos colocar as variáveis com o metódo format para serem
utilizadas como outra forma de saída '''

string = 'a = {nome1}, b = {nome2}, c = {nome3:.3f}'

# Saída 
formato = string.format(
    nome1 = a,
    nome2 = b,
    nome3 = c)
print(formato)

''' 'NOME' = Será um parâmetro nomeado.
    Parâmetro nomeado será um objeto.
    Será usado em ordem.
    E precisam também está em ''string'' que é a primeira
    variável. 
'''
