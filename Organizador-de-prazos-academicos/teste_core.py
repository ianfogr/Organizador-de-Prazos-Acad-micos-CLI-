import pytest
from src.main import TaskManager

@pytest.fixture
def manager():
    return TaskManager(persist=False)

def test_validate_input_empty(manager):
    # Testa se a validação falha com strings vazias
    assert manager.validate_input("", " ") is False

def test_validate_input_ok(manager):
    # Testa se a validação aceita dados corretos
    assert manager.validate_input("Prova", "10/10") is True

def test_format_task(manager):
    # Testa se o formato de saída é um dicionário limpo
    task = manager.format_task("  Lab  ", " 12/05 ")
    assert task == {"name": "Lab", "deadline": "12/05"}

def test_add_task_integration(manager):
    # Testa o fluxo completo de adição
    manager.add_task("Trabalho Final", "20/06")
    assert len(manager.tasks) == 1
    assert manager.tasks[0]["name"] == "Trabalho Final"

def test_remove_task_success(manager):
    # Testa a remoção por índice
    manager.add_task("Tarefa 1", "01/01")
    assert manager.remove_task_by_index(0) is True
    assert len(manager.tasks) == 0

def test_remove_task_invalid_index(manager):
    # Caso limite: tentar remover o que não existe
    assert manager.remove_task_by_index(99) is False

def test_edit_task_success(manager):
    # Testa a edição de uma tarefa
    manager.add_task("Tarefa Original", "01/01")
    assert manager.edit_task(0, "Tarefa Editada", "02/02") is True
    assert manager.tasks[0]["name"] == "Tarefa Editada"
    assert manager.tasks[0]["deadline"] == "02/02"

def test_edit_task_invalid_index(manager):
    # Testa edição com índice inválido
    assert manager.edit_task(99, "Nome", "01/01") is False

def test_validate_date_invalid(manager):
    # Testa validação de data inválida
    assert manager.validate_date("32/13") is False
    assert manager.validate_date("abc") is False

def test_validate_date_valid(manager):
    # Testa validação de data válida
    assert manager.validate_date("31/12") is True
    assert manager.validate_date("01/01") is True

def test_get_sorted_tasks(manager):
    # Testa ordenação das tarefas por data
    manager.add_task("Tarefa 3", "15/03")
    manager.add_task("Tarefa 1", "01/01")
    manager.add_task("Tarefa 2", "10/02")
    sorted_tasks = manager.get_sorted_tasks()
    assert sorted_tasks[0]["name"] == "Tarefa 1"
    assert sorted_tasks[1]["name"] == "Tarefa 2"
    assert sorted_tasks[2]["name"] == "Tarefa 3"