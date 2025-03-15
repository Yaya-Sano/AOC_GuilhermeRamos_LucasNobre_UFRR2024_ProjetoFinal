from sympy import symbols, simplify_logic, Or, And, Not 

def expressao_booleana(A, B, C, D):
    """
    Cria a expressão booleana complexa:
    F = ABCD + AB¬C D + AB¬C¬D + A¬B C D + ¬A B C D + ¬A B C ¬D + ¬A B ¬C D + ¬A ¬B ¬C D
    """
    return Or(
        And(A, B, C, D),
        And(A, B, Not(C), D),
        And(A, B, Not(C), Not(D)),
        And(A, Not(B), C, D),
        And(Not(A), B, C, D),
        And(Not(A), B, C, Not(D)),
        And(Not(A), B, Not(C), D),
        And(Not(A), Not(B), Not(C), D)
    )

def format_expr(expr, top=True):
    """
    Converte a expressão booleana (do sympy) para uma string
    usando o formato desejado:
     - 'ʌ' para AND
     - 'v' para OR
     - '¬' para NOT
    O parâmetro 'top' controla se adiciona parênteses externos.
    """
    # Se for um átomo (variável), retorna seu nome
    if expr.is_Atom:
        return str(expr)
    elif expr.func == Not:
        s = "¬" + format_expr(expr.args[0], top=False)
        return s if top else "(" + s + ")"
    elif expr.func == And:
        s = " ʌ ".join([format_expr(arg, top=False) for arg in expr.args])
        return s if top else "(" + s + ")"
    elif expr.func == Or:
        # Para OR, coloca cada argumento entre parênteses
        s = " v ".join(["(" + format_expr(arg, top=False) + ")" for arg in expr.args])
        return s if top else "(" + s + ")"
    else:
        return str(expr)

def main():
    # Definindo as variáveis simbólicas
    A, B, C, D = symbols('A B C D')
    
    # Obtendo a expressão original
    expr_original = expressao_booleana(A, B, C, D)
    
    # Simplificando a expressão para sua forma mínima (DNF)
    expr_simplificada = simplify_logic(expr_original, form='dnf')
    
    # Formatando as expressões no estilo desejado
    formatted_original = "F=" + format_expr(expr_original, top=True)
    formatted_simplificada = "F=" + format_expr(expr_simplificada, top=True)
    
    print("Expressão Original:")
    print(formatted_original)
    print("\nExpressão Simplificada (Forma Mínima - DNF):")
    print(formatted_simplificada)

if __name__ == '__main__':
    main()
