import flet as ft 

def main(tela: ft.Page):
    tela.theme_mode=ft.ThemeMode.DARK
    
    card_musica =  ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("O Rappa"),
                            subtitle=ft.Text(
                                "Pescador de Ilusões"
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    
    
    layout =  ft.Row(
        [
            ft.Column([
                ft.Text("Spotfy Senac-MS", size=32, width=400, text_align="center"),
                card_musica,card_musica,card_musica,card_musica
            ],
            spacing=10  # Adiciona espaçamento entre os cards
            ),
            ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Icon(ft.icons.PLAY_CIRCLE_OUTLINE_SHARP, color="green", size=150),
                            bgcolor=ft.colors.BLACK26,
                            height=400,
                            width=400,
                            border_radius=10
                        ),
                        ft.Text("Capital Inicial", weight="bold", size=30, width=400, text_align="center"),
                        ft.Text("Natasha", width=400, text_align="center"),
                        ft.Row(
                            [
                                ft.Icon(ft.icons.SKIP_PREVIOUS, color="green", size=50),
                                ft.Icon(ft.icons.PLAY_ARROW, color="green", size=50),
                                ft.Icon(ft.icons.SKIP_NEXT, color="green", size=50),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ],
                    spacing=10,  # Adiciona espaçamento entre os elementos
                    width=400
            )
        ], 
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    
    
    tela.add(layout)

ft.app(target=main)