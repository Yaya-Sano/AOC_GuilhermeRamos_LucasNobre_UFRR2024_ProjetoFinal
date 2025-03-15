from sympy import symbols, simplify_logic, Or, And, Not

def format_expr(expr, top=True):
    """
    Converte a expressão booleana (do sympy) para uma string no formato desejado:
      - 'ʌ' para AND
      - 'v' para OR
      - '¬' para NOT
    O parâmetro 'top' controla se adiciona parênteses externos.
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
    # Definição dos símbolos booleanos
    x, y, z = symbols('x y z')

    expr = Or(
                And(Or(Not(x), y), Not(Or(y, And(x, Not(z))))),
                And(x, Not(And(y, z)))
             )
    
    # Exibição da expressão original no formato desejado
    print("Expressão Original:")
    print("F=" + format_expr(expr))
    
    # Simplificação da expressão utilizando álgebra booleana (forma mínima em DNF)
    expr_simplificada = simplify_logic(expr, form='dnf')
    print("\nExpressão Simplificada (Forma Mínima - DNF):")
    print("F=" + format_expr(expr_simplificada))

if __name__ == '__main__':
    main()
