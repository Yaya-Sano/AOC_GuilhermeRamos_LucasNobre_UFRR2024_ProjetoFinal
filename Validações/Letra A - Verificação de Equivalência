from z3 import *

# Definir variáveis booleanas
x, y, z = Bools('x y z')

# Expressão booleana completa
F_completa = Or(And(Or(Not(x), y), Not(And(y, And(x, Not(z))))), And(x, Not(And(y, z))))

# Expressão booleana simplificada
F_simplificada = Or(And(Or(Not(x), y), Not(And(x, z))), And(x, Not(And(y, z))))

# Solver para verificar equivalência
solver = Solver()

# Adicionar condição de inequivalência (se forem diferentes, há um problema)
solver.add(F_completa != F_simplificada)

# Verificar
if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes. A redundância não pode ser removida.")
else:
    print("Os circuitos são equivalentes. A redundância pode ser removida.")
