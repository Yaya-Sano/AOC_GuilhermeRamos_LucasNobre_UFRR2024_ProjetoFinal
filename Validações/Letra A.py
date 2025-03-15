from z3 import *

# Definição das variáveis booleanas
x, y, z = Bools('x y z')

# Definição da fórmula lógica
F = Or(
    And(Not(x) | y, Not(Or(y, And(x, Not(z))))),
    And(x, Not(And(y, z)))
)

# Criando um solver
solver = Solver()
solver.add(F == True)

# Verificando a satisfatibilidade da função
if solver.check() == sat:
    print("A fórmula é satisfatível. Um modelo possível:")
    print(solver.model())
else:
    print("A fórmula é insatisfatível.")
