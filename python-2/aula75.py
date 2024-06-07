import os
'''
# função duplica
def duplica(numeros):
  lista_resultados = []
  for numero in numeros:
    lista_resultados.append(numero * 2)
  return lista_resultados

# função triplica
def triplica(numeros):
  lista_resultados = []
  for numero in numeros:
    lista_resultados.append(numero * 3)
  return lista_resultados

# função quadriplica
def quadriplica(numeros):
  lista_resultados = []
  for numero in numeros:
    lista_resultados.append(numero * 4)
  return lista_resultados
'''

def criar_multiplicador(multiplicador):
  def multiplicar(numeros):
    resultados = []
    for numero in numeros:
      resultados.append(numero * multiplicador)
    return resultados
  return multiplicar

os.system('cls')
numeros = [3, 5, 8]

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print('Duplicados:',duplicar(numeros))
print('Triplicados:',triplicar(numeros))
print('Quadruplicados:',quadruplicar(numeros))
