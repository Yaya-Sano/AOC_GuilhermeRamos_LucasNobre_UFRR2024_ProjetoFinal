from z3 import *

# Definir as variáveis booleanas
pc_update      = Bool('pc_update')
mem_read_instr = Bool('mem_read_instr')
instr_decode   = Bool('instr_decode')
reg_read_1     = Bool('reg_read_1')
reg_read_2     = Bool('reg_read_2')
alu_control    = Bool('alu_control')
alu_execute    = Bool('alu_execute')
reg_write      = Bool('reg_write')

# Expressão booleana completa:
# ((pc_update ∧ mem_read_instr) ∧ (instr_decode ∧ reg_read_1 ∧ reg_read_2) ∧ (alu_control ∧ alu_execute) ∧ reg_write)
expr = And(
    And(pc_update, mem_read_instr),
    And(instr_decode, reg_read_1, reg_read_2),
    And(alu_control, alu_execute),
    reg_write
)

# Configurar o solver para validar a especificação:
# Especificação: a expressão deve ser verdadeira quando todas as variáveis forem True
solver = Solver()
# Adiciona a condição para que a expressão seja falsa (Not(expr))
solver.add(Not(expr))
# Define as condições de entrada para a especificação
solver.add(pc_update == True,
           mem_read_instr == True,
           instr_decode == True,
           reg_read_1 == True,
           reg_read_2 == True,
           alu_control == True,
           alu_execute == True,
           reg_write == True)

# Verifica se a especificação falha (ou seja, se o solver encontra um cenário onde expr é falsa mesmo com todas as entradas True)
if solver.check() == sat:
    print("A especificação falhou.")
else:
    print("A especificação foi atendida.")
