# Laços internos 

# Ou While dentro de While 

# Imagine uma tabela

# E para cada linha da tabela, se tem cinco colunas. 


qtd_linhas = 5
qtd_colunas = 5

linha = 1

while linha <= qtd_linhas:

    colunas = 1

    while colunas <= qtd_colunas:
        print(f'{linha = }, {colunas = }')
        colunas += 1
    
    linha += 1

print('Acabou')