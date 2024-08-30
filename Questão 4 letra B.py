def verificar_condicao_falsa(A, B, C):
    return ((not A or B) and (A or not B)) or C

print(verificar_condicao_falsa(True, False, False))
print(verificar_condicao_falsa(True, True, False))
print(verificar_condicao_falsa(False, False, False))
print(verificar_condicao_falsa(True, False, True))
