'''
Flag (Bandeira) - Marcar um Local
None = Não valor.
is e is not = é ou não é (tipo, valor, identidade)

'''

# condicao = True

'''
Se nos quisermos saber se perante essa condição é pra fazer
algo ou não, sendo ela True ou False.

E se ela for true, queremos a confirmação que o interpretador
entrou dentro daquele bloco de código. Podemos fazer uma 
variável dentro do bloco ''if''.

'''

'''
Isso seria um código ruim, e ilegível porque a variável não
foi declarada antes do bloco de código, se colocarmos a condicao
como False, voltará um erro, porque a variável está dentro do blo
co de código, e dará como não criada.

condicao = True

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    passou_no_if = None
    print('Não faça algo')

print(passou_no_if)

A variável criada o else nos retorna um erro, obrigando
a variável ser criada.

'''

'''
Declarando a variável fora do bloco de código, e não precisamos
dela mais no else.

Por ser um valor None, ela só passará ser True se passar pelo
bloco de código ''if''

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    
    print('Não faça algo')

print(passou_no_if)

'''

'''
Agora imagina seu código está em outro módulo e você está
trabalhando em outro código, e você queira demarcar determinado
bloco de código para saber se o interpretador passou por aquele
bloco de código, utilizando o valor None como ''Um não valor''
se ele não passar. 

Você pode fazer da seguinte maneira:
'''

# Usando is e is not (é ou não é)

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

# Se o interpretador passou o valor passará ser True.
    
if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')





