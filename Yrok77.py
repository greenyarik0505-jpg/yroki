import flet as ft


def main(page: ft.Page):
    page.title = "Усі віджети Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO        # дозволити прокрутку
    page.padding = 20
    
    # ─── Заголовки ───
    page.add(ft.Text("Опиши себя", size=32, weight=ft.FontWeight.BOLD))
    page.add(ft.Divider())
    
    # ─── Поле введення ───
    name_input = ft.TextField(label="Введи свое имя",hint_text="Введи свое имя",prefix_icon=ft.Icons.PERSON,border_radius=10,)
    page.add(name_input)

    name_input = ft.TextField(label="Введи свой возраст",hint_text="Введи свой возраст",prefix_icon=ft.Icons.PERSON,border_radius=10,)
    page.add(name_input)

    name_input = ft.TextField(label="Введи свое хоби",hint_text="Введи свое хоби",prefix_icon=ft.Icons.PERSON,border_radius=10,)
    page.add(name_input)
    
    # ─── Іконка ───
    page.add(ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.PINK, size=40))
    
    # ─── Картинка ───
    page.add(ft.Image(
        src="https://placehold.co/400x200",
        width=400, height=200,
        border_radius=10,
    ))


ft.app(target=main)
