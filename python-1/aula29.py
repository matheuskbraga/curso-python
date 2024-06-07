'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

print()
numero_str = input('Vou dobrar o número que você digitar: ')

# isdigit retorna TRUE se o usuário digitar APENAS NÚMEROS // Se digitar alguma letra retorna FALSE

#if numero_str.isdigit():
#  print(f'O dobro de {numero_str} é {numero_float * 2:.1f}')
#else:
#  print('Você não digitou um número')

# --------------------------------------

try: # tenta executar o codigo aqui
  print('STR:', numero_str)
  numero_float = float(numero_str)
  print('FLOAT:', numero_float)
  print(f'O dobro de {numero_str} é {numero_float * 2:.1f}')

except: # se der algum ERROR no 'try' executa o except
  print('Você não digitou um número')

print()

