import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivymd import toast
from plyer import tts
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import MainClient


class MyGrid(GridLayout):

    def SPEAK(self):
        try:
            Text = MainClient.ReceiveTextToSpeak()
            tts.speak(Text)
        except Exception as e:
            print(e)

    def ReceiveText(self, instance):
        Clock.schedule_interval(MainClient.ReceiveTextToSpeak, 1 / 30)
        Clock.schedule_interval(self.SPEAK, 1 / 30)

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.TextToSpeak = TextInput(text="Enter Text To Speak", multiline=False)
        self.add_widget(self.TextToSpeak)

        self.Speak = Button(text="SPEAK")
        self.add_widget(self.Speak)
        self.Speak.bind(on_press=self.SPEAK)
        Clock.schedule_once(MainClient.Connect, 1)
        Clock.schedule_once(self.ReceiveText, 2)


class MyApp(App):

    def build(self):
        return MyGrid()


MyApp().run()
