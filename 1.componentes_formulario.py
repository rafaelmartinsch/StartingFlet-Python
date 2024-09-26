import flet as ft

def main(tela: ft.Page):
    # Configurações iniciais da página
    tela.window_width = 600
    tela.window_height = 800
    tela.padding = 20
    tela.spacing = 10
    tela.title ="Meu Aplicativo"
    tela.theme_mode = ft.ThemeMode.DARK #cor da tela de fundo


    ###funções de ação de botões e check-box###

    def acaoBotao(e): #sera chamado quando o botão for clicado
        texto.value="Você Digitou:"+input.value
        tela.update() #atualiza a pagina

    def checkar(e):
        if cx_selecao.value==True:
            print("Aceitou")
        else:
            print("Não Aceitou")

    def imprime(e):
        tx_imprime.value = (f"Volume:{int(sl_volume.value)}"
                           f"\n Opção:{op_opcao.value}"
                           f"\n Radio:{rg_pref.value}")
        tela.update()


    ###componentes da tela###

    #texto
    titulo =ft.Text("Titulo do meu App", weight="bold", color="blue", italic=True)

    #campo de edição
    input = ft.TextField(label="Digite algo", width="300", bgcolor="gray")

    texto = ft.Text("texto", color="#FFFF00")

    #botao, ao ser clicado chama a função com nome "acaoBotao"
    botao = ft.ElevatedButton("Salvar", on_click=acaoBotao)

    #Caixa de seleção
    cx_selecao = ft.Checkbox(label="Eu aceito os termos!", on_change=checkar)

    #Slider, seleção valor númerico
    sl_volume = ft.Slider(min=0, max=16,  label="Selecione o valor: {value}", width=400, divisions=16) 

    #Lista de Seleção
    op_opcao = ft.Dropdown(label="Selecione uma opção", width=300,
                           options=[
                                        ft.dropdown.Option("Opção 1"),
                                        ft.dropdown.Option("Opção 2"),
                                        ft.dropdown.Option("Opção 3")
                                    ]
                        )

    #Seleção única
    rg_pref = ft.RadioGroup(content=ft.Column(
                                [
                                    ft.Radio(label="Red", value='vermelho'),
                                    ft.Radio(label="Green", value='verde'),
                                    ft.Radio(label="Blue", value='azul'),
                                ]
                                )
                            )

    bt_imprime = ft.ElevatedButton(text="Mostra", on_click=imprime) #botão mostrar no terminal
    tx_imprime =  ft.Text(color="#FF0000")



    #adiciona os elementos na tela
    tela.add(
        titulo,
        input,
        botao,
        texto,
        cx_selecao,
        sl_volume,op_opcao,rg_pref,bt_imprime,tx_imprime
    )

#cria o app para computador
ft.app(target=main)