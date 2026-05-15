# Organizador de Prazos Acadêmicos CLI

Um aplicativo de linha de comando simples para organizar prazos acadêmicos, como entregas de trabalhos, provas e outras atividades escolares.

## Funcionalidades

- Adicionar novas entregas com nome e prazo (formato DD/MM)
- Listar todas as entregas ordenadas por data
- Editar entregas existentes
- Remover entregas
- Persistência automática dos dados em arquivo JSON
- Validação de entrada e datas

## Requisitos

- Python 3.8 ou superior

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd Organizador-de-Prazos-Acad-micos-CLI-
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Execute o programa:
```bash
python Organizador-de-prazos-academicos/main.py
```

Siga o menu interativo para adicionar, listar, editar ou remover entregas.

## Testes

Para executar os testes:
```bash
python -m pytest
```

## Entrega Intermediária (Adaptações)

Para a atividade da Entrega Intermediária foram adicionadas:

- Integração com a API pública Nager.Date para consultar feriados públicos (`src/holidays_api.py`).
- Um teste de integração em `Organizador-de-prazos-academicos/tests/test_integration_holidays.py` que valida o fluxo da API.
- Uma página estática em `docs/index.html` que consulta a mesma API (pronta para deploy em GitHub Pages).
- Workflows em `.github/workflows/` para CI (rodar testes) e deploy de `docs/` para GitHub Pages.

Como rodar a integração localmente:

1. Instale dependências:

```bash
pip install -r requirements.txt
```

2. Rode os testes (inclui o teste de integração):

```bash
pytest
```

3. Execute o CLI e escolha a opção "Listar Feriados Públicos":

```bash
python src/main.py
```

4. Para publicar um site com a listagem de feriados, ative o workflow `pages.yml` ao publicar o branch `main` no GitHub; o conteúdo de `docs/` será publicado no GitHub Pages.

Atualize este README com o link público após o deploy.

## Estrutura do Projeto

```
Organizador-de-Prazos-Acad-micos-CLI-/
├── README.md
├── DOCUMENTACAO.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── Organizador-de-prazos-academicos/
│   ├── main.py          # Ponto de entrada
│   ├── teste_core.py    # Testes unitários
│   └── src/
│       ├── __init__.py
│       └── main.py      # Lógica principal
└── tasks.json           # Dados persistidos (gerado automaticamente)
```

## Desenvolvimento

- Código modularizado em classes
- Testes automatizados
- Persistência de dados
- Validação de entrada
- Tratamento de erros

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

## Documentação

Para documentação detalhada do projeto, incluindo introdução, funcionalidades, estrutura do código e casos de uso, consulte o arquivo [DOCUMENTACAO.md](DOCUMENTACAO.md).