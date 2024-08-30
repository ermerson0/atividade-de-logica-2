def conjuncao(p, q):
    return p and q

def disjuncao(p, q):
    return p or q

def condicional(p, q):
    return not p or q

def bicondicional(p, q):
    return p == q

def ou_exclusivo(p, q):
    return p != q


def tabela_verdade():

    print(f"{'P':^5} {'Q':^5} {'AND':^7} {'OR':^7} {'IMPLICA':^10} {'EQUIVAL':^10} {'XOR':^7}")
    print("-" * 50)

   
    valores = [True, False]
    
    for p in valores:
        for q in valores:
            print(f"{str(p):^5} {str(q):^5} "
                  f"{str(conjuncao(p, q)):^7} "
                  f"{str(disjuncao(p, q)):^7} "
                  f"{str(condicional(p, q)):^10} "
                  f"{str(bicondicional(p, q)):^10} "
                  f"{str(ou_exclusivo(p, q)):^7}")

tabela_verdade()
