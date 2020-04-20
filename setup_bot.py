from intent_classifier.intent_classifier import IntentClassifier

def bot_setup():
    ic = IntentClassifier()
    ic.train_model()

bot_setup()