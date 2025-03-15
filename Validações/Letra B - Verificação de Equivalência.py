from z3 import *

# Definir variáveis booleanas para os 8 bits de A, B e C_in
A = [Bools(f'A{i}') for i in range(8)]
B = [Bools(f'B{i}') for i in range(8)]
C_in = Bools('C_in')

# Definir variáveis booleanas para os 8 bits de soma S e carry out
S = [Bools(f'S{i}') for i in range(8)]
C_out = Bools('C_out')

# Função para somador completo de 1 bit (completo)
def somador_completo(Ai, Bi, Cin):
    S = Xor(Xor(Ai, Bi), Cin)
    C = Or(And(Ai, Bi), And(Bi, Cin), And(Ai, Cin))
    return S, C

# Função para somador completo simplificado de 1 bit (simplificado)
def somador_completo_simplificado(Ai, Bi, Cin):
    S = Xor(Xor(Ai, Bi), Cin)
    C = Or(And(Ai, Bi), And(Bi, Cin))  # Simplificação: sem a combinação extra de gates
    return S, C

# Equações para o somador completo de 8 bits (completo)
S_eq_completo = [somador_completo(A[i], B[i], C_in if i == 0 else C_out[i-1])[0] for i in range(8)]
C_out_eq_completo = [somador_completo(A[i], B[i], C_in if i == 0 else C_out[i-1])[1] for i in range(8)]

# Equações para o somador completo de 8 bits (simplificado)
S_eq_simplificado = [somador_completo_simplificado(A[i], B[i], C_in if i == 0 else C_out[i-1])[0] for i in range(8)]
C_out_eq_simplificado = [somador_completo_simplificado(A[i], B[i], C_in if i == 0 else C_out[i-1])[1] for i in range(8)]

# Solver para verificar a equivalência
solver = Solver()

# Adicionar as equações para o somador completo (completo)
for i in range(8):
    solver.add(S[i] == S_eq_completo[i])  # Adicionar as equações do somador completo
solver.add(C_out == C_out_eq_completo[7])  # Verificar o carry final do somador completo

# Adicionar as equações para o somador simplificado
for i in range(8):
    solver.add(S[i] == S_eq_simplificado[i])  # Adicionar as equações do somador simplificado
solver.add(C_out == C_out_eq_simplificado[7])  # Verificar o carry final do somador simplificado

# Verificar se a equivalência é verdadeira
if solver.check() == sat:
    print("As expressões completas e simplificadas são equivalentes.")
else:
    print("As expressões completas e simplificadas NÃO são equivalentes.")
