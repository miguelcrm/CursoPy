# Debugger = retirar um problema do seu código, depurando ele.
# Usando o VS Code e o interpretador do Python.

''' Ao lado da contagem de linha de código terá um ponto verme
lho chamado ''Breakpoint''

    Utilizando o breakpoint fora de uma linha de código, ele
    não irá parar e irá rodar o código inteiro. Temos que usar 
    o breakpoint como marca na primeira linha de código existen
    te.

    Após marca seu breakpoint e começar a depuração do seu códi
    go, ele irá abrir um pequeno painel de opções. E utilizando
    ''Step Over'' ou ''Contornar'' ele irá pular linha de código
    por linha de código conferindo e depurando seu programa parte
    por parte ajudando o entendimento a códigos complexos. 
'''
condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para execução da condição 1')

elif condicao2:
    print('Código para execução da condição 2')

elif condicao3:
    print('Código para execução da condição 3')

elif condicao4:
    print('Código para execução da condição 4')

else :
    print('Nenhuma condição foi aceita!')