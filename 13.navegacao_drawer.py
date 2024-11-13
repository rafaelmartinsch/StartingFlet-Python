import flet as ft

# Função para definir as páginas baseadas em rotas
def main(page:  ft.Page):

    
    # Função para lidar com a navegação do Drawer
    def drawer_change(route):
        match drawer.selected_index:
            case 0:
                page.go("/")
            case 1:
                page.go("/page1")
            case 2:
                page.go("/page2")
        

    # Definindo o AppBar
    appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=lambda e: page.open(drawer)), #botão para chamar o drawer
        leading_width=40,
        title=ft.Text("Meu App com Drawer e Rotas"),
        center_title=True,
    )

    # Definindo o Drawer com opções de navegação
    drawer = ft.NavigationDrawer(
        on_change=drawer_change,
        controls=[
                    ft.NavigationDrawerDestination(
                        icon=ft.icons.HOME, label="Home"
                    ),
                    ft.NavigationDrawerDestination(
                        icon=ft.icons.PAGEVIEW, label="Página 1"
                    ),
                    ft.NavigationDrawerDestination(
                        icon=ft.icons.PAGEVIEW, label="Página 2"
                    )
        ]
    )



    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                #as views podem ser criadas em arquivos diverentes para o arquivo principal não ser tão exteso
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("Home")),
                        ft.Text("Bem-vindo à Home!", size=30),
                    ],
                    appbar=appbar,
                    drawer=drawer,
                )
            )

        # Página 1
        elif page.route  == "/page1":
            page.views.append(
                ft.View(
                    "/page1",
                    [
                        ft.AppBar(title=ft.Text("Formulário")),
                        ft.Text("Você está na Página 1!", size=30),
                        form
                        
                    ],
                    appbar=appbar,
                    drawer=drawer,
                )
            )

        # Página 2
        elif page.route  == "/page2":
            page.views.append(
                ft.View(
                    "/page2",
                    [
                        ft.AppBar(title=ft.Text("Página 2")),
                        ft.Text("Você está na Página 2!", size=30),
                        table
                    ],
                    appbar=appbar,
                    drawer=drawer,
                )
            )

        # Atualiza a exibição da página
        page.update()

    tf_nome = ft.TextField(label="Primeiro Nome")
    tf_sobrenome = ft.TextField(label="Sobrenome")
    tf_tel = ft.TextField(label="Telefone", hint_text="Apenas números")
    
    form =  ft.Column(
        [
            ft.Row([
                tf_nome,tf_sobrenome
            ]
            ),
            tf_tel
        ]
    )

    table =ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Primeiro Nome")),
                ft.DataColumn(ft.Text("Sorenome")),
                ft.DataColumn(ft.Text("Idade"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("439999999")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("199999999")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("259999999")),
                    ],
                ),
            ],
    )


    

    # Define a função de mudança de rota
    page.on_route_change = route_change

    # Vai para a rota inicial "/"
    page.go("/")
    ##page.add(appbar)

# Executa o app
ft.app(target=main)
