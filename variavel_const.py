# Variáveis, constantes e complexidade do código 

'''
CONSTANTES = São valores que não vão mudar no seu código,
ela sempre terá o mesmo valor e não será atribuído outros
valores a aquela variável.

Em Python não temos o conceito de constantes, mas para indicar
que é uma constante usamos a varíavel em letras MAIÚSCULA.

'''

# Outro assunto abordado nessa aula é complexidade de código.

'''
Códigos complexos não ajudam para a leitura do seu código,
como por exemplo muitos ''if'' entre outras coisas, quanto
mais simples seu código for, melhor para o desenvolvimento.
'''

# Exemplo de constantes.

# Imagina um carro em um estrada e a velocidade do carro é:

# Esse é o primeiro código de ''IF'' mas podemos limpar esse código:


velocidade = 61 # Velocidade atual do carro.
localidade = 98 # O ''KM'' em que os carro está dá estrada.

RADAR_1 = 60 # Velocidade máxima do radar 1.
LOCAL_1 = 100 # Local onde está o radar na estrada.
RADAR_RANGE = 1 # A distância onde o radar pega.

excesso_velocidade = velocidade > RADAR_1

localidade_min = localidade >= (LOCAL_1 - RADAR_RANGE)
localidade_max = localidade <= (LOCAL_1 + RADAR_RANGE)

if excesso_velocidade:
    print('Excesso de velocidade')

if localidade_min and localidade_max:
    print('O carro passou na estrada')

if localidade_min and localidade_max and excesso_velocidade: 
    print('Carro multado')





