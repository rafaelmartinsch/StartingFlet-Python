import flet as ft

def main(tela: ft.Page):
    # Configurações iniciais da página
    tela.window.width = 600
    tela.window.height = 800
    tela.spacing = 15
    tela.scroll = ft.ScrollMode.AUTO
    tela.title ="Cadastro de turistas"
    tela.theme_mode = ft.ThemeMode.DARK #cor da tela de fundo


    #Função para apresentar ao usuário o valor selecionado
    def slider(e):
        tx_freq.value="Qual sua frequência de Viagem: "+str(sl_freq.value)
        tela.update()


    # Função para coletar os dados e exibir no console
    def imprime(e):
        texto = (f"Nome: {tf_nome.value}\n"
                            f"Email: {tf_email.value}\n"
                            f"Gênero: {op_genero.value}\n"
                            f"Meio de transporte preferido: {op_transport.value}\n"
                            f"Interesses em atividades: \n"
                            )
        
        for atividade in ck_atividades:
            if(atividade.value==True):
                texto+=f"{atividade.label}\n"

        texto+=(f"\nFrequência de viagens ao ar livre: {sl_freq.value}\n"
                f"Notas adicionais: {tf_obs.value}\n")
        
        tx_imprime.value=texto
        tela.update()
                        

    ### Campos do formulário ##

    tf_nome = ft.TextField(label="Nome Completo", hint_text="Digite seu nome completo", bgcolor="gray")
    tf_email = ft.TextField(label="Email", hint_text="Digite seu email", bgcolor="gray")

    op_genero = ft.Dropdown(
        label="Gênero",
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
            ft.dropdown.Option("Outro"),
        ]
    )

    op_transport = ft.Dropdown(
        label="Meio de Transporte Preferido",
        options=[
            ft.dropdown.Option("Carro"),
            ft.dropdown.Option("Avião"),
            ft.dropdown.Option("Ônibus"),
            ft.dropdown.Option("Bicicleta"),
            ft.dropdown.Option("A pé"),
        ]
    )

    ck_atividades  =  (ft.Checkbox(label="Trilhas", value=False),
                        ft.Checkbox(label="Canoagem", value=False),
                        ft.Checkbox(label="Observação de aves", value=False),
                        ft.Checkbox(label="Fotografia da natureza", value=False)
                        )
        
  
    tx_freq =  ft.Text(value="Qual sua frequência de Viagem: 0")
    sl_freq = ft.Slider(min=0, max=10, divisions=10, label="Frequência de Viagens: {value}/ano", value=0, on_change=slider)

    tf_obs = ft.TextField(label="Notas Adicionais", hint_text="Se houver algo mais que gostaria de nos contar", multiline=True, bgcolor="gray")
    

    tx_imprime =  ft.Text(color="green")

    # Botão de envio
    bt_submit = ft.ElevatedButton(text="Enviar", on_click=imprime)

    # Layout da página
    tela.add(
        tf_nome,
        tf_email,
        op_genero,
        op_transport,
        *ck_atividades,
        tx_freq,
        sl_freq,
        tf_obs,
        bt_submit,tx_imprime
    )

# Executar o app
ft.app(target=main)
