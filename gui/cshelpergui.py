from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen

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
    pass

if __name__ == '__main__':
    Window.size = (1920, 1080)
    Window.fullscreen = True
    CSHelperGUIApp().run()