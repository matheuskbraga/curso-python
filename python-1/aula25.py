# interpolação de string com % em python
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)

nome = 'Matheus'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print()
print(variavel)
print('O hexadecimal de %d é %08x' % (1500, 1500))
print()