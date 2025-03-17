from z3 import *

# Definir variáveis de estado e opcode
S2, S1, S0 = Bools('S2 S1 S0')  # Bits de estado
Op5, Op4, Op3, Op2, Op1, Op0 = Bools('Op5 Op4 Op3 Op2 Op1 Op0')  # Bits do opcode

# Definir variáveis de saída (sinais de controle)
RegDst, ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, ALUOp1, ALUOp0, Jump = Bools(
    'RegDst ALUSrc MemtoReg RegWrite MemRead MemWrite Branch ALUOp1 ALUOp0 Jump'
)

# Expressões booleanas completas
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

# Criar o solver
solver = Solver()

# Adicionar as expressões ao solver
solver.add(RegDst == RegDst_expr)
solver.add(ALUSrc == ALUSrc_expr)
solver.add(MemtoReg == MemtoReg_expr)
solver.add(RegWrite == RegWrite_expr)
solver.add(MemRead == MemRead_expr)
solver.add(MemWrite == MemWrite_expr)
solver.add(Branch == Branch_expr)
solver.add(ALUOp1 == ALUOp1_expr)
solver.add(ALUOp0 == ALUOp0_expr)
solver.add(Jump == Jump_expr)

# Validação de saída: Verificar se a saída atende a uma condição específica
# Exemplo: Verificar se, no estado Fetch (S2=0, S1=0, S0=0), MemRead é True
solver.push()  # Salvar o estado atual do solver
solver.add(Not(MemRead))  # Verificar se MemRead é False (condição de falha)
solver.add(Not(S2), Not(S1), Not(S0))  # Estado Fetch

# Resultado da verificação
if solver.check() == sat:
    print("A especificação falhou: MemRead não é True no estado Fetch.")
else:
    print("A especificação foi atendida: MemRead é True no estado Fetch.")
solver.pop()  # Restaurar o estado anterior do solver

# Outro exemplo: Verificar se, no estado Execute (S2=0, S1=1, S0=0) com opcode R-type, ALUOp1 é True
solver.push()
solver.add(Not(ALUOp1))  # Verificar se ALUOp1 é False (condição de falha)
solver.add(Not(S2), S1, Not(S0))  # Estado Execute
solver.add(Not(Op5), Not(Op4), Not(Op3), Not(Op2), Not(Op1), Not(Op0))  # Opcode R-type

# Resultado da verificação
if solver.check() == sat:
    print("A especificação falhou: ALUOp1 não é True no estado Execute com opcode R-type.")
else:
    print("A especificação foi atendida: ALUOp1 é True no estado Execute com opcode R-type.")
solver.pop()
