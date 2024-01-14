# While

'''
While = Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

Loop Infinito - Quando um código não tem fim.

# Isso é um exemplo de código de Loop Infinito,
tem que tomar cuidado, que isso pode gerar um transtorno
em seu computador, por repetir ele várias vezes, caso não
consiga parar.

condicao = True

while condicao:
    print(1)

'''

# Mas se fizermos da seguinte maneira

# Se a condicao for ''True'', e enquanto ela for ''True''
# ela irá rodar o que está dentro do bloco de código while

condicao = True

while condicao: # Enquanto condição for true
    nome = input('Digite seu nome: ') # Digite um nome
    
    if nome == 'sair' or nome == 'Sair': # Se o nome digitado
        break # for sair ou Sair acabe o código.
                # Se não
    
    print(f'Seu nome é: {nome}') # Imprima o nome digitado
    
# Se usarmos o Debugger iremos ver como funciona o While.
# Ele irá rodar trecho por trecho de código, e você irá perceber
# Que enquanto a condicao for ''True'', ele volta ao While.

# Podemos utilizar ''break'' para parar o laço While.
    # Se o usuário escrever ''sair'' em nome, ele irá ativar o break.

print('Acabou')    

