# 🤖 Bot de Automação de Cadastro de Produtos (RPA)

Projeto desenvolvido durante a Jornada Python da Hashtag Treinamentos. Este bot automatiza o processo de login em um sistema web, lê uma base de dados externa e realiza o cadastro automatizado de produtos.

## 🛠️ Tecnologias Utilizadas
* **Python** (Linguagem principal)
* **PyAutoGUI** (Automação de interface, cliques e teclado)
* **Pandas** (Manipulação e leitura da base de dados `.csv`)
* **OS** (Tratamento dinâmico de caminhos de arquivos)

## 🎯 Funcionalidades
* Abertura automática do navegador Chrome e navegação até o sistema.
* Realização de login automatizado.
* Leitura de uma base de dados contendo múltiplos produtos.
* Estrutura de repetição (`for`) para cadastrar item por item.
* Inteligência de dados para ignorar campos de observação vazios (`NaN`), evitando erros de preenchimento.