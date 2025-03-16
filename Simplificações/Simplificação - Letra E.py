from sympy import symbols, simplify_logic, Or, And, Not, Xor

def format_expr(expr, top=True):
    """
    Converte a expressão booleana para um formato compacto:
     - 'ʌ' para AND
     - 'v' para OR
     - '¬' para NOT
    Mantém a estrutura legível.
    """
    if expr.is_Atom:
        return str(expr)
    elif expr.func == Not:
        s = "¬" + format_expr(expr.args[0], top=False)
        return s if top else "(" + s + ")"
    elif expr.func == And:
        s = " ʌ ".join([format_expr(arg, top=False) for arg in expr.args])
        return s if top else "(" + s + ")"
    elif expr.func == Or:
        s = " v ".join(["(" + format_expr(arg, top=False) + ")" for arg in expr.args])
        return s if top else "(" + s + ")"
    else:
        return str(expr)

# ------------------------------------------
# Módulo: ULA de 8 bits
# ------------------------------------------

def full_adder_bit(x, y, cin):
    """
    Implementa um somador completo de 1 bit.
    S = (¬x ʌ ¬y ʌ cin) v (¬x ʌ y ʌ ¬cin) v (x ʌ ¬y ʌ ¬cin) v (x ʌ y ʌ cin)
    Cout = (x ʌ y) v (x ʌ cin) v (y ʌ cin)
    """
    S = Or(
        And(Not(x), Not(y), cin),
        And(Not(x), y, Not(cin)),
        And(x, Not(y), Not(cin)),
        And(x, y, cin)
    )
    Cout = Or(And(x, y), And(x, cin), And(y, cin))
    return S, Cout

def adder_8bits(X, Y, Cin_val):
    """
    Constrói um somador completo de 8 bits.
    X e Y são listas de 8 bits; Cin_val é o carry-in.
    Retorna:
      - S: lista de 8 bits de soma
      - Cout: carry-out final
    """
    S = []
    C = [Cin_val]
    for i in range(8):
        s, cout = full_adder_bit(X[i], Y[i], C[i])
        S.append(s)
        C.append(cout)
    return S, C[-1]

def full_subtractor(A, B, Bin):
    """
    Subtrator completo de 1 bit:
      Diferença = A ⊕ B ⊕ Bin
      Empréstimo = (¬A ʌ B) v ((A ⊕ B) ʌ Bin)
    """
    Diff = Xor(Xor(A, B), Bin)
    Borrow = Or(And(Not(A), B), And(Xor(A, B), Bin))
    return Diff, Borrow

def alu_8bits():
    """
    Constrói a ULA de 8 bits com as seguintes operações:
      - SUBTRAÇÃO: A - B, implementada como A + (¬B) + 1 (complemento de 2), 
        porém utilizando apenas o subtrator de 1 bit para o bit 0.
      - XOR: bitwise, S[i] = A[i] XOR B[i]
      - NAND: bitwise, S[i] = ¬(A[i] ʌ B[i])
      - NOR: bitwise, S[i] = ¬(A[i] v B[i])
      - DESLOCAMENTO2: desloca A 2 posições para a esquerda (bit 0 e 1 são 0)
    """
    # Define os 8 bits dos operandos A e B
    A = [symbols(f'A{i}') for i in range(8)]
    B = [symbols(f'B{i}') for i in range(8)]
    
    # SUBTRAÇÃO (1 bit): calcula a diferença e o empréstimo para o bit 0 usando o subtrator de 1 bit
    Bin = symbols("Bin")  # Entrada de empréstimo para o subtrator de 1 bit
    Diff, Borrow = full_subtractor(A[0], B[0], Bin)
    
    # XOR: operação bit a bit
    S_xor = [Or(And(A[i], Not(B[i])), And(Not(A[i]), B[i])) for i in range(8)]
    
    # NAND: bitwise = ¬(A[i] ʌ B[i])
    S_nand = [Not(And(A[i], B[i])) for i in range(8)]
    
    # NOR: bitwise = ¬(A[i] v B[i])
    S_nor = [Not(Or(A[i], B[i])) for i in range(8)]
    
    # DESLOCAMENTO2: desloca A 2 posições para a esquerda
    S_shift = []
    for i in range(8):
        if i < 2:
            S_shift.append(False)  # 0
        else:
            S_shift.append(A[i-2])
    
    return {
        'A': A,
        'B': B,
        'SUBTRAÇÃO': (Diff, Borrow),  # Subtração de 1 bit
        'XOR': S_xor,
        'NAND': S_nand,
        'NOR': S_nor,
        'DESLOCAMENTO2': S_shift,
        'Bin': Bin
    }

# ------------------------------------------
# Main: Exibição das funções da ULA e do Subtrator de 1 Bit
# ------------------------------------------

def main():
    ops = alu_8bits()
    
    print("🔍 ULA de 8 bits - Operações e Expressões Simplificadas:\n")
    
    # SUBTRAÇÃO (1 bit)
    Diff, Borrow = ops['SUBTRAÇÃO']
    print("Subtração (A - B) [1 bit]:")
    diff_expr = simplify_logic(Diff, form='dnf')
    borrow_expr = simplify_logic(Borrow, form='dnf')
    print("Diferença = " + format_expr(diff_expr))
    print("Empréstimo = " + format_expr(borrow_expr) + "\n")
    
    # XOR
    print("XOR (A XOR B):")
    for i in range(8):
        expr = simplify_logic(ops['XOR'][i], form='dnf')
        print(f"Bit {i}: {format_expr(expr)}")
    print()
    
    # NAND
    print("NAND (A NAND B):")
    for i in range(8):
        expr = simplify_logic(ops['NAND'][i], form='dnf')
        print(f"Bit {i}: {format_expr(expr)}")
    print()
    
    # NOR
    print("NOR (A NOR B):")
    for i in range(8):
        expr = simplify_logic(ops['NOR'][i], form='dnf')
        print(f"Bit {i}: {format_expr(expr)}")
    print()
    
    # DESLOCAMENTO2
    print("Deslocamento para a esquerda em 2 bits (A << 2):")
    for i in range(8):
        expr = ops['DESLOCAMENTO2'][i]
        if expr is False:
            print(f"Bit {i}: 0")
        else:
            print(f"Bit {i}: {format_expr(expr)}")
    
    print("\nBin (entrada de empréstimo para subtração) = " + format_expr(ops['Bin']))

if __name__ == '__main__':
    main()
