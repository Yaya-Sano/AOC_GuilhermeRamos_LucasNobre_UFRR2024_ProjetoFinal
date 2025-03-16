from sympy import symbols, simplify_logic, Or, And, Not

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

def somador_completo_1bit(x, y, cin):
    """
    Implementa um full adder de 1 bit.
    A soma é calculada como:
      S = (¬x ʌ ¬y ʌ cin) v (¬x ʌ y ʌ ¬cin) v (x ʌ ¬y ʌ ¬cin) v (x ʌ y ʌ cin)
    O carry-out é:
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

def somador_8bits(X, Y, Cin_val):
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
        s, cout = somador_completo_1bit(X[i], Y[i], C[i])
        S.append(s)
        C.append(cout)
    return S, C[-1]

def ula_8bits():
    """
    Constrói a ULA de 8 bits com as seguintes operações:
      - Subtração: A - B, implementada como A + (¬B) + 1.
      - XOR: bitwise, S[i] = A[i] XOR B[i]
      - NAND: bitwise, S[i] = ¬(A[i] ʌ B[i])
      - NOR: bitwise, S[i] = ¬(A[i] v B[i])
      - Shift Left 2: S[i] = A[i-2] (para i>=2), 0 para i = 0,1.
    """
    # Define os 8 bits dos operandos A e B
    A = [symbols(f'A{i}') for i in range(8)]
    B = [symbols(f'B{i}') for i in range(8)]
    
    # Subtração: usar complemento de 2, isto é, calcular A + (¬B) + 1.
    NotB = [Not(b) for b in B]
    S_sub, Cout_sub = somador_8bits(A, NotB, True)  # Cin = True representa +1
    
    # XOR: bitwise
    S_xor = [Or(And(A[i], Not(B[i])), And(Not(A[i]), B[i])) for i in range(8)]
    
    # NAND: bitwise = ¬(A[i] ʌ B[i])
    S_nand = [Not(And(A[i], B[i])) for i in range(8)]
    
    # NOR: bitwise = ¬(A[i] v B[i])
    S_nor = [Not(Or(A[i], B[i])) for i in range(8)]
    
    # Shift Left 2 bits: desloca A 2 posições para a esquerda
    S_shift = []
    for i in range(8):
        if i < 2:
            S_shift.append(False)  # 0
        else:
            S_shift.append(A[i-2])
    
    return {
        'A': A,
        'B': B,
        'Subtraction': (S_sub, Cout_sub),
        'XOR': S_xor,
        'NAND': S_nand,
        'NOR': S_nor,
        'ShiftLeft2': S_shift
    }

def main():
    ops = ula_8bits()
    
    
    print("🔍 ULA de 8 bits - Operações e Expressões Simplificadas:\n")
    
    # Subtração
    S_sub, Cout_sub = ops['Subtraction']
    print("Subtração (A - B):")
    for i in range(8):
        expr = simplify_logic(S_sub[i], form='dnf')
        print(f"Bit {i}: {format_expr(expr)}")
    print(f"Cout (borrow/carry): {format_expr(simplify_logic(Cout_sub, form='dnf'))}\n")
    
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
    
    # Shift Left 2 bits
    print("Shift Left 2 bits (A << 2):")
    for i in range(8):
        expr = ops['ShiftLeft2'][i]
        # Se for o valor False, considere como 0.
        if expr is False:
            print(f"Bit {i}: 0")
        else:
            print(f"Bit {i}: {format_expr(expr)}")

if __name__ == '__main__':
    main()
