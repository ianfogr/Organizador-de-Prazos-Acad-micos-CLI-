import pytest
from src.main import TaskManager

@pytest.fixture
def manager():
    return TaskManager()

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