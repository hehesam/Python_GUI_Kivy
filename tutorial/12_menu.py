from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file("12_menu.kv")

class MyLayout(Widget):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
            print(filename[0])
        except:
            pass


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()
