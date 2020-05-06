import os
import spacy


def chunk_important_date(utterance):
    """ find the chunks associated with an important date utterance """
    print("\n\nIn chunk important date")

    # load model
    important_date_dir = "slots/important_date/"
    id_nlp = spacy.load(important_date_dir)
    # print(id_nlp.meta)

    doc = id_nlp(utterance)

    # Take a look at doc like so...
    # print("Entities in '%s'" % utterance)
    # for ent in doc.ents:
    #     print(ent.label_, ent.text)

    return doc


def chunk_course(utterance):
    """ find the chunks associated with an course utterance """
    print("\n\nIn chunk course")

    # load model
    course_dir = "slots/course/"
    id_nlp = spacy.load(course_dir)
    # print(id_nlp.meta)

    doc = id_nlp(utterance)

    # Take a look at doc like so...
    # print("Entities in '%s'" % utterance)
    # for ent in doc.ents:
    #     print(ent.label_, ent.text)

    return doc


def chunk_professor(utterance):
    """ find the chunks associated with an professor utterance """
    print("\n\nIn chunk professor")

    # load model
    professor_dir = "slots/professor/"
    id_nlp = spacy.load(professor_dir)
    # print(id_nlp.meta)

    doc = id_nlp(utterance)

    # Take a look at doc like so...
    # print("Entities in '%s'" % utterance)
    # for ent in doc.ents:
    #     print(ent.label_, ent.text)

    return doc


def chunk_professor_name(utterance):
    """ find the chunks associated with an professor name utterance """
    print("\n\nIn chunk professor name")

    # load model
    professor_name_dir = "slots/professor_name/"
    id_nlp = spacy.load(professor_name_dir)
    # print(id_nlp.meta)

    doc = id_nlp(utterance)

    # Take a look at doc like so...
    # print("Entities in '%s'" % utterance)
    # for ent in doc.ents:
    #     print(ent.label_, ent.text)

    return doc
