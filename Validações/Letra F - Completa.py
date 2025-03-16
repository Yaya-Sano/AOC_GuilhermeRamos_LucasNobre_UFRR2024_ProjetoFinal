from z3 import *

# Definir as variáveis booleanas para os bits do opcode
op5, op4, op3, op2, op1, op0 = Bools('op5 op4 op3 op2 op1 op0')

# Expressões booleanas dos sinais de controle para uma instrução R
# Para opcode R: op = 000000
RegDst   = And(Not(op5), Not(op4), Not(op3), Not(op2), Not(op1), Not(op0))
ALUSrc   = False   # Como a operação usa ambos os registradores, ALUSrc é 0
MemToReg = False   # O dado vem da ALU e não da memória
RegWrite = True    # A instrução R escreve no registrador destino
MemRead  = False
MemWrite = False
Branch   = False
# ALUOp é representado por dois bits: para instrução R, ALUOp = 10
ALUOp1 = True
ALUOp0 = False

# Criação do solver Z3
solver = Solver()

# Especificação: Para opcode R, todos os bits do opcode devem ser False.
solver.add(op5 == False, op4 == False, op3 == False, op2 == False, op1 == False, op0 == False)

# Validação de saída: RegDst deve ser verdadeiro para opcode R.
# Se adicionarmos Not(RegDst) e o solver encontrar uma atribuição, significa que a especificação falhou.
solver.add(Not(RegDst))

# Verifica se há uma contradição com a especificação:
if solver.check() == sat:
    print("Especificação falhou: RegDst não está verdadeiro para opcode R.")
else:
    print("Especificação atendida: RegDst está verdadeiro para opcode R.")

# ---------------------------------------------------
# Caso queira validar outros sinais, pode-se repetir o processo. Por exemplo, para ALUSrc:
solver.reset()
solver.add(op5 == False, op4 == False, op3 == False, op2 == False, op1 == False, op0 == False)
# ALUSrc deve ser falso, logo, se adicionarmos ALUSrc (i.e. True) a especificação, falha.
solver.add(ALUSrc)  # se ALUSrc for True, a verificação falha.
if solver.check() == sat:
    print("Especificação falhou: ALUSrc não está falso para opcode R.")
else:
    print("Especificação atendida: ALUSrc está falso para opcode R.")
