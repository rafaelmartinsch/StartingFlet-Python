import flet as ft

def main(page: ft.Page):
    page.title = "Organizando elementos de Layout"
    page.theme_mode = ft.ThemeMode.DARK
    page.spacing=10
    page.scroll=ft.ScrollMode.AUTO
    
    def bt_add(e):
            txt_number.value = str(int(txt_number.value) + 1)
            page.update()
    def bt_menos(e):
            txt_number.value = str(int(txt_number.value) - 1)
            page.update()
    
    
    
    container = ft.Container(
        content=ft.Icon(ft.icons.ALBUM, color="white"),  # Ícone 'Album' exibido dentro do container, com a cor branca.
        margin=10,  # Margem externa de 10 pixels ao redor do container.
        padding=10,  # Espaçamento interno (padding) de 10 pixels dentro do container.
        alignment=ft.alignment.center,  # Centraliza o ícone dentro do container.
        bgcolor=ft.colors.GREEN_200,  # Define o fundo do container com a cor verde clara.
        width=100,  # Largura fixa de 100 pixels para o container.
        height=100,  # Altura fixa de 100 pixels para o container.
        border_radius=10,  # Bordas arredondadas com raio de 10 pixels.
        on_click=lambda e: print("Elemento Clicado"),  # Função de callback que imprime uma mensagem no console ao clicar no container.
    )
    
   
    colunas=ft.Column( #matriz vertical
        [
            container,container,container
        ],alignment=ft.MainAxisAlignment.CENTER
    )  
    
    linhas=ft.Row(#matriz horizontal.
        [
            container,container,container, container,container,container
        ],alignment=ft.MainAxisAlignment.CENTER
    )
    
    
    album = ft.Container(
        content=ft.Row(
                [
                    ft.Icon(ft.icons.ALBUM, color="white"),
                    ft.Column(
                        [
                            ft.Text("CPM22", weight="bold"),
                            ft.Text("Regina Let's Go")
                        ]
                    )
                ]
            ),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREEN_200,
        width=200,
        height=100,
        border_radius=10
    )
    
    
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    bt_add =  ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=bt_menos),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=bt_add),
            ],
            alignment=ft.MainAxisAlignment.CENTER
    )
    

    imagens = []
    for i in range(50):
        imagens.append(
            ft.Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )

    grid = ft.GridView(
        controls=imagens,       # Lista de componentes a serem exibidos na grade. No caso, são as imagens.
        #expand=1,              # Faz com que o GridView ocupe todo o espaço disponível na página. (Comentado no código)
        runs_count=5,           # Define o número fixo de colunas na grade. Aqui, a grade terá 5 colunas.
        max_extent=150,         # Largura máxima permitida para cada item da grade, em pixels. Cada item terá no máximo 150px de largura.
        child_aspect_ratio=1.0, # Proporção largura/altura de cada item. Aqui, 1.0 significa que cada item será quadrado.
        spacing=5,              # Espaçamento horizontal entre os itens da grade, ou seja, a distância entre os itens em uma mesma linha.
        run_spacing=5,          # Espaçamento vertical entre as linhas da grade, ou seja, a distância entre as fileiras de itens.
    )

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



    page.add(
        
        colunas,
        ft.Divider(),
        linhas,
        ft.Divider(),
        album,
        bt_add,
        grid,
        card_musica
        
    )

ft.app(main)