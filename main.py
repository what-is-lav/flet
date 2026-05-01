import flet as ft

def main_page(page: ft.Page):
    page.title = "my first app"
    page.theme_mode = ft.ThemeMode.DARK
    hello_text = ft.Text("Hello, world!")
    name_input = ft.TextField(label="Enter your name")
    page.add(hello_text,name_input)

ft.run(main_page, view=ft.AppView.WEB_BROWSER)
# ft.run(main_page)
