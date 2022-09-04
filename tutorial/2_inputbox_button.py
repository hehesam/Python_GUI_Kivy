import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('color.kv')
class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    address = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        address = self.address.text

        print(f"Hello {name}, you like {pizza}, your address is {address}")

        self.name.text = ""
        self.pizza.text = ""
        self.address.text = ""


class AwesomeApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    AwesomeApp().run()