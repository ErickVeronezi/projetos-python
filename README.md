# 🐍 Projetos em Python

Este repositório contém pequenos programas em Python desenvolvidos para prática e aprendizado.  
Cada script possui um propósito simples, com menu em texto e tratamento básico de erros.

---

## 📂 Scripts incluídos

### 1. 🎮 Jogo da Palavra (`jogo_da_palavra.py`)
Um mini jogo estilo "forca" onde o usuário deve adivinhar a palavra secreta letra por letra.

- Valida entrada para aceitar apenas **uma letra**.
- Exibe progresso com `*` para letras ainda não descobertas.
- Conta o número de tentativas até o acerto final.

### 2. 🛒 Lista de Compras (`lista_compras.py`)
Aplicação de console que gerencia uma lista de compras.

- **[I]nsert** → adiciona um item.  
- **[D]elete** → remove um item pelo índice.  
- **[L]istar** → mostra todos os itens.  
- **[S]air** → encerra o programa.  

Inclui tratamento para:
- Índices inválidos.
- Lista vazia.
- Inserções vazias.

### 3. 🧮 Calculadora (`calculadora.py`)
Calculadora básica com operações matemáticas simples:

- **Soma [+]**
- **Subtração [-]**
- **Multiplicação [*]**
- **Divisão [/]** (com tratamento para divisão por zero)

Aceita tanto `.` quanto `,` como separador decimal.

---

## 🚀 Como executar

Clone o repositório e rode qualquer script diretamente com Python:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Execute um script
python jogo_da_palavra.py
