from z3 import *

# Definir variáveis booleanas
A, B, C, D = Bools('A B C D')

# Expressão booleana completa
F_completa = Or(
    And(A, B, C, D),  # ABCD
    And(A, B, Not(C), D),  # ABC'D
    And(A, B, Not(C), Not(D)),  # ABC'D'
    And(A, Not(B), C, D),  # AB'CD
    And(Not(A), B, C, D),  # A'BCD
    And(Not(A), B, C, Not(D)),  # A'BCD'
    And(Not(A), B, Not(C), D),  # A'BC'D
    And(Not(A), Not(B), Not(C), D)  # A'B'C'D
)

# Expressão booleana simplificada fornecida
F_simplificada = Or(
    And(A, C, D),  # A ∧ C ∧ D
    And(A, B, Not(C)),  # A ∧ B ∧ ¬C
    And(B, C, Not(A)),  # B ∧ C ∧ ¬A
    And(D, Not(A), Not(C))  # D ∧ ¬A ∧ ¬C
)

# Resolver para verificar a equivalência entre a expressão completa e simplificada
solver = Solver()

# Adicionar a condição de inequivalência
solver.add(F_completa != F_simplificada)

# Verificar a equivalência
if solver.check() == sat:
    print("As expressões completa e simplificada NÃO são equivalentes.")
else:
    print("As expressões completa e simplificada SÃO equivalentes.")
