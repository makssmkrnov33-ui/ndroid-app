from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (0.9, 0.9, 0.9, 1)

class ConverterLayout(BoxLayout):
    amount = StringProperty('0')
    result = StringProperty('0')

    def convert(self):
        exchange_rate = 75.5
        try:
            converted = float(self.amount or 0) * exchange_rate
            self.result = f'{converted:.2f} RUB'
        except Exception as e:
            self.result = 'Ошибка!'

class ConverterApp(App):
    def build(self):
        return ConverterLayout()

if __name__ == '__main__':
    ConverterApp().run()
