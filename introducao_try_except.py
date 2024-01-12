# Introdução a try e except do Python

# Em outras linguagens chamado de ''Try-catch''

''' O try e except executa determinado código, caso ocorra
qualquer erro, com execeção de erro de sintaxe, ele irá
capturar o erro, para manuseio daquele erro em seu código.

'''

# Vamo supor que queremos dobrar um número posto pelo usuário.

 # Input sempre será uma str

''' ''isdigit'' confere se o usuário digitou apenas números. 
''.'' e '','' ele retornará False como valor, são realmente apenas
números.

print(numerostr.isdigit())

teste esse print, para testar o metódo ''isdigit''
'''

# Assim podemos fazer a conferência de que o usuário digitou apenas números.
# Mas o ''IF'' não evita erros em nosso código, ele apenas confere a lógica. 

'''
Executando essa linha de código, e se tentarmos usar um ''.''
ou alguma letra, ele nós retornará um o else.

if numerostr.isdigit():
    numerofloat = float(numerostr)
    print(f'O dobro do {numerofloat} é {numerofloat * 2:.2f}')
else:
    print('Isso não é um número.')

ou mudando a estruturação do código e tentarmos converter o número para
float antes de entrar no bloco de if, ele retornará um erro.

numerofloat = float(numerostr)

if numerostr.isdigit():
    print(f'O dobro do {numerofloat} é {numerofloat * 2:.2f}')
else:
    print('Isso não é um número.')

Erros são chamados de execeções, e o if não confere execeções, podemos resolver
isso com try e except

'''

''' Try = Tenta executar essa linha de código e se ocorrer alguma erro, pule
diretamente para meu bloco de código ''except''

E alguma momento no bloco de código abaixo, ele irá gerar um erro, se utilizarmos
algo que não seja números, por exemplo, e ele irá executar até o erro, após o erro
ele pula para o ''except''

'''

''' Se utilizarmos uma str para interação do usuário com a input, ele irá pular 
diretamente ao ''except''.

Evitando o erro comum causado pela conversão. 

'''
numerostr = input('Vou dobrar o número que você digitar: ')


try:
    numerofloat = float(numerostr) # Aqui acontece a conversão.
    print('FLOAT:', numerofloat)
    print(f'O dobro do {numerofloat:.2f} é {numerofloat * 2:.2f}')
except:
    print('Isso não é um número')




# Chamamos isso de fail-fast.
# Muito utilizado para conferência de erros para o código.

# Isso é o básico do try e except como uma pequena demonstração!





