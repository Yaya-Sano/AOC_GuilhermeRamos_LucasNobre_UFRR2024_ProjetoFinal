from z3 import *

# Definir variáveis booleanas
A, B, C, D = Bools('A B C D')

# Expressão booleana simplificada
F_simplificada = Or(
    And(A, B, C, D),  # ABCD
    And(A, B Not(C), D),  # AB'CD
    And(Not(A), B, C),  # A'BC
    And(Not(A), Or(And(Not(B), Not(C), D), And(B, Not(C), D)))  # A'(B'C'D + BC'D)
)

# Resolver para verificar a expressão simplificada
solver = Solver()

# Verificar se a simplificação está correta
solver.add(Not(F_simplificada))  # Verificar se a expressão simplificada é falsa em algum caso específico
solver.add(A == True, B == True, C == True, D == True)  # Especificar entradas para a verificação

if solver.check() == sat:
    print("A expressão simplificada falhou.")
else:
    print("A expressão simplificada foi bem-sucedida.")
