import flet as ft 
from db import main_db


def main(page: ft.Page):
    page.title = "ToDo list"
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=10)

    filter_type = 'all'

    def load_task():
        task_list.controls.clear()
        for task_id, task_text, completed in main_db.get_tasks(filter_type):
            print(task_id, task_text)
            task_list.controls.append(create_task_row(task_id, task_text, completed))

        page.update()

    def create_task_row(task_id, task_text, completed):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)

        task_check_box = ft.Checkbox(
            value=bool(completed),
            on_change=lambda e: toggle_task(task_id, e.control.value)
        )

        def enable_edit(_):
            task_field.read_only = False
            task_field.update()

        enable_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit, tooltip='Редактировать')

        def save_task(_):
            main_db.update_task(task_id, task_field.value)
            page.update()

        save_button = ft.IconButton(icon=ft.Icons.SAVE_ALT_ROUNDED, tooltip='Сохранить', on_click=save_task)

        def delete_tassk(_):
            main_db.delete_task(task_id)
            load_task()
        
        delete_button = ft.IconButton(icon=ft.Icons.DELETE, tooltip='удалить', icon_color="red", on_click=delete_tassk)
        page.update
        
        return ft.Row([task_check_box, task_field, enable_button, save_button,delete_button, ], alignment=ft.MainAxisAlignment.START)
    
    def add_task(_):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task)
            task_list.controls.append(create_task_row(task_id=task_id, task_text=task, completed=None))
            task_input.value = ''
            page.update()

    def toggle_task(task_id, is_completed):
        main_db.update_task(task_id=task_id,completed=int(is_completed))
        load_task()
 
    def set_FILTER(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_task()
    def ochistka_xx():
        main_db.delete_completed_tasks()
        load_task

    task_input = ft.TextField(label="Введите новую задачу", read_only=False, expand=True, on_submit=add_task)
    add_button = ft.IconButton(icon=ft.Icons.ADD_COMMENT, tooltip='Добавить задачу', on_click=add_task)
    knopka_1 = ft.Row(controls=[ft.IconButton(icon=ft.Icons.DELETE, tooltip='удалить выполненные задачи', on_click=ochistka_xx)], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    filter_buttons = ft.Row(controls=[
        ft.ElevatedButton('все задачи', on_click=lambda e: set_FILTER('all')),
        ft.ElevatedButton('завершенные задачи', on_click=lambda e: set_FILTER('completed')),
        ft.ElevatedButton('незавершенные задачи', on_click=lambda e: set_FILTER('uncompleted'))
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)


    page.add(ft.Row(
        [task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),filter_buttons,knopka_1, task_list)
    

    load_task()


if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)