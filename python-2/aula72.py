import os

# Questão 1
def multiplicaTodos(numeros):
  total = 1
  for numero in numeros:
    total *= numero
  return total

# Questão 2
def analisaNumero(numero_digitado):
  if numero_digitado % 2 == 0:
    print(f'{numero_digitado} é Par')
  else:
    print(f'{numero_digitado} é Ímpar')

os.system('cls')
# print(1*2*3*4*5*6)
numeros = [1, 2, 3, 4, 5, 6]
print(f'Questão 1: Multiplicação da lista: {numeros}')
print('Resultado:',multiplicaTodos(numeros))
print('------------------------------')
print('Questão 2: Verificando se o numero é par ou ímpar')
numero_digitado = int(input('Digite um valor inteiro: '))
analisaNumero(numero_digitado)