from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling

Builder.load_file("13_spell.kv")

class MyLayout(Widget):
    def press(self):
        s = Spelling()
        s.select_language('en_US')

        word = self.ids.word_input.text

        option = s.suggest(word)
        x = ''
        for item in option :
            x = f"{x} \n {item}"

        self.ids.word_label.text = f"{x}"


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()
