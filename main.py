import flet as ft
from db import main_db
main_db.init_db()

def main(page: ft.Page):
    pass

if __name__=="__main__":
    main.db.init_db()
    ft.app(target=main)    
