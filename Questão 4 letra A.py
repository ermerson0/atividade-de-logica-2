#Letra A
def tarefa(A, B, C):
    return ((A and not B) or (not A and B)) and not C

A, B, C = True, False, False
print(tarefa(A, B, C))

A, B, C = True, True, False
print(tarefa(A, B, C))

A, B, C = False, False, False
print(tarefa(A, B, C))

A, B, C = True, False, True
print(tarefa(A, B, C))
