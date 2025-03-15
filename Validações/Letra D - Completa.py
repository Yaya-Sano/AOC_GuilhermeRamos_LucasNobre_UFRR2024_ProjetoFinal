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

# Resolver para verificar a expressão completa
solver = Solver()

# Verificar se a expressão completa é falsa para a condição fornecida
solver.add(Not(F_completa))  # Verificar se a expressão completa é falsa em algum caso específico
solver.add(A == True, B == True, C == True, D == True)  # Especificar entradas para a verificação

if solver.check() == sat:
    print("A expressão completa falhou.")
else:
    print("A expressão completa foi bem-sucedida.")
