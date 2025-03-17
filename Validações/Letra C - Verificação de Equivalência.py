from z3 import *

# Definir variáveis de estado e opcode
S2, S1, S0 = Bools('S2 S1 S0')  # Bits de estado
Op5, Op4, Op3, Op2, Op1, Op0 = Bools('Op5 Op4 Op3 Op2 Op1 Op0')  # Bits do opcode

# Definir variáveis de saída (sinais de controle)
RegDst, ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, ALUOp1, ALUOp0, Jump = Bools(
    'RegDst ALUSrc MemtoReg RegWrite MemRead MemWrite Branch ALUOp1 ALUOp0 Jump'
)

# Expressão booleana completa (original)
RegDst_completo = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0))
ALUSrc_completo = And(Not(S2), S1, Not(S0), Or(
    And(Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0),  # LW
    And(Not(Op5), Not(Op4), Op3, Not(Op2), Not(Op1), Not(Op0))  # SW ou ADDI
))
MemtoReg_completo = And(Not(S2), Not(S1), S0, Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0)  # LW
RegWrite_completo = And(S2, Not(S1), Not(S0), Or(
    And(Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0)),  # R-type
    And(Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0),  # LW
    And(Not(Op5), Not(Op4), Op3, Not(Op2), Not(Op1), Not(Op0))  # ADDI
))
MemRead_completo = Or(
    And(Not(S2), Not(S1), Not(S0)),  # Fetch
    And(Not(S2), Not(S1), S0, Not(Op5), Not(Op4), Not(Op3), Op2, Op1, Op0)  # LW
)
MemWrite_completo = And(Not(S2), Not(S1), S0, Not(Op5), Not(Op4), Op3, Not(Op2), Not(Op1), Not(Op0))  # SW
Branch_completo = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Op1, Not(Op0))  # BEQ
ALUOp1_completo = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0))  # R-type
ALUOp0_completo = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Op1, Not(Op0))  # BEQ
Jump_completo = And(Not(S2), S1, Not(S0), Not(Op5), Not(Op4), Not(Op3), Not(Op2), Op1, Op0)  # J

# Expressão booleana simplificada (hipotética)
RegDst_simplificado = And(S1, Not(S0), Not(Op0))
ALUSrc_simplificado = And(S1, Or(Op2, Op1))
MemtoReg_simplificado = And(S0, Op2, Op1)
RegWrite_simplificado = Or(And(Not(S2), Not(S1), Not(S0)), And(S1, Op0))
MemRead_simplificado = Or(And(Not(S2), Not(S1), Not(S0)), And(S0, Op2, Op1))
MemWrite_simplificado = And(S0, Not(Op3), Not(Op2))
Branch_simplificado = And(S1, Not(Op1), Not(Op0))
ALUOp1_simplificado = And(S1, Not(Op0))
ALUOp0_simplificado = And(S1, Not(Op1))
Jump_simplificado = And(S1, Op1, Op0)

# Solver para verificar equivalência
solver = Solver()

# Adicionar condição de inequivalência (se forem diferentes, há um problema)
solver.add(RegDst_completo != RegDst_simplificado)
solver.add(ALUSrc_completo != ALUSrc_simplificado)
solver.add(MemtoReg_completo != MemtoReg_simplificado)
solver.add(RegWrite_completo != RegWrite_simplificado)
solver.add(MemRead_completo != MemRead_simplificado)
solver.add(MemWrite_completo != MemWrite_simplificado)
solver.add(Branch_completo != Branch_simplificado)
solver.add(ALUOp1_completo != ALUOp1_simplificado)
solver.add(ALUOp0_completo != ALUOp0_simplificado)
solver.add(Jump_completo != Jump_simplificado)

# Verificar equivalência
if solver.check() == sat:
    print("As fórmulas NÃO são equivalentes. A simplificação não é válida.")
else:
    print("As fórmulas são equivalentes. A simplificação é válida.")
