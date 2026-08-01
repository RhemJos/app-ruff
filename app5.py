from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
# Una pantalla (un objeto de la clase Screen) es un widget de diseño (Screen es un descendiendo de la clase RelativeLayout).
# ScreenManager es un widget especial que hace visible una de las pantallas especificadas en él.

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name) # el nombre de la pantalla debe ser pasado al constructor de la clase Screen
        btn = Button(text="Cambiar a otra pantalla")
        btn.on_press = self.next
        self.add_widget(btn) # screen es un widget en el cual todos los otros (descendientes) pueden ser creados

    def next(self):
        self.manager.transition.direction = 'left' # el objeto Screen tiene una propiedad "manager"
                                                   # - es un enlace al padre
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text="¡Regresa, regresa!")
        btn.on_press = self.next
        self.add_widget(btn)
        
    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        # FirstScr se mostrará porque fue añadido primero. Esto se puede cambiar así:
        # sm.current = 'second'
        return sm

app = MyApp()
app.run()