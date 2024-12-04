import flet as ft
import requests


def main(page: ft.Page):
    page.window_width=600
    
    
    def get_dolar(moeda):
        url = f"https://open.er-api.com/v6/latest/{moeda}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            valorReal = data["rates"].get("BRL")
            
        return valorReal
    
    
    # Função para realizar a conversão
    def convert_currency(e):
        
        valor_dolar=get_dolar("USD")
        
        if dollar_input.value.isdecimal() and valor_dolar!=None:
            dollars = float(dollar_input.value)
            reais = valor_dolar * dollars 
            result.value = f"USD {reais:.2f}"
        
        else:
            result.value = "Por favor, insira um número válido"
            
        page.update()
    
    # Título
    page.title = "Conversor de Moeda"

    
    dollar_input = ft.TextField(label="Valor em Dólares (USD)", width=200)

    # Botão para acionar a conversão
    convert_button = ft.ElevatedButton(text="Converter", on_click=convert_currency)

    # Texto para exibir o resultado
    result = ft.Text(value="BRL 0.00", size=20)

    # Adicionando componentes à página
    page.add(
        ft.Column(
            [
                ft.Text("Conversor de Moeda (BRL para USD)", size=30),
                dollar_input,
                convert_button,
                result,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Executar o aplicativo
ft.app(target=main)