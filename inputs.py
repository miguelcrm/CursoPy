# input = será uma forma para coletar dados do usuário.
''' O programa não será finalizado no terminal até que o usuário
    faça a interação com a input criada.
'''

# input('Qual é o seu nome? ')

# E podemos atribuir uma variável para essa input.
# ''nome'' será a variável. 

nome = input('Qual é o seu nome? ')

print(f'O seu nome é: {nome} \r\n')


# Outro exemplo usando números. 
''' Como as variáveis sempre serão uma str temos que fazer
    uma conversão de tipos para que não gere erro.
'''

numero1 = input(f'{nome} digite um número: ')
numero2 = input('Digite outro número: ')

# Fazendo a conversão.

intnumero1 = int(numero1)
intnumero2 = int(numero2)

print(f'A soma dos números são: {intnumero1 + intnumero2}')
