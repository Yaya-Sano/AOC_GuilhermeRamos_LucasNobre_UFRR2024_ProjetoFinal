from z3 import *

# Definir variáveis booleanas
A, B, C, D = Bools('A B C D')

# Expressão booleana simplificada
F_simplificada = Or(
    And(A, C, D),  # A ∧ C ∧ D
    And(A, B, Not(C)),  # A ∧ B ∧ ¬C
    And(B, C, Not(A)),  # B ∧ C ∧ ¬A
    And(D, Not(A), Not(C))  # D ∧ ¬A ∧ ¬C
)

# Solver para verificar a expressão
solver = Solver()

# Adicionar a expressão booleana simplificada
solver.add(F_simplificada)

# Verificar se a expressão é satisfatível
if solver.check() == sat:
    print("A expressão é satisfatível.")
else:
    print("A expressão não é satisfatível.")
