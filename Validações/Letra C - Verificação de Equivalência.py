from z3 import *

# Definir variáveis para os sinais de controle
RegDst, ALUOp, MemRead, MemWrite, RegWrite, ALUSrc = Bools('RegDst ALUOp MemRead MemWrite RegWrite ALUSrc')

# Função para a unidade de controle completa
def unidade_controle_completa(instrucao):
    if instrucao == "ADD":
        return And(RegDst, ALUOp, RegWrite, Not(ALUSrc))
    elif instrucao == "LW":
        return And(MemRead, RegWrite, ALUSrc)
    elif instrucao == "SW":
        return And(MemWrite, ALUSrc)
    else:
        return False

# Função para a unidade de controle simplificada
def unidade_controle_simplificada(instrucao):
    if instrucao == "ADD":
        return And(RegWrite, Not(ALUSrc), ALUOp)
    elif instrucao == "LW":
        return And(MemRead, RegWrite, ALUSrc)
    elif instrucao == "SW":
        return And(MemWrite, ALUSrc)
    else:
        return False

# Verificar equivalência entre a unidade de controle completa e a simplificada
def verificar_equivalencia(instrucao):
    solver = Solver()

    # Obter a expressão da unidade de controle completa e simplificada
    controle_completo = unidade_controle_completa(instrucao)
    controle_simplificado = unidade_controle_simplificada(instrucao)

    # Adicionar a condição de que os controles devem ser equivalentes
    solver.add(controle_completo == controle_simplificado)

    # Verificar se a equivalência é verdadeira
    if solver.check() == sat:
        print(f"As unidades de controle (completa e simplificada) NÃO são equivalentes para a instrução {instrucao}.")
    else:
        print(f"As unidades de controle (completa e simplificada) SÃO equivalentes para a instrução {instrucao}.")

# Testar para uma instrução específica
instrucao = "ADD"  # Pode trocar para "LW", "SW" ou outras instruções conforme necessário
verificar_equivalencia(instrucao)
