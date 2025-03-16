from z3 import *

# Definir variáveis A, B, C, D
A, B, C, D = Bools('A B C D')

# Expressão booleana completa
F = Or(
    And(A, B, C, D),                # ABCD
    And(A, B, Not(C), D),            # ABC'D
    And(A, B, Not(C), Not(D)),       # ABC'D'
    And(A, Not(B), C, D),            # AB'CD
    And(Not(A), B, C, D),            # A'BCD
    And(Not(A), B, C, Not(D)),       # A'BCD'
    And(Not(A), B, Not(C), D),       # A'BC'D
    And(Not(A), Not(B), Not(C), D)  # A'B'C'D
)

# Solver para verificar a especificação
solver = Solver()

# Especificação: A saída deve ser verdadeira para uma condição específica
# Exemplo: Verificar se a expressão é verdadeira quando A=True, B=True, C=False, D=True
solver.add(Not(F))  # Verificar se F é falso para a condição especificada
solver.add(A == True, B == True, C == False, D == True)

# Resultado da verificação
if solver.check() == sat:
    print("A especificação falhou.")
else:
    print("A especificação foi atendida.")
