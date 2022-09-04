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

Builder.load_file('9_update_label.kv')


class MyLayout(Widget):
    def press(self):
        # create variables
        name = self.ids.name_input.text
        print(name)

        # update the label
        self.ids.name_label.text = f"hello {name}"

        # clear input text
        self.ids.name_input.text = ""


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()