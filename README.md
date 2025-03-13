# Análise e Verificação de Circuitos Lógicos com Fórmulas Booleanas e Z3

Este repositório contém a implementação do trabalho da disciplina **Arquitetura e Organização de Computadores**, cujo objetivo é analisar e verificar circuitos lógicos utilizando **fórmulas booleanas** e o **SMT Solver Z3**.

## 📌 Objetivo
O projeto busca validar circuitos lógicos digitais através de **expressões booleanas** e verificar sua equivalência e correção usando **fórmulas booleanas** e a ferramenta **Z3 Solver**. Com isso, é possível identificar **erros, redundâncias e otimizações** em circuitos combinacionais e sequenciais.

## 🛠 Tecnologias Utilizadas
- **Python 3.x**
- **Z3 Solver** (`z3-solver`)
- **Manipulação de Expressões Booleanas** (com Python)
- **Jupyter Notebook** (opcional para experimentação interativa)

## 📂 Estrutura do Projeto
```
📁 circuitos-logicos-z3
│-- 📜 README.md
│-- 📜 requirements.txt
│-- 📂 src
│   ├── 📜 circuitos.py  # Definição de circuitos e expressões booleanas
│   ├── 📜 verificacao.py  # Implementação da verificação com Z3 e manipulação booleana
│   ├── 📜 testes.py  # Casos de teste para validar circuitos
│-- 📂 docs
│   ├── 📜 relatorio.pdf  # Relatório técnico do projeto
│-- 📂 exemplos
│   ├── 📜 exemplo_somador.py  # Teste de um somador binário
```

## 🚀 Instalação e Uso
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/circuitos-logicos-z3.git
cd circuitos-logicos-z3
```
### 2️⃣ Criar um Ambiente Virtual (opcional)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```
### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```
### 4️⃣ Executar Exemplos
```bash
python exemplos/exemplo_somador.py
```

## 🧪 Testes
Para rodar os testes e verificar circuitos:
```bash
python -m unittest src/testes.py
```

## 📖 Relatório
O relatório técnico completo pode ser encontrado em [`docs/relatorio.pdf`](docs/relatorio.pdf).

## 📜 Licença
Este projeto é de código aberto sob a licença MIT.

---
🔹 **Autores:** Guilherme Ramos e Lucas Nobre
🔹 **Disciplina:** Arquitetura e Organização de Computadores  
🔹 **Docente:** Herbert Oliveira Rocha
