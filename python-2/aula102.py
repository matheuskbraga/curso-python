import os

os.system('cls')

# Variáveis livres + nonlocal (locals, globals)
'''
def fora(x):
  a = x

  def dentro():
    # print(locals()) # mostra tudo que eu posso acessar localmente
    return a
  return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())
'''

def concatenar(string_inicial):
  valor_final = string_inicial # escopo atual

  def interna(valor_a_concatenar=''):
    nonlocal valor_final  # acesso do escopo anterior
    valor_final += valor_a_concatenar
    return valor_final
  return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print('final')