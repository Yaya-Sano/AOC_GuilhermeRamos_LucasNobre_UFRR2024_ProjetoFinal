from z3 import *

# Definindo o Z3 solver
solver = Solver()

# Variáveis de entrada para 8 bits
A = [Bool(f'A{i}') for i in range(8)]  # Bits de A (A0..A7)
B = [Bool(f'B{i}') for i in range(8)]  # Bits de B (B0..B7)
Cin = [Bool(f'Cin{i}') for i in range(8)]  # Carries de entrada (Cin0..Cin7)

# Variáveis de saída: Soma (S0..S7) e Carry (Cout)
S = [Bool(f'S{i}') for i in range(8)]  # Soma de 8 bits
Cout = [Bool(f'Cout{i}') for i in range(8)]  # Carry de 8 bits (Cout0..Cout7)

# Funções para o somador completo de 1 bit
def full_adder(a, b, cin):
    sum_bit = Xor(Xor(a, b), cin)  # Soma
    carry_out = Or(And(a, b), And(cin, Xor(a, b)))  # Carry-out
    return sum_bit, carry_out

# Adicionando as restrições para o somador completo de 8 bits
for i in range(8):
    if i == 0:
        sum_bit, carry_out = full_adder(A[i], B[i], Cin[i])
    else:
        sum_bit, carry_out = full_adder(A[i], B[i], Cout[i-1])  # Carry anterior
    
    solver.add(S[i] == sum_bit)
    solver.add(Cout[i] == carry_out)

# Verificação de uma combinação específica de entradas
solver.push()  # Salva o estado atual do solver
solver.add(A[0] == True, A[1] == False, A[2] == True, A[3] == False,  # Exemplo de entradas
           A[4] == True, A[5] == False, A[6] == True, A[7] == False)
solver.add(B[0] == False, B[1] == True, B[2] == False, B[3] == True,
           B[4] == False, B[5] == True, B[6] == False, B[7] == True)
solver.add(Cin[0] == False, Cin[1] == False, Cin[2] == False, Cin[3] == False,
           Cin[4] == False, Cin[5] == False, Cin[6] == False, Cin[7] == False)

# Verificar se as entradas satisfazem a restrição
if solver.check() == sat:
    model = solver.model()
    print("Soma: ", [model[S[i]] for i in range(8)])
    print("Carry-out: ", [model[Cout[i]] for i in range(8)])
else:
    print("Solução não encontrada.")

solver.pop()  # Restaura o estado anterior do solver
