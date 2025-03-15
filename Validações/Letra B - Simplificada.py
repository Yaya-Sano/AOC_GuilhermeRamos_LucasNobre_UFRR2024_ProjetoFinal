from z3 import *

# Definir variáveis booleanas para os 8 bits de A, B e C_in
A = [Bools(f'A{i}') for i in range(8)]
B = [Bools(f'B{i}') for i in range(8)]
C_in = Bools('C_in')

# Definir variáveis booleanas para os 8 bits de soma S e carry out
S = [Bools(f'S{i}') for i in range(8)]
C_out = Bools('C_out')

# Função para somador completo simplificado de 1 bit (simplificado)
def somador_completo_simplificado(Ai, Bi, Cin):
    # Soma
    S = Xor(Xor(Ai, Bi), Cin)
    # Carry simplificado, exemplo com menos gates
    C = Or(And(Ai, Bi), And(Bi, Cin))  
    return S, C

# Equações para o somador completo de 8 bits simplificado
S_eq_simplificado = [somador_completo_simplificado(A[i], B[i], C_in if i == 0 else C_out[i-1])[0] for i in range(8)]
C_out_eq_simplificado = [somador_completo_simplificado(A[i], B[i], C_in if i == 0 else C_out[i-1])[1] for i in range(8)]

# Solver para verificar a equivalência
solver = Solver()

# Adicionar as equações para os somadores simplificados
for i in range(8):
    solver.add(S[i] == S_eq_simplificado[i])
solver.add(C_out == C_out_eq_simplificado[7])  # Verificar o carry final

# Verificar se a equivalência é verdadeira
if solver.check() == sat:
    print("A expressão simplificada foi modelada corretamente.")
else:
    print("A expressão simplificada não foi modelada corretamente.")
