import flet as ft

def main(page: ft.Page):
    page.title="Calculadora IMC"
    page.window.width=600
    page.window.alignment=ft.alignment.center
    

    # Função para calcular IMC e definir a imagem e resultado
    def calcular_imc(e):
        
        if peso_field.value!="" and  altura_field.value!="" :
            peso = float(peso_field.value)
            altura = float(altura_field.value) / 100  # Converter para metros
            imc = peso / (altura ** 2)
            
            # Determina a categoria do IMC e a imagem associada
            if imc < 18.5:
                categoria = "Abaixo do peso"
                img_src = "https://example.com/abaixo_do_peso.png"
            elif 18.5 <= imc < 24.9:
                categoria = "Peso normal"
                img_src = "https://example.com/peso_normal.png"
            elif 25 <= imc < 29.9:
                categoria = "Sobrepeso"
                img_src = "https://example.com/sobrepeso.png"
            else:
                categoria = "Obesidade"
                img_src = "https://as2.ftcdn.net/v2/jpg/06/71/99/75/1000_F_671997548_99G7Bq4SJng6ONA1yYywhsJqpTSrLJ6H.webp"

            # Atualiza o resultado na interface
            imc_result.value = f"Seu IMC é {imc:.2f} - {categoria}"
            imc_img.src = img_src
            page.update()

        else:
            imc_result.value = "Por favor, insira valores para comerçar!"
            page.update()

    def valida_altura(e):
        if  not (altura_field.value.isnumeric() and int(altura_field.value)>0):
            altura_field.error_text = "Insira um valor numérico positivo"
            altura_field.value=None
        else:
            altura_field.error_text=None
        page.update()
        
    def valida_peso(e):
        if  not (peso_field.value.isnumeric() and int(peso_field.value)>0):
            peso_field.error_text = "Insira um valor numérico positivo"
            peso_field.value=None
        else:
            peso_field.error_text=None
        page.update()

    # Campo de entrada para altura
    altura_field = ft.TextField(
        label="Altura (cm)", 
        width=300,
        hint_text="Por favor, insira sua altura",
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=valida_altura
    )

    # Campo de entrada para peso
    peso_field = ft.TextField(
        label="Peso (kg)", 
        width=300,
        hint_text="Por favor, insira seu peso",
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    # Dropdown para selecionar gênero
    genero_dropdown = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Feminino"),
            ft.dropdown.Option("Outro"),
        ],
        label="Gênero",
    )

    # Exibe o resultado do cálculo do IMC
    imc_result = ft.Text(value="Seu IMC é ...", size=22)

    # Imagem que será atualizada conforme o IMC
    imc_img = ft.Image(src="https://th.bing.com/th/id/OIP.hDNlYeQpHrfkzZlcT_e6bgHaFz?rs=1&pid=ImgDetMain", width=150, height=150)

    # Botão para calcular o IMC
    calc_button = ft.ElevatedButton(text="Calcular IMC", on_click=calcular_imc)

    # Layout principal
    page.add(
        ft.AppBar(title=ft.Text("Calculadora IMC"), center_title=True),
        
        ft.Column([
            ft.Row(
            [
                imc_result,
                imc_img,
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
            ft.Text("Insira seus dados", size=18),
                altura_field,
                peso_field,
                genero_dropdown,
                calc_button
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
         alignment=ft.MainAxisAlignment.CENTER,
        
        )
        
    )

# Executa o aplicativo
ft.app(target=main)
