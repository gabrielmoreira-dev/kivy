#conding: utf-8

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label


class TextApp(App):

    def build(self):
        return Label(
            text="Test app",
            italic=True,
            font_size=50,
        )


if __name__ == '__main__':
    TextApp.run(self=TextApp())
