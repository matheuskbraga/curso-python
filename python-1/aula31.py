# 'id' endereço na memoria
print()
v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))

"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None: # is é o mesmo que ==
    print('Não passou no if')
else:
    print('Passou no if')

print()