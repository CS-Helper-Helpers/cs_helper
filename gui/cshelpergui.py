from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.core.window import Window 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from cs_helper import threader
import time
from kivy.uix.screenmanager import NoTransition
from database import nmsuldap
from intent_classifier.intent_classifier import IntentClassifier
from kivy.properties import BooleanProperty
from kivy.uix import boxlayout, checkbox, label, textinput

class MainGUI(Screen):
    def answerQuestion(self):
        app = App.get_running_app()
        ic = IntentClassifier()
        answer = ic.answer(self.ids.questionInput.text)
        # print(answer)
        app.root.ids.response_screen.ids.response.text = answer + "\nIf you would like to contribute to this project, press the feedback button. Otherwise, press the home button."

class ResponseScreen(Screen):
    def setupCategories(self):
        app = App.get_running_app()
        ic = IntentClassifier()
        categories = ic.load_dataset(piece = "uniqueintents")
        categoryScroller = app.root.ids.feedback_screen.ids.feedbackCategories
        categoryList = boxlayout.BoxLayout()
        categoryList.orientation = "vertical"
        categoryList.id = "categoryList"
        # categoryList.size_hint_y = None
        for i in categories:
            newcat = boxlayout.BoxLayout()
            newcat.orientation = "horizontal"
            newCheckBox = checkbox.CheckBox()
            newLabel = label.Label()
            newLabel.font_size = 24
            newLabel.text = i
            newcat.add_widget(newCheckBox)
            newcat.add_widget(newLabel)
            categoryList.add_widget(newcat)
        # for i in range(10):
        #     newLabel = label.Label()
        #     newLabel.text = str(i)
        #     newLabel.font_size = 24
        #     categoryList.add_widget(newLabel)
        newcat = boxlayout.BoxLayout()
        newcat.orientation = "horizontal"
        newCheckBox = checkbox.CheckBox()
        newLabel = label.Label()
        newLabel.font_size = 24
        newLabel.text = "Other"
        newInput = textinput.TextInput()
        newInput.font_size = 24
        newInput.hint_text = "Category"
        newcat.add_widget(newCheckBox)
        newcat.add_widget(newLabel)
        newcat.add_widget(newInput)
        categoryList.add_widget(newcat)
        categoryScroller.add_widget(categoryList)


class AdministratorLogin(Screen):
    def login(self):
        app = App.get_running_app()
        if (nmsuldap.authenticate(self.ids.usernameInput.text, self.ids.passwordInput.text)):
            self.ids.usernameInput.text = ""
            self.ids.passwordInput.text = ""
            self.ids.failedLogin.text = ""
            app.root.transition = NoTransition()
            app.root.current = "ModificationScreen"
        else:
            self.ids.usernameInput.text = ""
            self.ids.passwordInput.text = ""
            self.ids.failedLogin.text = "Login Failed"
            app.root.transition = NoTransition()
            app.root.current = "LoginScreen"

