from z3 import *

# Definindo as variáveis
Op0, Op1, Op2, Op3, Op4, Op5 = Bools('Op0 Op1 Op2 Op3 Op4 Op5')
S0, S1, S2 = Bools('S0 S1 S2')

# Expressão 1
RegDst_expr_1 = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0))
ALUSrc_expr_1 = And(Not(S2), S1, Not(S0), Or(
    And(Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0),  # LW
    And(Not(Op5), Not(Op4), Op3, Not(Op2), Not(Op1), Not(Op0))  # SW ou ADDI
))
MemtoReg_expr_1 = And(Not(S2), Not(S1), S0, Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0)  # LW
RegWrite_expr_1 = And(S2, Not(S1), Not(S0), Or(
    And(Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0)),  # R-type
    And(Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0),  # LW
    And(Not(Op5), Not(Op4), Op3, Not(Op2), Not(Op1), Not(Op0))  # ADDI
))
MemRead_expr_1 = Or(
    And(Not(S2), Not(S1), Not(S0)),  # Fetch
    And(Not(S2), Not(S1), S0, Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0)  # LW
)
MemWrite_expr_1 = And(Not(S2), Not(S1), S0, Not(Op5), Not(Op4), Op3, Not(Op2), Not(Op1), Not(Op0))  # SW
Branch_expr_1 = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Op1, Not(Op0))  # BEQ
ALUOp1_expr_1 = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0))  # R-type
ALUOp0_expr_1 = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Op1, Not(Op0))  # BEQ
Jump_expr_1 = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Op1, Op0)  # J

# Expressão 2
RegDst_expr_2 = And(S1, Not(Op0), Not(Op1), Not(Op2), Not(Op3), Not(Op4), Not(Op5), Not(S0), Not(S2))
ALUSrc_expr_2 = And(S1, Not(S0), Not(S2), Or(
    And(Op0, Op1, Op2, Not(Op3), Not(Op4), Not(Op5)),  # R-type
    And(Op3, Not(Op0), Not(Op1), Not(Op2), Not(Op4), Not(Op5))  # SW, ADDI
))
MemtoReg_expr_2 = And(Op0, Op1, Op2, S0, Not(Op3), Not(Op4), Not(Op5), Not(S1), Not(S2))  # LW
RegWrite_expr_2 = And(S2, Not(S0), Not(S1), Or(
    And(Op0, Op1, Op2, Not(Op3), Not(Op4), Not(Op5)),  # R-type
    And(Op3, Not(Op0), Not(Op1), Not(Op2), Not(Op4), Not(Op5)),  # SW, ADDI
    And(Not(Op0), Not(Op1), Not(Op2), Not(Op3), Not(Op4), Not(Op5))  # R-type
))
MemRead_expr_2 = Or(
    And(Not(S0), Not(S1), Not(S2)),  # Fetch
    And(Op0, Op1, Op2, S0, Not(Op3), Not(Op4), Not(Op5), Not(S1), Not(S2))  # LW
)
MemWrite_expr_2 = And(Op3, S0, Not(Op0), Not(Op1), Not(Op2), Not(Op4), Not(Op5), Not(S1), Not(S2))  # SW
Branch_expr_2 = And(Op1, S1, Not(Op0), Not(Op2), Not(Op3), Not(Op4), Not(Op5), Not(S0), Not(S2))  # BEQ
ALUOp1_expr_2 = And(S1, Not(Op0), Not(Op1), Not(Op2), Not(Op3), Not(Op4), Not(Op5), Not(S0), Not(S2))  # R-type
ALUOp0_expr_2 = And(Op1, S1, Not(Op0), Not(Op2), Not(Op3), Not(Op4), Not(Op5), Not(S0), Not(S2))  # BEQ
Jump_expr_2 = And(Op0, Op1, S1, Not(Op2), Not(Op3), Not(Op4), Not(Op5), Not(S0), Not(S2))  # J

# Criando o solver Z3
solver = Solver()

# Comparando as expressões
solver.add(RegDst_expr_1 == RegDst_expr_2)
solver.add(ALUSrc_expr_1 == ALUSrc_expr_2)
solver.add(MemtoReg_expr_1 == MemtoReg_expr_2)
solver.add(RegWrite_expr_1 == RegWrite_expr_2)
solver.add(MemRead_expr_1 == MemRead_expr_2)
solver.add(MemWrite_expr_1 == MemWrite_expr_2)
solver.add(Branch_expr_1 == Branch_expr_2)
solver.add(ALUOp1_expr_1 == ALUOp1_expr_2)
solver.add(ALUOp0_expr_1 == ALUOp0_expr_2)
solver.add(Jump_expr_1 == Jump_expr_2)

# Verificando a equivalência
if solver.check() == sat:
    print("As expressões são equivalentes.")
else:
    print("As expressões não são equivalentes.")
