class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline, 'description': description, 'status': 'не выполнено'})

    def complete_tasks(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = 'выполнено'
                print(f'Задача {description} выполнена')
                break  # Добавляем break, чтобы остановить цикл после выполнения задачи

    def show_tasks(self):
        print('текущие задачи')
        for task in self.tasks:
            if task['status'] == 'не выполнено':
                print(f"{task['description']} - {task['deadline']}")  # Используем двойные кавычки для строки

t = Task()
t.add_task('01.06.25', 'почесать за ухом')
t.add_task('02.06.25', 'потереть левый глаз')
t.add_task('03.06.25', 'наморщить лоб')

t.show_tasks()

t.complete_tasks('почесать за ухом')