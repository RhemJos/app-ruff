from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

def tst():
    print('¿Qué onda?')

class MyApp(App):
    def build(self):
        txt = Label(text='Esto es una etiqueta')
        btn = Button(text='Esto es un botón')
        btn.on_press = tst  # el método on_press del objeto btn se vuelve igual a la función tst
        # es decir, llamar a btn.on_press() es equivalente a llamar tst()
        # un método nombrado on_press es llamado automáticamente cuando se hace clic en el botón
                             
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)
        return layout

MyApp().run() # el programa monitorea el clic en el botón e imprime el texto