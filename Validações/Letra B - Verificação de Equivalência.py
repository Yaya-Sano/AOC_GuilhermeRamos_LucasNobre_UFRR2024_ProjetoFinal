from z3 import *

# Definir variáveis booleanas para os bits de entrada e carry-in
A = [Bool(f'A{i}') for i in range(8)]
B = [Bool(f'B{i}') for i in range(8)]
C_in = Bool('C_in')

# Criar variáveis para a soma e carry-out
S_completo = [Bool(f'S_completo{i}') for i in range(8)]
C_out_completo = Bool('C_out_completo')
S_simplificado = [Bool(f'S_simplificado{i}') for i in range(8)]
C_out_simplificado = Bool('C_out_simplificado')

# Definir o solver
solver = Solver()

# Implementação do somador completo de 8 bits
C_completo = C_in  # Carry inicial
for i in range(8):
    # Soma de cada bit para o somador completo
    solver.add(S_completo[i] == Xor(A[i], B[i], C_completo))
    # Atualização do Carry para a próxima iteração
    C_completo = Or(And(A[i], B[i]), And(C_completo, Xor(A[i], B[i])))

# Implementação do somador simplificado de 8 bits
C_simplificado = C_in  # Carry inicial
for i in range(8):
    # Soma de cada bit para o somador simplificado
    solver.add(S_simplificado[i] == Xor(A[i], B[i], C_simplificado))
    # Atualização do Carry para a próxima iteração
    C_simplificado = Or(And(A[i], B[i]), And(C_simplificado, Xor(A[i], B[i])))

# Definir a saída final do carry para ambos os circuitos
solver.add(C_out_completo == C_completo)
solver.add(C_out_simplificado == C_simplificado)

# Verificar se os dois circuitos são equivalentes
solver.add(S_completo == S_simplificado)  # A soma deve ser igual
solver.add(C_out_completo == C_out_simplificado)  # O carry final também deve ser igual

# Verificar se a equivalência é atendida
if solver.check() == sat:
    print("Os circuitos NÃO são equivalentes.")
else:
    print("Os circuitos são equivalentes.")
