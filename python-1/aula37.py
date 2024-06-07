# continue
'''
continue -> pula a vez no loop
'''
contador = 0

while contador <= 10:
  contador += 1

  if contador == 6:
     print('Não vou mostrar o 6')
     continue # pula essa vez no loop ao entrar no 'if'

  print(contador)

  if contador == 40:
      break

print('Acabou')