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

# Set the app size
Window.size = (500, 700)

Builder.load_file('10_calc.kv')


class MyLayout(Widget):

    def clear(self):
        self.ids.calc_input.text = ""

    def button_press(self, button):

        # create a variable that contains everything that is already there
        prior = self.ids.calc_input.text

        if "Error" in prior:
            prior = ""

        # determine if 0 is there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f"{button}"
        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def math_sign(self, sign):
        # create a variable that contains everything that is already there
        prior = self.ids.calc_input.text

        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'

    # Create a decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior = f"{prior}."
            self.ids.calc_input.text = prior

        elif "." in prior:
                pass
        else :
            prior = f"{prior}."
            self.ids.calc_input.text = prior


    def remove(self):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f"{prior.replace('-', '')}"
        else :
            self.ids.calc_input.text = f"-{prior}"

    def equals(self):
        prior = self.ids.calc_input.text

        # Error handling
        try :
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"


        # Addition
        # if '+' in prior:
        #     nums = prior.split("+")
        #     res = 0
        #     for num in nums:
        #         res += float(num)
        #
        #     self.ids.calc_input.text = f"{res}"



class CalculatorApp(App):
    def build(self):
        Window.clearcolor = (50/255,50/255,50/255,1)
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()