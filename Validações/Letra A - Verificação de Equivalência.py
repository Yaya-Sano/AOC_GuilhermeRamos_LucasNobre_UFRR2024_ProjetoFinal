from z3 import *

# Definir variáveis booleanas
x, y, z = Bools('x y z')

# Expressão booleana completa
F_completa = Or(
    And(Or(Not(x), y), Not(Or(y, And(x, Not(z))))),
    And(x, Not(And(y, z)))
)

# Expressão booleana simplificada proposta
F_simplificada = Or(Not(y), And(x, Not(z)))

# Solver para verificar equivalência
solver = Solver()
solver.add(F_completa != F_simplificada)

# Verificar a equivalência
if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes. A redundância não pode ser removida.")
else:
    print("Os circuitos são equivalentes. A redundância pode ser removida.")
