from z3 import *

# Definir variáveis A, B, C, D
A, B, C, D = Bools('A B C D')

# Expressão booleana simplificada do circuito
F = Or(
    And(A, C, D),              # A ∧ C ∧ D
    And(A, B, Not(C)),         # A ∧ B ∧ ¬C
    And(B, C, Not(A)),         # B ∧ C ∧ ¬A
    And(D, Not(A), Not(C))     # D ∧ ¬A ∧ ¬C
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
