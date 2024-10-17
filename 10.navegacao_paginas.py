import flet as ft

def main(page: ft.Page):
    # Função para alternar páginas
    def change_page(page_name):
        if page_name == "Page1":
            page.controls.append(page1)
            if page2 in page.controls:
                page.controls.remove(page2)
        elif page_name == "Page2":
            page.controls.append(page2)
            if page1 in page.controls:
                page.controls.remove(page1)
        page.update()

    # Criar o conteúdo da primeira página
    page1 = ft.Column(
        [
            ft.Text("Página 1", style="headlineMedium"),
            ft.Text("Bem-vindo à primeira página.", size=20),
            ft.ElevatedButton(text="Ir para Página 2", on_click=lambda e: change_page("Page2")),
        ],
        alignment=ft.alignment.center,
        spacing=20,
    )

    # Criar o conteúdo da segunda página
    page2 = ft.Column(
        [
            ft.Text("Página 2", style="headlineMedium"),
            ft.Text("Você está na segunda página.", size=20),
            ft.ElevatedButton(text="Voltar para Página 1", on_click=lambda e: change_page("Page1")),
        ],
        alignment=ft.alignment.center,
        spacing=20,
    )

    # Configurar a AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Navegação de Páginas"),
        bgcolor=ft.colors.SURFACE_VARIANT,
        leading=ft.Icon(ft.icons.MENU),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Página 1", on_click=lambda e: change_page("Page1")),
                    ft.PopupMenuItem(text="Página 2", on_click=lambda e: change_page("Page2")),
                ]
            )
        ],
    )

    # Iniciar com a primeira página
    change_page("Page1")

# Executar o aplicativo
ft.app(target=main)
