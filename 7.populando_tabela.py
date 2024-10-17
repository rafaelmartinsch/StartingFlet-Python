import flet as ft

# Função principal
def main(page: ft.Page):
    page.title="Outros componentes"
    page.window_width=800
    page.window_height=600
    page.auto_scroll=ft.ScrollMode.AUTO
    page.theme_mode=ft.ThemeMode.DARK


    # Lista para armazenar os cadastros
    cadastros = []
        

    # Função que será chamada ao clicar no botão Salvar
    def salvar_dados(e):

        cadastro = {
            "nome": nome.value,
            "email": email.value,
            "telefone": telefone.value
        }
        
        cadastros.append(cadastro)

        # Limpa os campos após salvar
        nome.value = ""
        email.value = ""
        telefone.value = ""

        tabela.rows.append(
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(cadastro["nome"])),
                ft.DataCell(ft.Text(cadastro["email"])),
                ft.DataCell(ft.Text(cadastro["telefone"]))
            ])
        )
        
        page.update()


    # Campos do formulário
    nome = ft.TextField(label="Nome", width=300)
    email = ft.TextField(label="E-mail", width=300)
    telefone = ft.TextField(label="Telefone", width=300)

    botao_salvar = ft.ElevatedButton("Salvar", on_click=salvar_dados)



    # Tabela que exibirá os dados
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("E-mail")),
            ft.DataColumn(ft.Text("Telefone"))
        ],
        rows=[]
    )

    # Adicionando os elementos na tela
    page.add(
            ft.Text("Cadastro de Usuários", size=24, weight="bold"),
            nome,
            email,
            telefone,
            botao_salvar,
            ft.Text("Cadastros:", size=20, weight="bold"),
            tabela
    )

# Executar o app
ft.app(target=main)
