from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling

Builder.load_file("14_slider.kv")

class MyLayout(Widget):
    def slide_it(self, *args):
        # print(args[1])
        self.slide_text.text = str(int(args[1]))



class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()
