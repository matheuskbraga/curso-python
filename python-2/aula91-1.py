# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
  yield 1
  print('Continuando...')
  yield 2
  print('Mais uma...')
  yield 3
  print('Vou terminar')
  return 'ACABOU'

gen = generator(n=0)
#print(next(gen)) # 1
#print(next(gen)) # Continuando...    2
#print(next(gen)) # Mais uma          3
#print(next(gen)) # ACABOU

for n in gen:
  print(n)