from z3 import *

# Definir variáveis para os sinais de controle
PCWrite, IRWrite, MemRead, MemWrite, RegDst, RegWrite, MemtoReg, ALUSrcA, ALUSrcB = Bools('PCWrite IRWrite MemRead MemWrite RegDst RegWrite MemtoReg ALUSrcA ALUSrcB')
ALUOp_add, ALUOp_sub, ALUOp = Bools('ALUOp_add ALUOp_sub ALUOp')

# Função para a unidade de controle completa
def unidade_controle_completa(instrucao):
    if instrucao == "ADD":  # Instrução R
        return And(RegDst, RegWrite, Not(ALUSrcA), ALUSrcB, ALUOp_add, Not(ALUOp_sub))
    elif instrucao == "LW":  # Instrução I (load)
        return And(MemRead, RegWrite, MemtoReg, ALUSrcA, ALUSrcB, ALUOp_add, Not(ALUOp_sub))
    elif instrucao == "SW":  # Instrução I (store)
        return And(MemWrite, ALUSrcA, ALUSrcB, ALUOp_add, Not(ALUOp_sub))
    elif instrucao == "BEQ":  # Instrução I (branch)
        return And(ALUOp_sub, PCWrite, IRWrite, Not(ALUSrcA), Not(ALUSrcB))
    elif instrucao == "JUMP":  # Instrução J
        return And(PCWrite, IRWrite, Not(MemRead), Not(MemWrite), Not(RegWrite), Not(ALUSrcA), Not(ALUSrcB), Not(ALUOp_add), Not(ALUOp_sub))
    else:
        return False

# Verificar o comportamento da unidade de controle completa para uma instrução específica
instrucao = "ADD"  # Você pode trocar a instrução para "LW", "SW", "BEQ", "JUMP", ou outras conforme necessário

# Solver para verificar os sinais de controle
solver = Solver()

# Verificar se a unidade de controle completa gera os sinais corretamente
solver.add(unidade_controle_completa(instrucao))

# Resultado da verificação
if solver.check() == sat:
    print(f"A unidade de controle completa gerou os sinais de controle corretamente para a instrução {instrucao}.")
else:
    print(f"A unidade de controle completa NÃO gerou os sinais de controle corretamente para a instrução {instrucao}.")