class FeedbackForm(Screen):
    showQuestion2 = BooleanProperty(False)
    showQuestion4 = BooleanProperty(False)
    showQuestion5 = BooleanProperty(False)
    showQuestion6 = BooleanProperty(False)
    def saveFeedback(self):
        app = App.get_running_app()
        root = app.root.ids.feedback_screen
        # IF YES OR IDK SAVE STATE OF FIRST QUESTION
        #     && YES TO STORING and YES QUESTION ASKED
        #        STORE QUESTION 

        # IF YES OR IDK SAVE STATE OF FIRST QUESTION
        #     && YES TO STORING and NO QUESTION ASKED
        #        STORE QUESTION in text field

        # IF NO STORE REASON text field
        
        # 

        if ((root.ids.goodAnswerYes.active or root.ids.goodAnswerIDK.active) and root.ids.saveQuestionNo.active):
            # save answer quality
            app.root.ids.question_screen.ids.questionInput.text = ""
            app.root.transition = NoTransition()
            app.root.current = "QuestionScreen"
            showQuestion2 = BooleanProperty(False)
            showQuestion3 = BooleanProperty(False)
            showQuestion4 = BooleanProperty(False)
            showQuestion5 = BooleanProperty(False)
            root.ids.goodAnswerYes.active = False
            root.ids.goodAnswerNo.active = False
            root.ids.goodAnswerIDK.active = False
            root.ids.saveQuestionYes.active = False
            root.ids.saveQuestionNo.active = False
            root.ids.actualQuestionYes.active = False
            root.ids.actualQuestionNo.active = False
            root.ids.realQuestion.text = ""
            root.ids.notReason.text = ""
            root.ids.feedbackCategories.clear_widgets()

        elif ((root.ids.goodAnswerYes.active or root.ids.goodAnswerIDK.active) and root.ids.saveQuestionYes.active and root.ids.actualQuestionYes.active):
            # save answer quality and question and any categories
            app.root.ids.question_screen.ids.questionInput.text = ""
            app.root.transition = NoTransition()
            app.root.current = "QuestionScreen"
            showQuestion2 = BooleanProperty(False)
            showQuestion3 = BooleanProperty(False)
            showQuestion4 = BooleanProperty(False)
            showQuestion5 = BooleanProperty(False)
            root.ids.goodAnswerYes.active = False
            root.ids.goodAnswerNo.active = False
            root.ids.goodAnswerIDK.active = False
            root.ids.saveQuestionYes.active = False
            root.ids.saveQuestionNo.active = False
            root.ids.actualQuestionYes.active = False
            root.ids.actualQuestionNo.active = False
            root.ids.realQuestion.text = ""
            root.ids.notReason.text = ""
            root.ids.feedbackCategories.clear_widgets()

        elif ((root.ids.goodAnswerYes.active or root.ids.goodAnswerIDK.active) and root.ids.saveQuestionNo.active and root.ids.actualQuestionNo.active and root.ids.realQuestion.text != None and root.ids.realQuestion.text != ""):
            # save answer quality and revised question and any categories
            app.root.ids.question_screen.ids.questionInput.text = ""
            app.root.transition = NoTransition()
            app.root.current = "QuestionScreen"
            showQuestion2 = BooleanProperty(False)
            showQuestion3 = BooleanProperty(False)
            showQuestion4 = BooleanProperty(False)
            showQuestion5 = BooleanProperty(False)
            root.ids.goodAnswerYes.active = False
            root.ids.goodAnswerNo.active = False
            root.ids.goodAnswerIDK.active = False
            root.ids.saveQuestionYes.active = False
            root.ids.saveQuestionNo.active = False
            root.ids.actualQuestionYes.active = False
            root.ids.actualQuestionNo.active = False
            root.ids.realQuestion.text = ""
            root.ids.notReason.text = ""
            root.ids.feedbackCategories.clear_widgets()
        
        elif (root.ids.goodAnswerNo.active and root.ids.notReason.text != None and root.ids.notReason.text != "" and root.ids.saveQuestionYes.active and root.ids.actualQuestionYes.active):
            # save answer quality and question and any categories
            app.root.ids.question_screen.ids.questionInput.text = ""
            app.root.transition = NoTransition()
            app.root.current = "QuestionScreen"
            showQuestion2 = BooleanProperty(False)
            showQuestion3 = BooleanProperty(False)
            showQuestion4 = BooleanProperty(False)
            showQuestion5 = BooleanProperty(False)
            root.ids.goodAnswerYes.active = False
            root.ids.goodAnswerNo.active = False
            root.ids.goodAnswerIDK.active = False
            root.ids.saveQuestionYes.active = False
            root.ids.saveQuestionNo.active = False
            root.ids.actualQuestionYes.active = False
            root.ids.actualQuestionNo.active = False
            root.ids.realQuestion.text = ""
            root.ids.notReason.text = ""
            root.ids.feedbackCategories.clear_widgets()

        elif (root.ids.goodAnswerNo.active and root.ids.notReason.text != None and root.ids.notReason.text != "" and root.ids.saveQuestionNo.active and root.ids.actualQuestionNo.active and root.ids.realQuestion.text != None and root.ids.realQuestion.text != ""):
            # save answer quality and revised question and any categories
            app.root.ids.question_screen.ids.questionInput.text = ""
            app.root.transition = NoTransition()
            app.root.current = "QuestionScreen"
            showQuestion2 = BooleanProperty(False)
            showQuestion3 = BooleanProperty(False)
            showQuestion4 = BooleanProperty(False)
            showQuestion5 = BooleanProperty(False)
            root.ids.goodAnswerYes.active = False
            root.ids.goodAnswerNo.active = False
            root.ids.goodAnswerIDK.active = False
            root.ids.saveQuestionYes.active = False
            root.ids.saveQuestionNo.active = False
            root.ids.actualQuestionYes.active = False
            root.ids.actualQuestionNo.active = False
            root.ids.realQuestion.text = ""
            root.ids.notReason.text = ""
            root.ids.feedbackCategories.clear_widgets()

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