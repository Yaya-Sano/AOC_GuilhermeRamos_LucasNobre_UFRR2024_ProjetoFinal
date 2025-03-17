
# Análise e Verificação de Circuitos Lógicos com Fórmulas Booleanas e Z3

Este repositório contém a implementação do trabalho da disciplina **Arquitetura e Organização de Computadores**, cujo objetivo é analisar e verificar circuitos lógicos utilizando fórmulas booleanas e o SMT Solver Z3.

## 📌 Objetivo

O projeto busca validar circuitos lógicos digitais através de expressões booleanas e verificar sua equivalência e correção usando fórmulas booleanas e a ferramenta Z3 Solver. Com isso, é possível identificar erros, redundâncias e otimizações em circuitos combinacionais e sequenciais.

## 🛠 Tecnologias Utilizadas

- Python 3.x
- Z3 Solver (z3-solver)
- Manipulação de Expressões Booleanas (com Python)
- **SimPy** (para simulação de processos de sistemas discretos e análise de desempenho)
- Jupyter Notebook (opcional para experimentação interativa)

## 📂 Estrutura do Projeto

```plaintext
📁 circuitos-logicos-z3
📜 README.md
📜 requirements.txt
📂 src
├── 📂 Circuitos  # Definição de circuitos e expressões booleanas
├── 📂 Verificações  # Implementação das verificações com Z3 e manipulação booleana
├── 📂 Simplificações  # Simplificações dos circuitos e expressões lógicas
├── 📂 Testes  # Casos de teste para validar circuitos
📂 docs
├── 📜 relatorio.pdf  # Relatório técnico do projeto
📂 exemplos
├── 📜 exemplo_somador.py  # Teste de um somador binário
```

## 🚀 Instalação e Uso

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/Yaya-Sano/AOC_GuilhermeRamos_LucasNobre_UFRR2024_ProjetoFinal.git
cd circuitos-logicos-z3
```

### 2️⃣ Criar um Ambiente Virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scriptsctivate  # Windows
```

### 3️⃣ Instalar Dependências

Instale as dependências necessárias, incluindo **SimPy**, utilizando o comando abaixo:

```bash
pip install -r requirements.txt
```

**Certifique-se de que a biblioteca SimPy está listada no `requirements.txt`.** Caso contrário, adicione:

```plaintext
simpy==<versão>
```

### 4️⃣ Executar Exemplos

Para rodar o exemplo de um somador binário:

```bash
python exemplos/exemplo_somador.py
```

### 5️⃣ Executar Testes

Para rodar os testes e verificar circuitos:

```bash
python -m unittest src/testes.py
```

## 📖 Relatório

O relatório técnico completo pode ser encontrado em `docs/relatorio.pdf`.

## 📜 Licença

Este projeto é de código aberto sob a licença MIT.

## 🔹 Autores

Guilherme Ramos e Lucas Nobre

## 🔹 Disciplina

Arquitetura e Organização de Computadores

## 🔹 Docente

Herbert Oliveira Rocha
