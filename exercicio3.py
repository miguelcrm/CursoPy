# Nesse exercício usaremos tudo dito até o momento.
''' (Operadores, if, formatação, fatiamento, etc...)'''

# Peça ao usuário que digite seu nome.
# Peça ao usuário que digite sua idade.

# Se nome e idade forem digitados exiba:

'''
1. Seu nome.
2. Seu nome invertido. 
3. Se o nome contém ou não espaços
4. Conte as letras do nome do usuário.
5. A primeira letra do nome.
6. A última letra do nome.

Se nada for digitado em nome ou idade.
exiba ''Desculpe, você deixou campos vazios''

'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if ' ' not in nome and (nome and idade):
    print(f'Seu nome é:{nome}')
    print(f'Seu nome invertido é:{nome[::-1]}')
    print(f'Não contém espaços')
    print(f'O total de letras em seu nome é:{len(nome)}')
    print(f'A primeira letra do nome é:{nome[0]}')
    print(f'A última letra do nome é:{nome[-1]}')

elif ' ' in nome and (nome and idade):
    print(f'Seu nome é:{nome}')
    print(f'Seu nome invertido é:{nome[::-1]}')
    print(f'Contém espaços')
    print(f'O total de letras em seu nome é:{len(nome)}')
    print(f'A primeira letra do nome é:{nome[0]}')
    print(f'A última letra do nome é:{nome[-1]}')

else: 
    print('Desculpe, você deixou campos vazios!')
    



















   
    

         















