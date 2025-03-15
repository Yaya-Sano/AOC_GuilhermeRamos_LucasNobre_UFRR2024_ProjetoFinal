from z3 import *

# Definir variáveis booleanas
x, y, z = Bools('x y z')

# Expressão booleana simplificada
F_simplificado = Or(And(Or(Not(x), y), Not(And(x, z))), And(x, Not(And(y, z))))

# Solver para verificar a especificação
solver = Solver()

# Exemplo de validação de saída: A saída deve ser verdadeira quando x=True, y=True, z=False
solver.add(Not(F_simplificado))  # Verificar se F é falso para a condição especificada
solver.add(x == True, y == True, z == False)

# Resultado da verificação
if solver.check() == sat:
    print("A especificação falhou.")
else:
    print("A especificação foi atendida.")
