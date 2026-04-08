import sys

# Versão Semântica
__version__ = "1.0.0"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def validate_input(self, name, deadline):
        """Valida se os campos não estão vazios."""
        if not name.strip() or not deadline.strip():
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
            return True
        return False

    def remove_task_by_index(self, index):
        """Remove uma tarefa se o índice existir."""
        try:
            self.tasks.pop(index)
            return True
        except (IndexError, TypeError):
            return False

def menu():
    print(f"\n--- AcademicoCheck v{__version__} ---")
    print("1. Adicionar Entrega")
    print("2. Listar Entregas")
    print("3. Remover Entrega")
    print("4. Sair")
    return input("Escolha: ")

def main():
    manager = TaskManager()
    while True:
        choice = menu()
        if choice == "1":
            name = input("Nome da tarefa: ")
            date = input("Prazo (DD/MM): ")
            if manager.add_task(name, date):
                print("✅ Tarefa salva!")
            else:
                print("❌ Erro: Campos obrigatórios!")
        elif choice == "2":
            tasks = manager.tasks
            if not tasks:
                print("Pasta vazia.")
            for i, t in enumerate(tasks):
                print(f"{i}. 📌 {t['name']} - Prazo: {t['deadline']}")
        elif choice == "3":
            idx = int(input("Índice para remover: "))
            if manager.remove_task_by_index(idx):
                print("🗑️ Removido!")
            else:
                print("❌ Índice inválido.")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()