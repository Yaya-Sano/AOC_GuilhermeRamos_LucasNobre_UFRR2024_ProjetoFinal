from z3 import *

# Definir variáveis booleanas
pc_update, mem_read_instr, instr_decode, reg_read_1, reg_read_2 = Bools('pc_update mem_read_instr instr_decode reg_read_1 reg_read_2')
alu_control, alu_execute, reg_write = Bools('alu_control alu_execute reg_write')

# Expressão booleana simplificada
# (pc_update ∧ mem_read_instr ∧ instr_decode ∧ reg_read_1 ∧ reg_read_2 ∧ alu_control ∧ alu_execute ∧ reg_write)
F_simplificado = And(
    pc_update, 
    mem_read_instr, 
    instr_decode, 
    reg_read_1, 
    reg_read_2, 
    alu_control, 
    alu_execute, 
    reg_write
)

# Solver para verificar a especificação
solver = Solver()

# Exemplo de validação de saída: A saída deve ser verdadeira quando todas as variáveis de controle são verdadeiras
solver.add(Not(F_simplificado))  # Verificar se F é falso para a condição especificada
solver.add(
    pc_update == True, 
    mem_read_instr == True, 
    instr_decode == True, 
    reg_read_1 == True, 
    reg_read_2 == True, 
    alu_control == True, 
    alu_execute == True, 
    reg_write == True
)

# Resultado da verificação
if solver.check() == sat:
    print("A especificação falhou.")
else:
    print("A especificação foi atendida.")
