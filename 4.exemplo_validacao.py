import flet as ft
from datetime import datetime

def main(page: ft.Page):

    # Função para validar os dados do formulário
    def validate_form(e):
        brand = brand_field.value
        year = year_field.value
        mileage = mileage_field.value
        fuel_type = fuel_dropdown.value
        error_message = ""

        # Obter o ano atual
        current_year = datetime.now().year

        # Validações
        if not brand:
            error_message += "Vehicle brand cannot be empty.\n"
        
        if not year.isdigit() or int(year) < 1886 or int(year) > current_year:
            error_message += f"Year of manufacture must be between 1886 and {current_year}.\n"
        
        if not mileage.isdigit() or int(mileage) < 0:
            error_message += "Mileage must be a number greater than or equal to 0.\n"
        
        if fuel_type not in ["Gasolina", "Álcool", "Diesel", "Elétrico"]:
            error_message += "Please select a valid fuel type.\n"

        # Exibe mensagens de erro ou sucesso
        if error_message:
            result_text.value = error_message
            result_text.color = ft.colors.RED
        else:
            result_text.value = "Vehicle data submitted successfully!"
            result_text.color = ft.colors.GREEN

        page.update()

    # Campos do formulário
    brand_field = ft.TextField(label="Vehicle Brand", hint_text="Enter the vehicle's brand")
    year_field = ft.TextField(label="Year of Manufacture", hint_text="Enter the year of manufacture", keyboard_type=ft.KeyboardType.NUMBER)
    mileage_field = ft.TextField(label="Mileage (km)", hint_text="Enter the mileage", keyboard_type=ft.KeyboardType.NUMBER)
    
    fuel_dropdown = ft.Dropdown(
        label="Fuel Type",
        hint_text="Select the fuel type",
        options=[
            ft.dropdown.Option("Gasolina"),
            ft.dropdown.Option("Álcool"),
            ft.dropdown.Option("Diesel"),
            ft.dropdown.Option("Elétrico"),
        ],
    )

    # Botão para submissão
    submit_button = ft.ElevatedButton(text="Submit", on_click=validate_form)

    # Texto de resultado
    result_text = ft.Text(value="", color=ft.colors.RED)

    # Adicionando componentes à página
    page.add(
        ft.Column(
            [
                brand_field,
                year_field,
                mileage_field,
                fuel_dropdown,
                submit_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Executa o app
ft.app(target=main)
