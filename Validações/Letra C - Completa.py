from z3 import *

# Definir variáveis para os sinais de controle
RegDst, ALUOp, MemRead, MemWrite, RegWrite, ALUSrc = Bools('RegDst ALUOp MemRead MemWrite RegWrite ALUSrc')

# Função para a unidade de controle simplificada
def unidade_controle_simplificada(instrucao):
    # Exemplo de simplificação de estados, onde definimos um conjunto menor de sinais para controle
    if instrucao == "ADD":
        return And(RegDst, RegWrite, ALUOp)
    elif instrucao == "LW":
        return And(MemRead, MemWrite, RegWrite, ALUSrc)
    elif instrucao == "SW":
        return And(MemWrite, ALUSrc)
    else:
        return False

# Função para a unidade de controle completa
def unidade_controle_completa(instrucao):
    # Exemplo mais detalhado, com todos os sinais de controle definidos
    if instrucao == "ADD":
        return And(RegDst, ALUOp, RegWrite, Not(ALUSrc))
    elif instrucao == "LW":
        return And(MemRead, RegWrite, ALUSrc)
    elif instrucao == "SW":
        return And(MemWrite, ALUSrc)
    else:
        return False

# Definir a instrução que estamos verificando
instrucao = "ADD"  # Substitua pela instrução desejada para teste

# Verificar a equivalência entre a unidade de controle simplificada e a completa
solver = Solver()

# Verificar se ambas as unidades de controle geram os mesmos sinais para a instrução
solver.add(unidade_controle_simplificada(instrucao) == unidade_controle_completa(instrucao))

# Verificar a equivalência
if solver.check() == sat:
    print(f"As unidades de controle (completa e simplificada) são equivalentes para a instrução {instrucao}.")
else:
    print(f"As unidades de controle (completa e simplificada) NÃO são equivalentes para a instrução {instrucao}.")
