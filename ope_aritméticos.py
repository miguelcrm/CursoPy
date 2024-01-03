# Operadores aritméticos 

# Adição

adicao = 10 + 10
print(adicao)

# Subtração 

subtracao = 10 - 8
print(subtracao)

# Multiplicação 

multiplicacao = 10 * 2
print(multiplicacao)

#Divisão 

divisao = 100 / 5.2
print(divisao)

''' A única diferença entre as divisões e que a divisão
inteira sempre retornará um número inteiro independente 
se ele conter quebrados ou não '''

divisao_inteira = 100 // 5.2
print(divisao_inteira)

# Exponenciação 

exponenciacao = 2 ** 10
print(exponenciacao)

''' Será o mesmo que 2^10 ou 2 elevado a 10'''

# Modulo ou resto da divisão

modulo = 55 % 2
print(modulo)

''' Se fizermos 25 % 5, não terá o resto por conta da divisão
conter um resultado inteiro '''

modulo2 = 25 % 5
print(modulo2)


# Precendência dos operadores aritméticos.

# 1 - ( n + n)
# 2 - **
# 3 - * / // %
# 4 - + - 

''' Se quisermos achar a exponenciação de 2^10 '''

ex1 = 1 + 1 ** 10
print(ex1) # Esse exemplo dará 2, mas se...

ex2 = (1+1) ** 10
print(ex2) # Usando os ''()'', executára da forma correta.

ex3 = ((1+1) ** 10 * 2 / 2 + 1024) / 2 
print(ex3)