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
Builder.load_file('6_bg.kv')
class MyLayout(Widget):



    def press(self):
        pass


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,1,0,0)
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()