# Operadores Lógicos.

# Not (não) - Usado para inverter expressões.

entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Digite sua senha: ')

senha_registrada = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_registrada:
    print('Entrar')

elif (entrada == 'S' or entrada == 's') and senha_digitada == senha_registrada:
    print('Sair')

# Podemos usar o not nesse código para validar que o usuário
# não digitou nenhuma senha.
# Qualquer 'str' vazia retorna False, então podemos criar um
# elif invertendo seu valor quando o campo for vazio, fazendo
# que o interpretador entenda o valor da expressão como verdadeira
# e nos retorna a confirmação. 

elif not senha_digitada:
   print('O campo da senha está vazio!')

elif senha_digitada != senha_registrada:
    print('Senha incorreta!')

else:
    print('Digite apenas ''E'' ou ''S''!')



# Avaliação de curto circuito do not
# Qualquer expressão True, ele retorna False, e qualquer False
# retorna True.

print(not False)
print(not True)