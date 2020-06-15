import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.core.window import Window
Window.size = 500, 600


# The app class name must be equal to the kv file name
# hello.kv will be linked to this class
class HelloApp(App):

    def build(self):
        pass


if __name__ == '__main__':
    HelloApp.run(HelloApp())
