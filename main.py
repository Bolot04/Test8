import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = 'Список покупок'
    page.theme_mode = ft.ThemeMode.LIGHT
    buy_list = ft.Column(spacing=15)

    filter_type = "all"

    def load_list():
        buy_list.controls.clear()
        for list_id, list_text, completed in main_db.get_list(filter_type):
            buy_list.controls.append(create_list_row(list_id=list_id, list_text=list_text, completed=completed))
        page.update()

    def create_list_row(list_id, list_text, completed):

        checkbox = ft.Checkbox(value=bool(completed), on_change=lambda e: toggle_list(list_id=list_id, is_completed=e.control.value))

        def enable_edit(_):
            list_field.read_only = False
            list_field.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        def save_list(_):
            main_db.update_list(list_id=list_id , new_list=list_field.value)
            list_field.read_only = True
            list_field.update()
        
        def deleted_lists(_):
            main_db.delete_task(list_id)
            load_list()

        deleted_button = ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED, on_click=deleted_lists)

        save_button = ft.IconButton(icon=ft.Icons.SAVE_ALT_ROUNDED, on_click=save_list)

        list_field = ft.TextField(value=list_text, read_only=True, expand=True, on_submit=save_list)

        return ft.Row([checkbox, list_field, edit_button, save_button, deleted_button])
    
    def toggle_list(list_id, is_completed):
        print(f"{list_id} - {is_completed}")
        print(f"{list_id} - {int(is_completed)}")
        main_db.update_list(list_id=list_id, completed=int(is_completed))
        load_list()

    def add_list(_):
        if list_input.value:
            list = list_input.value
            list_id = main_db.add_list(list)
            buy_list.controls.append(create_list_row(list_id=list_id, list_text=list, completed=None))
            print(f'Запись сохранена! ID задачи - {list_id}')
            list_input.value = None
            page.update()

    def set_filter(filter_value):
        nonlocal filter_type
        filter_type = filter_value
        load_list()


    filter_buttons = ft.Row([
        ft.ElevatedButton('Все', on_click=lambda e: set_filter('all'), icon=ft.Icons.ALL_INBOX, icon_color=ft.Colors.YELLOW),
        ft.ElevatedButton('Некупленные', on_click=lambda e: set_filter('uncompleted'), icon=ft.Icons.WATCH_LATER, icon_color=ft.Colors.ORANGE),
        ft.ElevatedButton('Купленные', on_click=lambda e: set_filter('completed'), icon=ft.Icons.CHECK_BOX, icon_color=ft.Colors.GREEN)
    ], alignment=ft.MainAxisAlignment.SPACE_AROUND)

    list_input = ft.TextField(label='Что нужно купить?', expand=True, on_submit=add_list)
    task_input_button = ft.IconButton(icon=ft.Icons.SEND, on_click=add_list)

    main_objects = ft.Row([list_input, task_input_button])

    page.add(main_objects, filter_buttons, buy_list)
    load_list()


if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)