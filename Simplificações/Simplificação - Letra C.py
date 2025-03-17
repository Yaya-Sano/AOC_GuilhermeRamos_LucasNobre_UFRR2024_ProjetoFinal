from sympy import symbols, simplify_logic, And, Or, Not

# Função para formatar expressões booleanas de forma legível
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

# Definir variáveis de estado e opcode
S2, S1, S0 = symbols('S2 S1 S0')  # Bits de estado
Op5, Op4, Op3, Op2, Op1, Op0 = symbols('Op5 Op4 Op3 Op2 Op1 Op0')  # Bits do opcode

# Expressões booleanas completas (definidas anteriormente)
RegDst_expr = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0))
ALUSrc_expr = And(Not(S2), S1, Not(S0), Or(
    And(Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0),  # LW
    And(Not(Op5), Not(Op4), Op3, Not(Op2), Not(Op1), Not(Op0))  # SW ou ADDI
))
MemtoReg_expr = And(Not(S2), Not(S1), S0, Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0)  # LW
RegWrite_expr = And(S2, Not(S1), Not(S0), Or(
    And(Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0)),  # R-type
    And(Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0),  # LW
    And(Not(Op5), Not(Op4), Op3, Not(Op2), Not(Op1), Not(Op0))  # ADDI
))
MemRead_expr = Or(
    And(Not(S2), Not(S1), Not(S0)),  # Fetch
    And(Not(S2), Not(S1), S0, Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0)  # LW
)
MemWrite_expr = And(Not(S2), Not(S1), S0, Not(Op5), Not(Op4), Op3, Not(Op2), Not(Op1), Not(Op0))  # SW
Branch_expr = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Op1, Not(Op0))  # BEQ
ALUOp1_expr = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0))  # R-type
ALUOp0_expr = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Op1, Not(Op0))  # BEQ
Jump_expr = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Op1, Op0)  # J

# Simplificar as expressões booleanas
RegDst_simplified = simplify_logic(RegDst_expr)
ALUSrc_simplified = simplify_logic(ALUSrc_expr)
MemtoReg_simplified = simplify_logic(MemtoReg_expr)
RegWrite_simplified = simplify_logic(RegWrite_expr)
MemRead_simplified = simplify_logic(MemRead_expr)
MemWrite_simplified = simplify_logic(MemWrite_expr)
Branch_simplified = simplify_logic(Branch_expr)
ALUOp1_simplified = simplify_logic(ALUOp1_expr)
ALUOp0_simplified = simplify_logic(ALUOp0_expr)
Jump_simplified = simplify_logic(Jump_expr)

# Exibir as expressões simplificadas
print("Expressões booleanas simplificadas da Unidade de Controle:\n")
print("RegDst:", format_expr(RegDst_simplified))
print("ALUSrc:", format_expr(ALUSrc_simplified))
print("MemtoReg:", format_expr(MemtoReg_simplified))
print("RegWrite:", format_expr(RegWrite_simplified))
print("MemRead:", format_expr(MemRead_simplified))
print("MemWrite:", format_expr(MemWrite_simplified))
print("Branch:", format_expr(Branch_simplified))
print("ALUOp1:", format_expr(ALUOp1_simplified))
print("ALUOp0:", format_expr(ALUOp0_simplified))
print("Jump:", format_expr(Jump_simplified))
