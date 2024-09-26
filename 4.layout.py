import flet as ft

def main(page: ft.Page):

    # Função para o PopupMenuButton
    def menu_item_selected(e):
        page.dialog = ft.AlertDialog(title=ft.Text(f"Você escolheu: {e.control.text}"))
        page.dialog.open = True
        page.update()

    # Definindo a AppBar com Menu e PopupMenuButton
    page.appbar = ft.AppBar(
        title=ft.Text("Exemplo de Layout com Flet"),
        bgcolor=ft.colors.SURFACE_VARIANT, # é uma cor definida na biblioteca Flet que segue a Material Design Color System. É uma das cores de superfície usadas para criar um contraste visual no design de interfaces.
        leading=ft.Icon(ft.icons.MENU),
        actions=[
            ft.IconButton(ft.icons.SEARCH),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Opção 1", on_click=menu_item_selected),
                    ft.PopupMenuItem(text="Opção 2", on_click=menu_item_selected),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="Opção 3", on_click=menu_item_selected),
                ]
            ),
        ],
    )

    # Definindo o GridView
    grid = ft.GridView(
        expand=1,
        runs_count=3,  # Número de colunas no Grid
        child_aspect_ratio=1.0,  # Aspecto do item do grid
        spacing=10,  # Espaçamento entre os itens
        run_spacing=10,  # Espaçamento entre as linhas
    )

    # Adicionando itens ao GridView
    for i in range(1, 10):
        grid.controls.append(
            ft.Container(
                ft.Text(f"Item {i}", size=20),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_200,
                border_radius=10,
                padding=10,
            )
        )

    # Layout da página
    page.add(
        ft.Column(
            [
                ft.Text("Exemplo de Grid Layout", style="headlineMedium"),
                grid,
            ]
        )
    )

# Executar o aplicativo
ft.app(target=main)
