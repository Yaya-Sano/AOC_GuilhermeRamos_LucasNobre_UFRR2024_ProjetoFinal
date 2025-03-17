from z3 import *

#Definir variáveis booleanas para cada sinal
pc_update      = Bool('pc_update')
mem_read_instr = Bool('mem_read_instr')
instr_decode   = Bool('instr_decode')
reg_read_1     = Bool('reg_read_1')
reg_read_2     = Bool('reg_read_2')
alu_control    = Bool('alu_control')
alu_execute    = Bool('alu_execute')
reg_write      = Bool('reg_write')

#Expressão booleana completa:
#((pc_update ∧ mem_read_instr) ∧ (instr_decode ∧ reg_read_1 ∧ reg_read_2) ∧ (alu_control ∧ alu_execute) ∧ reg_write)
F = And(
    And(pc_update, mem_read_instr),
    And(instr_decode, reg_read_1, reg_read_2),
    And(alu_control, alu_execute),
    reg_write
)

#Criação do solver
solver = Solver()

#Especificação: A saída F deve ser verdadeira quando todas as entradas forem True.
solver.add(Not(F))
solver.add(pc_update      == True)
solver.add(mem_read_instr == True)
solver.add(instr_decode   == True)
solver.add(reg_read_1     == True)
solver.add(reg_read_2     == True)
solver.add(alu_control    == True)
solver.add(alu_execute    == True)
solver.add(reg_write      == True)

#Verificar se a especificação foi atendida
if solver.check() == sat:
    print("A especificação falhou.")
else:
    print("A especificação foi atendida.")
