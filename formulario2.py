#O formulário coleta várias informações do usuário, como dados pessoais, preferências de viagem, opções de transporte, interesses em atividades ao ar livre e um campo para notas adicionais.


import flet as ft

def main(page: ft.Page):
    # Função para coletar os dados e exibir no console
    def submit_data(e):
        selected_topics = []
        for checkbox in topics_checkboxes:
            if checkbox.value:
                selected_topics.append(checkbox.label)
        
        print(f"Nome do Evento: {event_name.value}")
        print(f"Data do Evento: {event_date.value}")
        print(f"Localização: {location.value}")
        print(f"Público-alvo: {audience_options.value}")
        print(f"Tópicos Abordados: {', '.join(selected_topics)}")
        print(f"Preferência Alimentar: {food_preferences.value}")
        print(f"Duração Estimada: {duration_slider.value} horas")
        print(f"Descrição Adicional: {description_field.value}")

    # Campos do formulário
    event_name = ft.TextField(label="Nome do Evento", hint_text="Digite o nome do evento")
    event_date = ft.TextField(label="Data do Evento", hint_text="Ex: 15/10/2024")
    location = ft.TextField(label="Localização", hint_text="Digite o endereço do evento")

    audience_options = ft.Dropdown(
        label="Público-alvo",
        options=[
            ft.dropdown.Option("Estudantes"),
            ft.dropdown.Option("Profissionais da área"),
            ft.dropdown.Option("Startups"),
            ft.dropdown.Option("Empresários"),
            ft.dropdown.Option("Pesquisadores"),
        ]
    )

    # Adicionando Checkboxes individualmente
    topics_checkboxes = [
        ft.Checkbox(label="Inteligência Artificial", value=False),
        ft.Checkbox(label="Big Data", value=False),
        ft.Checkbox(label="Internet das Coisas", value=False),
        ft.Checkbox(label="Blockchain", value=False),
        ft.Checkbox(label="Robótica", value=False)
    ]
    
    food_preferences = ft.Dropdown(
        label="Preferência Alimentar",
        options=[
            ft.dropdown.Option("Nenhuma"),
            ft.dropdown.Option("Vegetariana"),
            ft.dropdown.Option("Vegana"),
            ft.dropdown.Option("Sem Glúten"),
            ft.dropdown.Option("Sem Lactose"),
        ]
    )

    duration_slider = ft.Slider(min=1, max=12, divisions=11, label="{value} horas", value=4)
    description_field = ft.TextField(
        label="Descrição Adicional", hint_text="Descreva detalhes adicionais sobre o evento", multiline=True
    )


    # Botão de envio
    submit_button = ft.ElevatedButton(text="Enviar", on_click=submit_data)

    # Layout da página
    page.add(
        ft.Text("Cadastro de Evento de Inovação"),
        event_name,
        event_date,
        location,
        audience_options,
        ft.Text("Tópicos Abordados:"),
        *topics_checkboxes,  # Desenha os checkboxes um por um
        food_preferences,
        ft.Text("Duração do Evento (em horas):"),
        duration_slider,
        description_field,
        submit_button
    )

# Executar o app
ft.app(target=main)
