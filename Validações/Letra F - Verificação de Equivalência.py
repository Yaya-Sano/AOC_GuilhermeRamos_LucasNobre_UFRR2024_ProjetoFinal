from z3 import *

# Definir variáveis booleanas
pc_update, mem_read_instr, instr_decode, reg_read_1, reg_read_2 = Bools('pc_update mem_read_instr instr_decode reg_read_1 reg_read_2')
alu_control, alu_execute, reg_write = Bools('alu_control alu_execute reg_write')

# Expressão booleana original (com redundância)
F_original = And(
    And(pc_update, mem_read_instr),
    And(instr_decode, reg_read_1, reg_read_2),
    And(alu_control, alu_execute),
    reg_write
)

# Expressão booleana simplificada (sem redundância)
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

# Solver para verificar equivalência
solver = Solver()

# Adicionar condição de inequivalência (se forem diferentes, há um problema)
solver.add(F_original != F_simplificado)

# Verificar
if solver.check() == sat:
    print("As fórmulas NÃO são equivalentes. A redundância não pode ser removida.")
else:
    print("As fórmulas são equivalentes. A redundância pode ser removida.")
