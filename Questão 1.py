A = True
B = False
C = True

a = A and (B or C)
b = (A and B) or C
c = not (A and B) or C
d = not A or (not B and C)

print("a) A ^ (B v C) =", a)
print("b) (A ^ B) v C =", b)
print("c) (A ^ B)’ v C =", c)
print("d) A’ v (B’ ^ C) =", d)


#resposta da pergunta

def expr_a(A, B, C):
    return A and (B or C)

def expr_b(A, B, C):
    return (A and B) or C

def expr_c(A, B, C):
    return not (A and B) or C

def expr_d(A, B, C):
    return not A or (not B and C)


def solve_logic_expressions(A, B, C):

    result_a = expr_a(A, B, C)
    result_b = expr_b(A, B, C)
    result_c = expr_c(A, B, C)
    result_d = expr_d(A, B, C)
    
    return {
        "a": result_a,
        "b": result_b,
        "c": result_c,
        "d": result_d
    }

A = True
B = False
C = True

results = solve_logic_expressions(A, B, C)

for key, value in results.items():
    print(f"{key}) {value}")
