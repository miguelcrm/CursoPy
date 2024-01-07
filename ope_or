# Operadores Lógicos

# or (ou) - Qualquer condição que seja verdadeira, ele irá avaliar
# toda a expressão como verdadeira. 

''' Para introduzirmos ''or'' em nosso código e para que 
    o interpretador possa entender a diferenciação das 
    condições, podemos utilizar os () para essa situação,
    diferenciando e não causando conflitos no código. '''

entrada = input('[E]ntrar ou [S]air? ')
senha_digitada = input('Digite sua senha: ')

senha_registrada = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_registrada:
    print('Entrar')

elif (entrada == 'S' or entrada == 's') and senha_digitada == senha_registrada:
    print('Sair')

elif senha_digitada != senha_registrada:
    print('Senha incorreta!')

else:
    print('Digite apenas ''E'' ou ''S''!')

# Avaliação de curto circuito do or
# Qualquer expressão True, ele retorna True.

print(False or False or False or True)