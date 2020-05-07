from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from cs_helper import threader

class MainGUI(Screen):
    def testCallback(self):
        print("Question: ", self.ids.questionInput.text)
    # pass

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
    # def build(self):
    #     return MainGUI()


#Builder.load_file('gui/cshelpergui.kv')

#def maingui():
    # print(__name__)
if __name__ == '__main__':
    Window.size = (1920, 1080)
    Window.fullscreen = True
    threader.startThreads()
    CSHelperGUIApp().run()
    #main()