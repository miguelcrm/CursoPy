#Formatação de Strings

# Aqui temos o código do cálculo do IMC
# Teremos a diferença que usaremos a Formatação de string na saída.

nome = 'Miguel Camargo'
altura = 1.82
peso = 68

imc = peso / altura ** 2

# Alocação da formatação em uma variável
# Utilizando ''{}'' conseguimos armazenar o valor da variável acima.

saida = f'{nome} tem {altura} pesa {peso} e o seu IMC será de {imc} '

print(saida)



