import flet as ft

def main(page: ft.Page):
    page.title = "Flet App Com NavigationDrawer e AppBar"
    page.theme_mode = ft.ThemeMode.LIGHT

    def chama_dismiss(e):
        print("Drawer fechado")

    def chama_chang(e):
        print(f"Indice selecionado: {drawer.selected_index}")


    # Definição da AppBar
    appbar = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=lambda e: page.open(drawer)),
        leading_width=40,
        title=ft.Text("AppBar Exemplo"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Selecione", checked=False
                    ),
                ]
            ),
        ],
    )
    
    drawer = ft.NavigationDrawer(
        on_dismiss=chama_dismiss,
        on_change=chama_chang,
        controls=[
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.MAIL_OUTLINED),
                label="Item 2",
                selected_icon=ft.icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PHONE_OUTLINED),
                label="Item 3",
                selected_icon=ft.icons.PHONE,
            ),
        ],
    )

    page.add(appbar)
    
    
ft.app(target=main)
