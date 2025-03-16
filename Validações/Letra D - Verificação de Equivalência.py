from z3 import *

# Definir variáveis A, B, C, D
A, B, C, D = Bools('A B C D')

# Circuito original (com redundância)
F_original = Or(
    And(A, B, C, D),              # ABCD
    And(A, B, Not(C), D),         # ABC'D
    And(A, B, Not(C), Not(D)),    # ABC'D'
    And(A, Not(B), C, D),         # AB'CD
    And(Not(A), B, C, D),         # A'BCD
    And(Not(A), B, C, Not(D)),    # A'BCD'
    And(Not(A), B, Not(C), D),    # A'BC'D
    And(Not(A), Not(B), Not(C), D) # A'B'C'D
)

# Circuito simplificado (sem redundância)
F_simplificado = Or(
    And(A, C, D),                # A ∧ C ∧ D
    And(A, B, Not(C)),           # A ∧ B ∧ ¬C
    And(B, C, Not(A)),           # B ∧ C ∧ ¬A
    And(D, Not(A), Not(C))       # D ∧ ¬A ∧ ¬C
)

# Solver para verificar equivalência
solver = Solver()

# Adicionar condição de inequivalência (se forem diferentes, há um problema)
solver.add(F_original != F_simplificado)

# Verificar
if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes. A redundância não pode ser removida.")
else:
    print("Os circuitos são equivalentes. A redundância pode ser removida.")
