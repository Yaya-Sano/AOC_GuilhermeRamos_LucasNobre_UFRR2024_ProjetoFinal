from z3 import *

# Definir variáveis para os sinais de controle simplificados
RegWrite, ALUSrc, MemRead, MemWrite, ALUOp = Bools('RegWrite ALUSrc MemRead MemWrite ALUOp')

# Função simplificada para a unidade de controle (em um modelo de estados reduzido)
def unidade_controle_simplificada(instrucao):
    # A simplificação envolve apenas alguns sinais básicos para cada tipo de instrução
    if instrucao == "ADD":  # Exemplo: soma
        return And(RegWrite, Not(ALUSrc), ALUOp)
    elif instrucao == "LW":  # Exemplo: load
        return And(MemRead, RegWrite, ALUSrc)
    elif instrucao == "SW":  # Exemplo: store
        return And(MemWrite, ALUSrc)
    else:
        return False

# Verificar o comportamento da unidade de controle simplificada para uma instrução específica
instrucao = "ADD"  # Você pode trocar a instrução para "LW", "SW", ou outras conforme necessário

# Solver para verificar os sinais de controle
solver = Solver()

# Verificar se a unidade de controle simplificada gera os sinais corretamente
solver.add(unidade_controle_simplificada(instrucao))

# Resultado da verificação
if solver.check() == sat:
    print(f"A unidade de controle simplificada gerou os sinais de controle corretamente para a instrução {instrucao}.")
else:
    print(f"A unidade de controle simplificada NÃO gerou os sinais de controle corretamente para a instrução {instrucao}.")
