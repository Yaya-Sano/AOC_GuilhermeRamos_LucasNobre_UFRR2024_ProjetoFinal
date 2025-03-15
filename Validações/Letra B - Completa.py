from z3 import *

# Definir variáveis booleanas para os 8 bits de A, B e C_in
A = [Bools(f'A{i}') for i in range(8)]
B = [Bools(f'B{i}') for i in range(8)]
C_in = Bools('C_in')

# Definir variáveis booleanas para os 8 bits de soma S e carry out
S = [Bools(f'S{i}') for i in range(8)]
C_out = Bools('C_out')

# Função para somador completo de 1 bit
def somador_completo(Ai, Bi, Cin):
    S = Xor(Xor(Ai, Bi), Cin)
    C = Or(And(Ai, Bi), And(Bi, Cin), And(Ai, Cin))
    return S, C

# Equações para o somador completo de 8 bits
S_eq = [somador_completo(A[i], B[i], C_in if i == 0 else C_out[i-1])[0] for i in range(8)]
C_out_eq = [somador_completo(A[i], B[i], C_in if i == 0 else C_out[i-1])[1] for i in range(8)]

# Solver para verificar a equivalência
solver = Solver()

# Adicionar as equações para os somadores
for i in range(8):
    solver.add(S[i] == S_eq[i])
solver.add(C_out == C_out_eq[7])  # Verificar o carry final

# Verificar se a equivalência é verdadeira
if solver.check() == sat:
    print("A expressão completa foi modelada corretamente.")
else:
    print("A expressão completa não foi modelada corretamente.")
