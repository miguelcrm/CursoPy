# Operadores Lógicos 

#and = (e), or = (ou), not = (não)

# Quando se usa ''and'' todas as condições tem que ser verdadeiras.
# Se o valor for considerado falso, toda a expressão será falsa.

# São considerados expressões falsas: 0, 0.0, '', False

# Também existe o valor ''None'', não é um valor falso, mas um valor não existente.

# Usando o exemplo em que o usuário escolha entre entrar e sair de uma lista.
# Podemos aplicar os operadores lógicos.


# Retire esse código do comentário para que execute a primeira parte dele.
'''
entrada = input('[E]ntrar ou [S]air? ')

if entrada == 'E':
    print('Entrar')

elif entrada == 'S' :
    print('Sair')

else:
    print('Digite apenas ''E'' ou ''S''!')
'''
# Agora se fossemos por exemplo ter uma interação de usuário
# Para que ocorresse acesso a lista que ele se cadastrou.
# Para isso ele precisa ter acesso a primeira senha registrada.
# Ele somente irá ''Entrar'' se as duas condições no código forem verdadeiras.
# Caso contrário ele irá ser avaliado como falso e irá direto para o ''Sair''

entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Digite sua senha: ')

senha_registrada = '123456'

if entrada == 'E' and senha_digitada == senha_registrada:
    print('Entrar')

elif entrada == 'S' and senha_digitada == senha_registrada:
    print('Sair')

elif senha_digitada != senha_registrada:
    print('Senha incorreta!')

else:
    print('Digite apenas ''E'' ou ''S''!')