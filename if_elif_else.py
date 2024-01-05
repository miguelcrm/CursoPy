# if  / elif      / else
# se  / se não se / se não

# Em uma lista de espera por exemplo:

nome = input('Qual é o seu nome: ')
entrada = input(f'Olá {nome} você quer ''entrar'' ou ''sair'' da nossa lista? ')

if entrada == 'entrar' :
    print(f'Tudo pronto {nome}, você entrou em nossa lista!')

elif entrada == 'sair' :
    print(f'Tudo pronto {nome}, você saiu da nossa lista!')

else:
    print('Você digitou incorretamente, digite novamente')