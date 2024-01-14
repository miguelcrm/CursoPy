# While + continue 

'''
Quando se usa ''Continue'' estamos pulando um trecho do código
e voltando ao estado inicial do while e rodando ele novamente.

'''


# Fazer um algoritmo que conte de 1 em 1.

contador = 0

while contador < 10: # Enquanto o contador for menor que 30
    contador += 1 # Adicione mais um
    
    

    if contador == 2: # Se o contador for 30
        print('Não mostre o 30')
        continue # Volte pro início do While

    if contador >= 5 and contador <= 8: # E se o contador estiver entre 10 e 25
        print('Faixa Oculta')# Imprima
        continue # Volte pro início do while


    print(contador)
   




