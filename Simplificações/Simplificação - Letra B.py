from sympy import symbols, simplify_logic, Or, And, Not

def somador_completo(A, B, Cin):
    """
    Somador completo de 1 bit:
    S = A ⊕ B ⊕ Cin
    Cout = (A ʌ B) v (A ʌ Cin) v (B ʌ Cin)
    
    A soma S é implementada na forma:
      S = (¬A ʌ ¬B ʌ Cin) v (¬A ʌ B ʌ ¬Cin) v (A ʌ ¬B ʌ ¬Cin) v (A ʌ B ʌ Cin)
    """
    S = Or(
        And(Not(A), Not(B), Cin),
        And(Not(A), B, Not(Cin)),
        And(A, Not(B), Not(Cin)),
        And(A, B, Cin)
    )
    
    Cout = Or(
        And(A, B),
        And(A, Cin),
        And(B, Cin)
    )
    
    return S, Cout

def format_expr(expr, top=True):
    """
    Converte a expressão booleana para um formato mais compacto:
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

def main():
    # Definindo os símbolos booleanos para um somador de 1 bit
    A, B, Cin = symbols('A B Cin')
    
    # Obtém as expressões do somador completo de 1 bit
    S, Cout = somador_completo(A, B, Cin)
    
    print(" Expressões Originais do Somador Completo de 1 Bit:")
    print(f"S = {format_expr(S)}")
    print(f"Cout = {format_expr(Cout)}")
    
    # Simplifica as expressões usando a forma DNF
    S_simplificado = simplify_logic(S, form='dnf')
    Cout_simplificado = simplify_logic(Cout, form='dnf')
    
    print("\n Expressões Simplificadas:")
    print(f"S = {format_expr(S_simplificado)}")
    print(f"Cout = {format_expr(Cout_simplificado)}")
    print("\n Analise de uma parte menor para base")
if __name__ == '__main__':
    main()
