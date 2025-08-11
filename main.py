import flet as ft 


def main(page: ft.Page):
    page.title = "my first app on Flet"

    greeting_text = ft.Text("hello,world!")
    page.theme_mode = ft.ThemeMode.LIGHT

    name_input = ft.TextField(label='введите имя')

    def on_button_click(_):
        name = name_input.value.strip()
        print(name)
        if name:
            greeting_text.value = f'hello, {name}'
        else:
            greeting_text.value ='введите имя! '
        page.update()

    greet_buttton = ft.ElevatedButton('send', on_click=on_button_click)
    greet_buttton = ft.TextButton('send', on_click=on_button_click)
    greet_buttton = ft.IconButton(icon=ft.Icons.SEND, tooltip="отправить", on_click=on_button_click)

    
       
    
    page.add(greeting_text, name_input, greet_buttton)
    


ft.app(target=main, view=ft.WEB_BROWSER)
#ft.app(target=main)