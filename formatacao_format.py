a = 'A'
b = 'B'
c = 2.55

''' Podemos colocar as variáveis com o metódo format para serem
utilizadas como outra forma de saída '''

string = 'a = {}, b = {}, c = {:.3f}'

# Saída 
formato = string.format(a,b,c)
print(formato)

