import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
Window.size = 500, 600


class WidgetsApp(App):

    @staticmethod
    def click():
        print('Ok')

    def build(self):
        layout = FloatLayout()

        ti = TextInput(text="Enter your text here")
        ti.size_hint = None, None
        ti.height = 300
        ti.width = 400
        ti.x = 60
        ti.y = 250

        bt = Button(text="Click here")
        bt.on_press = self.click
        bt.size_hint = None, None
        bt.height = 50
        bt.width = 200
        bt.x = 170
        bt.y = 150

        layout.add_widget(ti)
        layout.add_widget(bt)
        return layout


if __name__ == '__main__':
    WidgetsApp.run(WidgetsApp())

