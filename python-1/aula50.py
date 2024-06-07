'''
Introdução ao desempacotamento + tuples (tuplas)
'''
import os
os.system('cls')

#desempacotamento
nome1, nome2, nome3 = ['Matheus', 'Arthur', 'Marcelo']
print(nome1, nome2, nome3)

_, _, nome, *resto = ['Paulo', 'Maurício', 'Gabriel']
print(nome1, nome2, nome3)