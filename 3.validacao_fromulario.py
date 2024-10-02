import flet as ft

def main(page: ft.Page):
    # Função de validação do campo Nome Completo
    def validate_name(e):
        if not full_name.value or len(full_name.value.split()) < 2:
            full_name.error_text = "Por favor, insira o nome completo (nome e sobrenome)."
        else:
            full_name.error_text = None
        page.update()

    # Função de validação do campo Telefone (apenas números com 11 dígitos)
    def validate_phone(e):
        if not (len(phone_number.value)==10 or len(phone_number.value)==11):
            phone_number.error_text = "Por favor, insira um telefone válido (somente números, 10 ou 11 dígitos)."
        else:
            phone_number.error_text = None
        page.update()

    # Função de validação do campo E-mail (formato padrão de e-mail)
    def validate_email(e):
        if not (email.value.count("@")==1 and email.value.count(".")>=1):
            email.error_text = "Por favor, insira um e-mail válido."
        else:
            email.error_text = None
        page.update()

    # Função de validação do campo Idade (maior que 0)
    def validate_age(e):
        if not age.value.isdigit() or int(age.value) <= 0:
            age.error_text = "Por favor, insira uma idade válida (maior que 0)."
        else:
            age.error_text = None
        page.update()

    # Função de validação do CPF (formato com 11 dígitos)
    def validate_cpf(e):
        if len(cpf.value)!=10 :
            cpf.error_text = "Por favor, insira um CPF válido (11 dígitos, apenas números)."
        else:
            cpf.error_text = None
        page.update()


    # Função de submissão e validação geral
    def submit_form(e):        
        if not (full_name.error_text or phone_number.error_text or email.error_text or 
                age.error_text or cpf.error_text):
            print("Todos os dados estão válidos!")
        else:
            print("Por favor, corrija os campos com erro.")

    # Campos de texto com validações
    full_name = ft.TextField(label="Nome Completo", on_blur=validate_name)
    phone_number = ft.TextField(label="Telefone", hint_text="Apenas números", on_blur=validate_phone)
    email = ft.TextField(label="E-mail", on_blur=validate_email)
    age = ft.TextField(label="Idade", on_blur=validate_age)
    cpf = ft.TextField(label="CPF", hint_text="Apenas números", on_blur=validate_cpf)

    # Botão de submissão
    submit_button = ft.ElevatedButton(text="Enviar", on_click=submit_form)

    # Layout da página
    page.add(
        full_name,
        phone_number,
        email,
        age,
        cpf,
        submit_button
    )

# Executar o app
ft.app(target=main)
