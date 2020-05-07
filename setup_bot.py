from intent_classifier.intent_classifier import IntentClassifier
from slots.train_course_chunker import train_course
from slots.train_important_date_chunker import train_important_date
from slots.train_professor_chunker import train_professor
from slots.train_professor_name_chunker import train_professor_name
from slots.train_course_info_chunker import train_course_info


def bot_setup():
    print("Training Intent Classifier...")
    ic = IntentClassifier()
    ic.train_model()
    print("done training Intent Classifier")

    # print("Training Course Chunker...")
    # train_course()
    # print("done training Course Chunker")

    # print("Training Course Info Chunker...")
    # train_course_info()
    # print("done training Course Info Chunker")

    # print("Training Important Date...")
    # train_important_date()
    # print("done training Important Date")

    # print("Training Professor Chunker...")
    # train_professor()
    # print("done training Professor Chunker")

    # print("Training Professor Name Chunker...")
    # train_professor_name()
    # print("done training Professor Name Chunker")

    # print("Training Location Chunker...")
    # train_location()
    # print("done training Location Chunker")


bot_setup()
