from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

KV = '''
MDScreen:
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'

        MDTopAppBar:
            title: "Dice Roller"
            pos_hint: {'center_x': 0.5}

    MDRectangleFlatButton:
        text: "Testing 1... 2... 3..."
        pos_hint: {'center_x': 0.5 , 'center_y': 0.5}
'''

class MainApp(MDApp):
    def __init__(self):
        super().__init__()
        self.kvs = Builder.load_string(KV)

    def build(self):
        screen = Screen()
        screen.add_widget(self.kvs)
        return screen
    
ma = MainApp()
ma.run()