#pip install flet
import flet as ft 


listaProdutos = []




def main(page: ft.Page):
    page.title = "Meu App"
    page.padding=200

    lisview =  ft.ListView()

    def itemLista(produto):
        return ft.Container(
            ft.Text(produto),
            bgcolor=ft.colors.BLACK12,
            padding=12,
            alignment=ft.alignment.center,
            margin=3,
            border_radius=10
        )



    def cadastrar(e):
        #print("Botão Clicado")
        ##lisview.controls.append(ft.Text(tx_produto.value))
        lisview.controls.append(itemLista(tx_produto.value))
        page.update()




    lb_produto =  ft.Text('Cadastro de Produto', text_align=ft.TextAlign.LEFT)
    tx_produto = ft.TextField(label="Digite o título do produto...", text_align=ft.TextAlign.LEFT)
    tx_preco = ft.TextField(label="Digite o preço do prduto", text_align=ft.TextAlign.LEFT)

    btn_salvar = ft.ElevatedButton('Salvar', on_click=cadastrar)

    page.add(
        lb_produto,
        tx_produto,
        tx_preco,
        btn_salvar,
        lisview
    )




ft.app(target=main)

