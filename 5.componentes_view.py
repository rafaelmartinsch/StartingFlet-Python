### eplorar documentação em https://flet.dev/docs/controls

import flet as ft

def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Exemplo Completo com Flet"
    page.window.width = 500
    page.window.height = 700

    # Cabeçalho
    header = ft.Text("Elementos de Layout com Flet", size=30, weight="bold")


    # Função para o botão normal
    def on_button_click(e):
        dlg = ft.AlertDialog(title=ft.Text("Alerta!"), content=ft.Text("Atenção eu sou um alerta!"))
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Função para o botão flutuante
    def on_float_button_click(e):
        # Exibe um alerta ao clicar no botão flutuante
        dlg = ft.AlertDialog(title=ft.Text("Alerta!"), content=ft.Text("Você clicou no botão flutuante."))
        page.dialog = dlg
        dlg.open = True
        page.update()


    # Botão normal
    button = ft.ElevatedButton("Exibir Texto", on_click=on_button_click)

    # Botão flutuante
    float_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=on_float_button_click)

    icones =  ft.Icon(name="settings", color="#c1c1c1")
    
    # Imagem
    image = ft.Image(
        src="https://via.placeholder.com/150",  # Imagem de exemplo
        width=150,
        height=150,
        fit=ft.ImageFit.COVER,
    )

    # ListView com itens
    list_view = ft.ListView(
        expand=True,  # Expande para ocupar todo o espaço disponível
        spacing=10,   # Espaçamento entre os itens
        padding=10,   # Padding dentro da lista
        auto_scroll=True,  # Rolagem automática
        controls=[
            ft.Text("Item 1"),
            ft.Text("Item 2"),
            ft.Text("Item 3"),
            ft.Text("Item 4"),
            ft.Text("Item 5"),
        ],
    )


    table =ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                    ],
                ),
            ],
        )
    

    # Layout com os elementos organizados verticalmente
    page.add(
        header,
        button,
        icones,
        image,       # Adicionando a imagem
        list_view,   # Adicionando a lista
        float_button, # Adicionando o botão flutuante
        table
    )

# Inicializando o aplicativo
ft.app(target=main)
