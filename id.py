# Id - Identidade do valor na memória 

# Se temos uma variável guardando um valor, podemos ver o Id dela.
# utilizando o ''print''.

'''
v1 = 'a'
print(id(v1))

'''

# Mas se tivermos esse mesmo valor em duas variáveis?


v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))


'''
 Sendo Python uma linguagem dinâmica e forte, ele reconhece
as duas variáveis como o mesmo valor de ip, porque são duas
variáveis iguais

'''