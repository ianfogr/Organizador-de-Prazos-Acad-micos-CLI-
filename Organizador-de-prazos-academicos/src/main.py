import sys
import json
import os
from datetime import datetime
from typing import List, Dict, Optional

# Versão Semântica
__version__ = "1.1.0"

class TaskManager:
    def __init__(self, persist=True):
        self.tasks: List[Dict[str, str]] = []
        self.persist = persist
        if persist:
            self.data_file = "tasks.json"
            self.load_tasks()

    def validate_date(self, deadline):
        """Valida se o prazo está no formato DD/MM e é uma data válida."""
        try:
            # Adiciona o ano atual para evitar warning de depreciação
            current_year = datetime.now().year
            datetime.strptime(f"{deadline.strip()}/{current_year}", "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def validate_input(self, name, deadline):
        """Valida se os campos não estão vazios e o prazo é válido."""
        if not name.strip() or not deadline.strip():
            return False
        if not self.validate_date(deadline):
            return False
        return True

    def format_task(self, name, deadline):
        """Formata o dicionário da tarefa."""
        return {"name": name.strip(), "deadline": deadline.strip()}

    def add_task(self, name, deadline):
        """Encapsula a validação e adição."""
        if self.validate_input(name, deadline):
            task = self.format_task(name, deadline)
            self.tasks.append(task)
            self.save_tasks()
            return True
        return False

    def remove_task_by_index(self, index):
        """Remove uma tarefa se o índice existir."""
        try:
            self.tasks.pop(index)
            self.save_tasks()
            return True
        except (IndexError, TypeError):
            return False

    def edit_task(self, index, name, deadline):
        """Edita uma tarefa existente."""
        if 0 <= index < len(self.tasks) and self.validate_input(name, deadline):
            self.tasks[index] = self.format_task(name, deadline)
            self.save_tasks()
            return True
        return False

    def save_tasks(self):
        """Salva as tarefas em um arquivo JSON."""
        if self.persist:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    def load_tasks(self):
        """Carrega as tarefas do arquivo JSON se existir."""
        if self.persist and os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                self.tasks = []

    def get_sorted_tasks(self):
        """Retorna as tarefas ordenadas por data."""
        current_year = datetime.now().year
        return sorted(self.tasks, key=lambda x: datetime.strptime(f"{x['deadline']}/{current_year}", "%d/%m/%Y"))

def menu():
    print(f"\n--- AcademicoCheck v{__version__} ---")
    print("1. Adicionar Entrega")
    print("2. Listar Entregas")
    print("3. Remover Entrega")
    print("4. Editar Entrega")
    print("5. Sair")
    return input("Escolha: ")

def main() -> None:
    manager = TaskManager()
    while True:
        choice = menu()
        if choice == "1":
            name = input("Nome da tarefa: ")
            date = input("Prazo (DD/MM): ")
            if manager.add_task(name, date):
                print("✅ Tarefa salva!")
            else:
                print("❌ Erro: Campos obrigatórios ou prazo inválido!")
        elif choice == "2":
            tasks = manager.get_sorted_tasks()
            if not tasks:
                print("Pasta vazia.")
            else:
                for i, t in enumerate(tasks):
                    print(f"{i}. 📌 {t['name']} - Prazo: {t['deadline']}")
        elif choice == "3":
            try:
                idx = int(input("Índice para remover: "))
                if manager.remove_task_by_index(idx):
                    print("🗑️ Removido!")
                else:
                    print("❌ Índice inválido.")
            except ValueError:
                print("❌ Entrada inválida. Digite um número.")
        elif choice == "4":
            try:
                idx = int(input("Índice para editar: "))
                if 0 <= idx < len(manager.tasks):
                    name = input("Novo nome: ")
                    date = input("Novo prazo (DD/MM): ")
                    if manager.edit_task(idx, name, date):
                        print("✅ Editado!")
                    else:
                        print("❌ Erro: Campos obrigatórios ou prazo inválido!")
                else:
                    print("❌ Índice inválido.")
            except ValueError:
                print("❌ Entrada inválida. Digite um número.")
        elif choice == "5":
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()