# Documentação do Organizador de Prazos Acadêmicos CLI

## Introdução

O **Organizador de Prazos Acadêmicos CLI** é uma aplicação de linha de comando desenvolvida em Python para ajudar estudantes a gerenciar prazos de entregas acadêmicas, como trabalhos, provas e outras atividades. O programa permite adicionar, listar, editar e remover tarefas, com persistência automática dos dados.

## Objetivos

- Facilitar a organização de prazos acadêmicos.
- Fornecer uma interface simples e intuitiva.
- Garantir a persistência dos dados entre execuções.
- Validar entradas para evitar erros.

## Funcionalidades

### 1. Adicionar Entrega
- Permite inserir o nome da tarefa e o prazo no formato DD/MM.
- Valida se os campos estão preenchidos e se a data é válida.
- Salva automaticamente no arquivo `tasks.json`.

### 2. Listar Entregas
- Exibe todas as tarefas ordenadas por data.
- Mostra o índice, nome e prazo de cada tarefa.

### 3. Remover Entrega
- Remove uma tarefa pelo índice fornecido.
- Confirma se o índice é válido.

### 4. Editar Entrega
- Permite alterar o nome e/ou prazo de uma tarefa existente.
- Valida as novas entradas.

### 5. Sair
- Encerra o programa.

## Estrutura do Código

### Classe TaskManager
Localizada em `src/main.py`, responsável pela lógica de negócio.

#### Métodos Principais:
- `__init__(persist=True)`: Inicializa a lista de tarefas e carrega dados se persistência ativada.
- `validate_date(deadline)`: Verifica se a data está no formato DD/MM.
- `validate_input(name, deadline)`: Valida nome e prazo.
- `format_task(name, deadline)`: Cria dicionário da tarefa.
- `add_task(name, deadline)`: Adiciona tarefa após validação.
- `remove_task_by_index(index)`: Remove tarefa por índice.
- `edit_task(index, name, deadline)`: Edita tarefa existente.
- `save_tasks()`: Salva tarefas em JSON.
- `load_tasks()`: Carrega tarefas do JSON.

### Função main()
- Controla o loop do menu interativo.
- Trata entradas inválidas com try-except.

### Testes
Localizados em `teste_core.py`, utilizando pytest.
- Testam validações, adição, remoção, edição e casos de erro.

## Tecnologias Utilizadas

- **Python 3.8+**: Linguagem principal.
- **JSON**: Para persistência de dados.
- **datetime**: Para validação de datas.
- **pytest**: Para testes automatizados.

## Instalação e Execução

Ver seção correspondente no README.md.

## Casos de Uso

### Exemplo de Uso:
1. Execute o programa.
2. Escolha "1" para adicionar uma tarefa.
3. Digite "Trabalho de Matemática" como nome.
4. Digite "15/05" como prazo.
5. A tarefa será salva.
6. Escolha "2" para listar tarefas.

## Limitações

- Datas no formato DD/MM sem ano (assume ano atual).
- Não suporta lembretes ou notificações.
- Interface limitada ao terminal.

## Melhorias Futuras

- Adicionar suporte a datas com ano.
- Implementar notificações por e-mail.
- Criar interface gráfica.
- Adicionar categorias para tarefas.

## Conclusão

Este projeto demonstra conceitos básicos de programação orientada a objetos, validação de entrada, persistência de dados e testes em Python. É uma ferramenta útil para estudantes e serve como base para expansões futuras.