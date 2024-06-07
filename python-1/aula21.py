# operador logico 'and'
print()

entrada = input('[E]entrada ou [S]sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
  print('Entrou no sistema!')
else:
  print('Não entrou no sistema!')

print()