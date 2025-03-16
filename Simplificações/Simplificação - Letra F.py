from sympy import symbols, simplify_logic, And, Or, Not

def format_expr(expr, top=True):
    """
    Converte a expressão booleana para uma string com:
      - 'ʌ' para AND
      - 'v' para OR
      - '¬' para NOT
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

def alu_control_rtype_state():
    # Definindo os dois bits de estado
    s1, s0 = symbols('s1 s0')
    # Estados:
    # IF: s1=0, s0=0
    # ID: s1=0, s0=1
    # EX: s1=1, s0=0
    # WB: s1=1, s0=1
    
    # Sinais de controle para uma instrução R (exemplo simplificado):
    PCWrite  = And(Not(s1), Not(s0))    # Ativo somente em IF
    MemRead  = And(Not(s1), Not(s0))    # IF
    IRWrite  = And(Not(s1), Not(s0))    # IF
    RegDst   = And(s1, s0)              # WB (seleciona rd)
    RegWrite = And(s1, s0)              # WB
    ALUSrcA  = And(s1, Not(s0))          # EX (usa o conteúdo do registrador)
    ALUOp    = And(s1, Not(s0))          # EX (operações determinadas pelo campo funct)
    MemtoReg = False                   # Para instruções R, o dado vem do ALU, não da memória
    
    control_signals = {
        'PCWrite': PCWrite,
        'MemRead': MemRead,
        'IRWrite': IRWrite,
        'RegDst': RegDst,
        'RegWrite': RegWrite,
        'ALUSrcA': ALUSrcA,
        'ALUOp':   ALUOp,
        'MemtoReg': MemtoReg
    }
    return control_signals, (s1, s0)

def main():
    control_signals, state_bits = alu_control_rtype_state()
    
    print("Fluxo de Execução para uma Instrução R (MIPS 32 bits):\n")
    for sig, expr in control_signals.items():
        if expr is False:
            formatted = "0"
        else:
            # Usamos a forma CNF para uma saída mais compacta
            simplified_expr = simplify_logic(expr, form='cnf')
            formatted = format_expr(simplified_expr)
        print(f"{sig} = {formatted}")
    
    print("\nEstados representados por s₁ s₀:")
    print("IF: 0 0,   ID: 0 1,   EX: 1 0,   WB: 1 1")
    print("Sequência: IF -> ID -> EX -> WB")

if __name__ == '__main__':
    main()
