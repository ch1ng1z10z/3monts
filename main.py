import flet as ft 
from db import main_db


def main(page: ft.Page):
    page.title = "ToDo list"
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=10)

    def load_task():
        task_list.controls.clear()
        for task_id, task_text in main_db.get_tasks():
            print(task_id, task_text)
            task_list.controls.append(create_task_row(task_id, task_text))

        page.update()

    def create_task_row(task_id, task_text):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)

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
        

        return ft.Row([task_field, enable_button, save_button,delete_button], alignment=ft.MainAxisAlignment.START)
    
    def add_task(_):
        if task_input.value:
            task = task_input.value
            task_id = main_db.add_task(task)
            task_list.controls.append(create_task_row(task_id=task_id, task_text=task))
            task_input.value = ''
            page.update()
    
        
        

    task_input = ft.TextField(label="Введите новую задачу", read_only=False, expand=True, on_submit=add_task)
    add_button = ft.IconButton(icon=ft.Icons.ADD_COMMENT, tooltip='Добавить задачу', on_click=add_task)

    # page.add(name_input, add_button)
    page.add(ft.Row(
        [task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ), task_list)
    

    load_task()


if __name__ == "__main__":
    main_db.init_db()
    ft.app(target=main)