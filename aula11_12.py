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