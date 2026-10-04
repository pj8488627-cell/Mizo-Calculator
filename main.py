from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle

class CalculatorApp(App):
    def build(self):
        root_layout = BoxLayout(orientation='vertical', spacing=10, padding=15)
        with root_layout.canvas.before:
            Color(0.09, 0.09, 0.11, 1)
            self.rect = Rectangle(size=root_layout.size, pos=root_layout.pos)
        root_layout.bind(size=self._update_rect, pos=self._update_rect)
        
        self.display = TextInput(
            text='', readonly=True, font_size=55, halign='right', size_hint_y=None, height=180,
            background_color=(0.09, 0.09, 0.11, 1), foreground_color=(1, 1, 1, 1), border=(0, 0, 0, 0)
        )
        root_layout.add_widget(self.display)
        
        button_layout = GridLayout(cols=4, spacing=8)
        buttons = ['7', '8', '9', '÷', '4', '5', '6', '×', '1', '2', '3', '-', 'C', '0', '=', '+']
        
        for btn in buttons:
            if btn == 'C': bg, fg = (0.83, 0.83, 0.82, 1), (0, 0, 0, 1)
            elif btn == '=': bg, fg = (0.18, 0.77, 0.71, 1), (1, 1, 1, 1)
            elif btn == '÷': bg, fg = (1, 0.62, 0.04, 1), (1, 1, 1, 1)
            elif btn == '×': bg, fg = (0.37, 0.36, 0.90, 1), (1, 1, 1, 1)
            elif btn == '-': bg, fg = (1, 0.23, 0.19, 1), (1, 1, 1, 1)
            elif btn == '+': bg, fg = (0.20, 0.78, 0.35, 1), (1, 1, 1, 1)
            else: bg, fg = (0.17, 0.17, 0.18, 1), (1, 1, 1, 1)
                
            button = Button(text=btn, font_size=38, bold=True, background_normal='', background_color=bg, color=fg)
            button.bind(on_press=self.on_button_press)
            button_layout.add_widget(button)
            
        root_layout.add_widget(button_layout)
        return root_layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_button_press(self, instance):
        current_text = self.display.text
        button_text = instance.text
        operators = ['+', '-', '×', '÷']
        
        if button_text == 'C':
            self.display.text = '' 
        elif button_text == '=':
            if current_text:
                try:
                    if current_text[-1] in operators: current_text = current_text[:-1]
                    calculation_text = current_text.replace('×', '*').replace('÷', '/')
                    res = eval(calculation_text)
                    if isinstance(res, float) and res.is_integer(): res = int(res)
                    self.display.text = str(res)
                except Exception: self.display.text = 'Error'
        else:
            if not current_text and button_text in operators and button_text != '-': return
            if current_text and current_text[-1] in operators and button_text in operators:
                self.display.text = current_text[:-1] + button_text
            else:
                self.display.text = current_text + button_text

if __name__ == '__main__':
    CalculatorApp().run()

