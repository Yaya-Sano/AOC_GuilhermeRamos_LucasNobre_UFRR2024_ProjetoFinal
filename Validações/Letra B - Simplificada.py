from z3 import *

# Criando variáveis booleanas para os bits de entrada e carry-in
A = [Bool(f'A{i}') for i in range(8)]
B = [Bool(f'B{i}') for i in range(8)]
C_in = Bool('C_in')

# Criando variáveis para a soma e carry-out
S = [Bool(f'S{i}') for i in range(8)]
C_out = Bool('C_out')

# Definindo o solver
solver = Solver()

# Implementação do somador completo de 8 bits simplificado
C = C_in  # Carry inicial
for i in range(8):
    # Soma de cada bit (simplificada diretamente usando XOR)
    # Soma (S) = A XOR B XOR Cin
    solver.add(S[i] == Xor(A[i], B[i], C))
    # Atualização do Carry para a próxima iteração (simplificação do carry)
     # Carry de saída (Cout) = (A AND B) OR (Cin AND (A XOR B))
    C = Or(And(A[i], B[i]), And(C, Xor(A[i], B[i])))

# Definir a saída final do carry
solver.add(C_out == C)

# Testando uma entrada específica: A = 10101010, B = 01010101, C_in = 0
entrada_A = [True, False, True, False, True, False, True, False]  # 170 em binário
entrada_B = [False, True, False, True, False, True, False, True]  # 85 em binário
carry_inicial = False

# Adicionando as restrições das entradas ao solver
for i in range(8):
    solver.add(A[i] == entrada_A[i])
    solver.add(B[i] == entrada_B[i])

solver.add(C_in == carry_inicial)

# Verificando a especificação
if solver.check() == sat:
    modelo = solver.model()
    soma_resultante = ''.join(['1' if modelo.evaluate(S[i]) else '0' for i in range(8)])
    carry_out_resultante = modelo.evaluate(C_out)
    
    print(f"Soma: {soma_resultante} (binário)")
    print(f"Carry-out: {carry_out_resultante}")
else:
    print("A especificação falhou.")
