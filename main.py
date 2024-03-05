from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class AddApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',  pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(None, None))

        self.num1 = TextInput(hint_text='Enter first number', multiline=False, size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5})
        self.num2 = TextInput(hint_text='Enter second number', multiline=False, size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5})
        self.result = TextInput(hint_text='Here is the result', disabled=True, size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5})

        calculate_btn = Button(text='Calculate', size_hint=(None, None), size=(100, 40), pos_hint={'center_x': 0.5})
        calculate_btn.bind(on_press=self.calculate)

        layout.add_widget(self.num1)
        layout.add_widget(self.num2)
        layout.add_widget(calculate_btn)
        layout.add_widget(self.result)

        return layout

    def calculate(self, instance):
        try:
            num1 = int(self.num1.text)
            num2 = int(self.num2.text)
            result = num1 + num2  
            self.result.text = str(result)
        except ValueError:
            self.result.text = 'Please enter valid integers'

if __name__ == '__main__':
    AddApp().run()
