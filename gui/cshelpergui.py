from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from cs_helper import threader
import time
from kivy.uix.screenmanager import NoTransition
from database.nmsuldap import authenticate
from intent_classifier.intent_classifier import IntentClassifier


class MainGUI(Screen):
    app = App.get_running_app()

    def testCallback(self):
        ic = IntentClassifier()
        answer = ic.answer(self.ids.questionInput.text)
        print(answer)
        # self.ids.response.text = "The question was: " + self.ids.questionInput.text


class ResponseScreen(Screen):
    pass


class AdministratorLogin(Screen):
    def login(self):
        app = App.get_running_app()
        if authenticate(self.ids.usernameInput.text, self.ids.passwordInput.text):
            app.root.transition = NoTransition()
            app.root.current = "ModificationScreen"
        else:
            app.root.transition = NoTransition()
            app.root.current = "LoginScreen"


class FeedbackForm(Screen):
    pass


class ModificationForm(Screen):
    pass


class CSHelperGUIApp(App):
    pass
    # def build(self):
    #     return MainGUI()


# Builder.load_file('gui/cshelpergui.kv')

# def maingui():
# print(__name__)
if __name__ == "__main__":
    # Window.size = (1920, 1080)
    # Window.fullscreen = True
    threader.startThreads()
    CSHelperGUIApp().run()
    # main()
