import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('8_float_layout.kv')
class MyLayout(Widget):



    def press(self):
        pass


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()