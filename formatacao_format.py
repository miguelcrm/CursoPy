a = 'A'
b = 'B'
c = 2.55

''' Podemos colocar as variáveis com o metódo format para serem
utilizadas como outra forma de saída '''

string = 'a = {}, b = {nome2}, c = {nome3:.3f}'

# Saída 
formato = string.format(
    a, nome2 = b,
    nome3 = c)
print(formato)

''' 'NOME' = Será um parâmetro nomeado.
    Parâmetro nomeado será um objeto.
    Será usado em ordem e tudo que vier depois da nomeação
    também tem que ser nomeado.
    E precisam também está em ''string'' que é a primeira
    variável. 
'''
