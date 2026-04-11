# 📦 Sistema de Controle de Estoque (CLI)

Um sistema simples de controle de mercadorias feito em **Python** utilizando **SQLite3**, rodando diretamente no terminal (CLI).

## 🚀 Funcionalidades

- ✅ Cadastro de produtos
- 📥 Entrada de mercadorias (incremento de estoque)
- 📤 Saída de mercadorias (baixa de estoque)
- 📋 Listagem de estoque
- 🗑️ Remoção de produtos
- 💾 Persistência de dados com SQLite

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- SQLite3 (banco de dados local)
- Terminal / CLI

---

## 📂 Estrutura do Projeto

```
📁 projeto/
│
├── main.py        # Arquivo principal que inicia o sistema
├── db.py          # Funções de banco de dados e lógica do sistema
├── estoque.db     # Banco de dados SQLite (gerado automaticamente)
```
---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```
2. Acesse a pasta:
```
cd seu-repositorio
```
3. Execute o projeto:
```
python main.py
```
---

## 🧠 Como Funciona

O sistema utiliza um menu interativo no terminal, permitindo ao usuário navegar entre as opções digitando números.

Os dados são armazenados em um banco SQLite local (`estoque.db`), que é criado automaticamente na primeira execução.

---

## 📋 Estrutura da Tabela

**Tabela:** `produtos`

| Campo       | Tipo           |
|------------|---------------|
| id         | INTEGER (PK)  |
| nome       | TEXT          |
| quantidade | INTEGER       |

---

## ⚠️ Validações Implementadas

- Não permite cadastrar produtos com nome vazio  
- Quantidade deve ser maior que 0  
- Tratamento de erro para entradas inválidas  
- Verificação se o produto existe antes de operações  

---

## 💡 Possíveis Melhorias

- Interface gráfica (Tkinter ou Web)  
- Sistema de login/autenticação  
- Relatórios de movimentação  
- Controle de estoque mínimo  
- Exportação para Excel/PDF  
- API REST com Flask ou FastAPI  

---

## 👨‍💻 Autor

Desenvolvido por **Andre Bimbatti**

---

## 📄 Licença

Este projeto é livre para uso e aprendizado.

