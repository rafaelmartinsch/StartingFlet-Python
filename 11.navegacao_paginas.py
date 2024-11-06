import flet as ft

def main(page: ft.Page):
    
     # Criar o conteúdo da primeira página
    view1 = ft.View(
        route="/",
        controls=[
            ft.Text("Página 1", style="headlineMedium"),
            ft.Text("Bem-vindo à primeira página.", size=20),
            ft.ElevatedButton(text="Ir para Página 2", on_click=lambda e: page.go("/page2")),
        ]
    )

    # Criar o conteúdo da segunda página
    view2 =  ft.View(
        route="/",
        controls=[
            ft.Text("Página 2", style="headlineMedium"),
            ft.Text("Você está na segunda página.", size=20),
            ft.ElevatedButton(text="Voltar para Página 1", on_click=lambda e: page.go("/")),
        ]
    )

    # Definição das rotas
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(view1)
        elif page.route == "/page2":
            page.views.append(view2)
        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main)
