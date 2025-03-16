from z3 import *

# Funções que modelam as operações da ULA

def subtrator_1bit(A, B, Bin):
    """
    Subtrator completo de 1 bit:
      Diferença = A ⊕ B ⊕ Bin
      Empréstimo = (¬A ʌ B) v ((A ⊕ B) ʌ Bin)
    """
    Diff = Xor(Xor(A, B), Bin)
    Borrow = Or(And(Not(A), B), And(Xor(A, B), Bin))
    return Diff, Borrow

def xor_bit(A, B):
    """
    Operação XOR bit a bit.
    """
    return Xor(A, B)

def nand_bit(A, B):
    """
    Operação NAND bit a bit = ¬(A ʌ B)
    """
    return Not(And(A, B))

def nor_bit(A, B):
    """
    Operação NOR bit a bit = ¬(A v B)
    """
    return Not(Or(A, B))

def shift_left_2(A_bits):
    """
    Deslocamento lógico para a esquerda em 2 bits para um vetor de 8 bits.
    Para i < 2, a saída é 0 (False); para i>=2, S[i] = A[i-2].
    """
    S = []
    for i in range(8):
        if i < 2:
            S.append(False)
        else:
            S.append(A_bits[i-2])
    return S

# Função para formatação das expressões para exibição legível
def format_expr(expr):
    if is_true(expr):
        return "True"
    elif is_false(expr):
        return "False"
    else:
        return str(expr)

# ------------------------------------------------
# Testes de Verificação com Z3 para cada operação
# ------------------------------------------------

def teste_subtrator():
    # Teste para o subtrator de 1 bit:
    # Especificação: Se A0=True, B0=False e Bin=False, então Diff deve ser True e Borrow False.
    A0, B0, Bin = Bools('A0 B0 Bin')
    Diff, Borrow = subtrator_1bit(A0, B0, Bin)
    
    # Verificar Diferença:
    solver_diff = Solver()
    solver_diff.add(A0 == True, B0 == False, Bin == False)
    # Adiciona restrição que Diferença seja FALSA (contrário do esperado)
    solver_diff.add(Diff == False)
    if solver_diff.check() == sat:
        print("Subtrator 1-bit: Especificação da DIFERENÇA falhou.")
    else:
        print("Subtrator 1-bit: Especificação da DIFERENÇA atendida.")
    
    # Verificar Empréstimo:
    solver_borrow = Solver()
    solver_borrow.add(A0 == True, B0 == False, Bin == False)
    # Especificação: Borrow deve ser False; forçamos Borrow == True para testar
    solver_borrow.add(Borrow == True)
    if solver_borrow.check() == sat:
        print("Subtrator 1-bit: Especificação do EMPRÉSTIMO falhou.")
    else:
        print("Subtrator 1-bit: Especificação do EMPRÉSTIMO atendida.")

def teste_xor():
    # Teste para XOR: se A0=True, B0=False, o resultado deve ser True.
    A0, B0 = Bools('A0 B0')
    X = xor_bit(A0, B0)
    solver = Solver()
    solver.add(A0 == True, B0 == False)
    solver.add(X == False)
    if solver.check() == sat:
        print("XOR: Especificação falhou.")
    else:
        print("XOR: Especificação atendida.")

def teste_nand():
    # Teste para NAND: se A0=True, B0=True, o resultado deve ser False.
    A0, B0 = Bools('A0 B0')
    N = nand_bit(A0, B0)
    solver = Solver()
    solver.add(A0 == True, B0 == True)
    solver.add(N == True)
    if solver.check() == sat:
        print("NAND: Especificação falhou.")
    else:
        print("NAND: Especificação atendida.")

def teste_nor():
    # Teste para NOR: se A0=False, B0=False, o resultado deve ser True.
    A0, B0 = Bools('A0 B0')
    N = nor_bit(A0, B0)
    solver = Solver()
    solver.add(A0 == False, B0 == False)
    solver.add(N == False)
    if solver.check() == sat:
        print("NOR: Especificação falhou.")
    else:
        print("NOR: Especificação atendida.")

def teste_shift_left_2():
    # Teste para Shift Left 2 bits: para uma entrada A = [A0,...,A7],
    # a saída deve ser S[0]=False, S[1]=False, S[2]=A0, S[3]=A1, ..., S[7]=A5.
    # Usamos um exemplo fixo: A0=True, A1=False, A2=True, A3=False, A4=True, A5=False, A6=True, A7=False.
    A0, A1, A2, A3, A4, A5, A6, A7 = Bools('A0 A1 A2 A3 A4 A5 A6 A7')
    A_bits = [A0, A1, A2, A3, A4, A5, A6, A7]
    S = shift_left_2(A_bits)
    
    # Teste: S[0] deve ser False. Verificamos adicionando S[0]==True e esperar insat.
    solver0 = Solver()
    solver0.add(A0 == True, A1 == False, A2 == True, A3 == False, A4 == True, A5 == False, A6 == True, A7 == False)
    # Forçamos S[0] para True (errado)
    solver0.add(S[0] == True)
    if solver0.check() == sat:
        print("Shift Left 2 bits: Especificação falhou para S[0] (não é 0).")
    else:
        print("Shift Left 2 bits: Especificação atendida para S[0] = 0.")
    
    # Teste: S[2] deve ser igual a A0 (que é True)
    solver2 = Solver()
    solver2.add(A0 == True, A1 == False, A2 == True, A3 == False, A4 == True, A5 == False, A6 == True, A7 == False)
    solver2.add(S[2] == False)
    if solver2.check() == sat:
        print("Shift Left 2 bits: Especificação falhou para S[2] (não é igual a A0).")
    else:
        print("Shift Left 2 bits: Especificação atendida para S[2] = A0.")

def main():
    print("Verificação da ULA de 8 bits - Funções com Z3\n")
    teste_subtrator()
    teste_xor()
    teste_nand()
    teste_nor()
    teste_shift_left_2()

if __name__ == '__main__':
    main()
