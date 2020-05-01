from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class MainGUI(Screen):
    pass

class ResponseScreen(Screen):
    pass

class AdministratorLogin(Screen):
    pass

class FeedbackForm(Screen):
    pass

class ModificationForm(Screen):
    pass

class CSHelperGUIApp(App):
    #pass
    def build(self):
        return MainGUI()

#Builder.load_file('gui/cshelpergui.kv')

def main():
    pass

def maingui():
    # print(__name__)
    if __name__ == 'gui.cshelpergui' or __name__ == 'cshelpergui' or __name__ == 'main':
        Window.size = (1920, 1080)
        Window.fullscreen = True
        CSHelperGUIApp().run()
        main()