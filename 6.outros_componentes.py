import flet as ft 

def main(page: ft.Page):
    page.title="Outros componentes"
    page.window_width=800
    page.window_height=900
    page.auto_scroll=ft.ScrollMode.AUTO
    page.theme_mode=ft.ThemeMode.DARK


    ##### input ####
    #CupertionoRadio: Selecionar Todos
    #RangeSlider: Faixa de valores;
    #AutoCompleteSuggestion: Inpunt com auto preenchimento;
    
    

    ###### view ######
    #BottomSheet: Caixa de notificação no rodapé da página;
    #SnackBar = notificação no rodapé
    #ProfressBar:  animação para enquanto carrega algo;
    #Dismissible:  excluir um item da lista arrastando pro lado;

    ##### Animações de View ####
    #CirculeAvatar:  imagem arredondada usada em imagem de perfil
    #CupertinoActivityIndicator: icone animado;
    #Rive: arquivo de animação do tipo .riv;
    #Lottie: animação do tipo lottie json
    #AnimatedSwitcher: trocar um componente na tela;
    #PieChart: grafico de pizza interativo 
    




    page.add()

ft.app(target=main)

