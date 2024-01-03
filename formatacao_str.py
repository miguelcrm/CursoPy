#Formatação de Strings

# Aqui temos o código do cálculo do IMC
# Teremos a diferença que usaremos a Formatação de string na saída.

nome = 'Miguel Camargo'
altura = 1.82
peso = 68

imc = peso / altura ** 2

# Alocação da formatação em uma variável
# Utilizando ''{}'' conseguimos armazenar o valor da variável acima.

saida = f'{nome} tem {altura} pesa {peso} e o seu IMC\r\nserá de {imc:.2f}'

''' 
Utilizando o :.nf você dita quantas casas demais terá a
variável númerica ''.'' será o ponto utilizado na separação,
''n'' corresponde números de casas que queira que apareça e
''f'' a formatação

Podemos utilizar quando ocorre a separação com '','' também
colocando a vírgula antes do ponto em :.

'''

print(saida)



