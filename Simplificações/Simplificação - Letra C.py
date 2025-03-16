from sympy import symbols, simplify, simplify_logic, And, Or, Not

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

def unidade_controle():
    # Definindo os bits de estado (usamos 3 bits para representar 5 estados)
    S2, S1, S0 = symbols('S2 S1 S0')
    
    # Estados (exemplo simplificado):
    IF  = And(Not(S2), Not(S1), Not(S0))  # Busca de Instrução
    ID  = And(Not(S2), Not(S1), S0)         # Decodificação e Leitura
    EX  = And(Not(S2), S1, Not(S0))         # Execução
    MEM = And(Not(S2), S1, S0)              # Acesso à Memória
    WB  = And(S2, Not(S1), Not(S0))         # Escrita no Registrador
    
    # Sinais que identificam o tipo de instrução (apenas um deve ser 1)
    R, LW, SW, BEQ = symbols('R LW SW BEQ')
    
    # Sinais de controle – definidos de forma simplificada:
    PCWrite   = IF                                  # Atualiza PC somente em IF
    IRWrite   = IF                                  # Grava a instrução somente em IF
    MemRead   = IF                                  # Leitura de memória durante IF
    MemWrite  = And(MEM, SW)                        # Escrita na memória: estado MEM e SW=1
    RegDst    = And(WB, R)                          # Escolhe rd (instrução R) em WB
    RegWrite  = And(WB, Or(R, LW))                  # Escrita no registrador em WB para R ou LW
    MemtoReg  = And(WB, LW)                         # Seleciona dado da memória em LW
    ALUSrcA   = EX                                  # Usa dado do registrador na EX
    ALUSrcB   = ID                                  # Usa dado imediato ou PC+4 em ID
    ALUOp_add = And(EX, Or(LW, SW))                 # Para lw/sw, ALU realiza adição
    ALUOp_sub = And(EX, BEQ)                        # Para beq, ALU realiza subtração
    ALUOp_r   = And(EX, R)                          # Para instrução R, operação definida pelo campo funct
    
    sinais_controle = {
        'PCWrite':   PCWrite,
        'IRWrite':   IRWrite,
        'MemRead':   MemRead,
        'MemWrite':  MemWrite,
        'RegDst':    RegDst,
        'RegWrite':  RegWrite,
        'MemtoReg':  MemtoReg,
        'ALUSrcA':   ALUSrcA,
        'ALUSrcB':   ALUSrcB,
        'ALUOp_add': ALUOp_add,
        'ALUOp_sub': ALUOp_sub,
        'ALUOp_r':   ALUOp_r
    }
    
    estados = {
        'IF': IF,
        'ID': ID,
        'EX': EX,
        'MEM': MEM,
        'WB': WB
    }
    
    return sinais_controle, estados, (S2, S1, S0), (R, LW, SW, BEQ)

def main():
    sinais, estados, state_bits, instr_types = unidade_controle()
    S2, S1, S0 = state_bits
    R, LW, SW, BEQ = instr_types
    
    print("Unidade de Controle do Processador Multiciclo MIPS (FSM):\n")
    
    print("Estados:")
    for nome, estado in estados.items():
        # Tenta simplificar cada estado
        estado_simpl = simplify_logic(estado, form='cnf')
        print(f"{nome}: {format_expr(simplify(estado_simpl))}")
    
    print("\nSinais de Controle:")
    for sig, expr in sinais.items():
        # Primeiro, simplifica usando simplify_logic (forma CNF)
        expr_simpl = simplify_logic(expr, form='cnf')
        # Depois, aplica simplify() para tentar compactar ainda mais
        expr_compacto = simplify(expr_simpl)
        print(f"{sig} (original): {format_expr(expr)}")
        print(f"{sig} (simplificado): {format_expr(expr_compacto)}\n")
    
    print("Observação:")
    print("R, LW, SW, BEQ representam os sinais que identificam o tipo de instrução.")
    print("Exemplo: Para uma instrução do tipo R, R = 1 e LW, SW, BEQ = 0.")

if __name__ == '__main__':
    main()
