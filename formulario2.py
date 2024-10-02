import flet as ft

def main(page: ft.Page):

    # Função para validar os dados do formulário
    def validate_form(e):
        name = name_field.value
        age = age_field.value
        email = email_field.value
        error_message = ""

        # Validações
        if not name:
            error_message += "Name cannot be empty.\n"
        
        if not age.isdigit() or int(age) <= 0:
            error_message += "Age must be a number greater than 0.\n"
        
        if "@" not in email or "." not in email:
            error_message += "Email must be valid and contain '@' and '.'.\n"
        
        # Exibe mensagens de erro ou sucesso
        if error_message:
            result_text.value = error_message
            result_text.color = ft.colors.RED
        else:
            result_text.value = "Form submitted successfully!"
            result_text.color = ft.colors.GREEN

        page.update()

    # Campos do formulário
    name_field = ft.TextField(label="Name", hint_text="Enter your name")
    age_field = ft.TextField(label="Age", hint_text="Enter your age", keyboard_type=ft.KeyboardType.NUMBER)
    email_field = ft.TextField(label="Email", hint_text="Enter your email")

    # Botão para submissão
    submit_button = ft.ElevatedButton(text="Submit", on_click=validate_form)

    # Texto de resultado
    result_text = ft.Text(value="", color=ft.colors.RED)

    # Adicionando componentes à página
    page.add(
        ft.Column(
            [
                name_field,
                age_field,
                email_field,
                submit_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Executa o app
ft.app(target=main)
