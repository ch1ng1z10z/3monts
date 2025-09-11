import flet as ft 
from datetime import datetime
from random import randint

def main(page: ft.Page):
    page.title = "Моё первое приложение на Flet"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")
    
    greeting_history = []
    history_text = ft.Text(value='История приветствий:')

    def random_nam(_):
        names = ("Александр", "Михаил Максим", "Иван", "Артём", "Дмитрий", "Даниил", "Лев", "Марк", "София", "Мария", "Анна", "Алиса", "Ева", "Варвара", "Виктория", "Василиса")
        ramdom_index = randint(0,len(names) - 1)
        name_input.value = names[ramdom_index]
    page.update()

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Hello {name}"
            name_input.value = ""

            date_str = datetime.now().strftime("%Y/%m/%d")
            greeting_history.append(f"{date_str} — {name}")
            
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Ошибка! Не ввели имя" 
        
        print(greeting_text.value)
        page.update()
    
    def backround_color(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode =ft.ThemeMode.LIGHT
        page.update()
    
    
    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    random_name = ft.ElevatedButton("random name",on_click=random_nam)
    greet_button = ft.ElevatedButton("send", on_click=on_button_click)
    backdr_color = ft.IconButton(icon=ft.Icons.ADD_BOX_ROUNDED, on_click=backround_color)
    


    page.add(greeting_text, name_input, greet_button, history_text, backdr_color,random_name)

ft.app(target=main)