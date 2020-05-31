import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Button


class WidgetsApp(App):

    @staticmethod
    def click():
        print("The button was clicked!")

    def build(self):
        bt = Button(text="Click here")
        bt.on_press = self.click
        return bt


if __name__ == '__main__':
    WidgetsApp.run(WidgetsApp())

