from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder

class CustomScreen(Screen):
    hue = NumericProperty(0)

class TeqsonApp(App):
    def build(self):
        root = ScreenManager()
        for x in range(4):
            root.add_widget(CustomScreen(name='Screen %d' % x))
        return root

if __name__ == '__main__':
    TeqsonApp().run()