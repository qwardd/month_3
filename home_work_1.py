import flet as ft 
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение"
    
    

    def on_button_light(_):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def on_button_night(_):
        page.theme_mode = ft.ThemeMode.DARK
        page.update()

    greeting_text = ft.Text('Привет, User')
    greeting_time = ft.Text("История приветствий :")
    history = ft.Text('')

    name_input = ft.TextField(label='Введите ваше имя:')
    def on_button_click(_):
        name = name_input.value.strip()
        print(name)
        if not name :
            greeting_text.value = f'Введите имя !'
            page.update()
        else : 

            time = datetime.now()
            hour = time.hour
            if 6 <= hour <= 12 :
                set_time = f'Доброе утро,  {name}!'
            elif 12 < hour <= 18 :
                set_time = f'Добрый день, {name}! '
            elif 18 < hour <= 24 :
                set_time = f'Добрый вечер, {name}!'
            elif 0 <= hour < 6 :
                set_time = f"Доброй ночи, {name}!"

            greeting_text.value = f"{set_time}" 
            
            time_now = time
            print(time_now)
            history.value +=  f"\n{time_now} : {name}      "


            page.update()


    def on_button_delete(_):
        history.value = " "
            

        page.update()



    light_button = ft.IconButton(icon=ft.Icons.SUNNY, tooltip="светлая тема", on_click=on_button_light)
    dark_button = ft.IconButton(icon=ft.Icons.DARK_MODE, tooltip="темная тема", on_click=on_button_night )
    send_name_button = ft.ElevatedButton('Поздороваться снова', on_click=on_button_click)
    delete_button = ft.IconButton(icon=ft.Icons.DELETE, tooltip= 'очистить историю', on_click=on_button_delete )




    page.add( light_button, dark_button, greeting_text, name_input, send_name_button, greeting_time, history, delete_button)


ft.app(target=main, view=ft.WEB_BROWSER)

