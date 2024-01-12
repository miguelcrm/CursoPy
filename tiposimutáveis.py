'''
Os tipos de dados: ''str'', ''int'', ''float'' e ''bool''
são tipos de dados Imutáveis.

Não conseguimos atribuir outro valor ao dado definido para uma 
variável.

Se pormos o nome em uma variável.

nome = 'Miguel Camargo'

Depois de definida, não conseguimos mudar.

Imagina que queremos atribuir um valor aleatório como 
ABC no espaço da nossa string, poderíamos fazer com fatiamento
de str:

'''
nome = 'Miguel Camargo'

nome2 = f'{nome[:6]}ABc{nome[7:]}'

print(nome2)

# Aqui nós conseguimos montar uma str usando um tipo imutável,

