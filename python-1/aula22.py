# operador logico 'or'
print()

entrada = input('[E]entrada ou [S]sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'
senha_permitida2 = '4321'

if (entrada == 'E' or entrada == 'e') and (senha_digitada == senha_permitida or senha_digitada == senha_permitida2):
  print('Entrou no sistema!')
else:
  print('Não entrou no sistema!')

print()