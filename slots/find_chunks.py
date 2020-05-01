import os
import spacy

def chunk_important_date(utterance):
    """ find the chunks associated with an important date utterance """
    # load model
    
    important_date_dir = os.path.join(os.getcwd(), 'important_date/')
    id_nlp = spacy.load(important_date_dir)
    #print(id_nlp.meta)
    
    doc = id_nlp(utterance)


    print("Entities in '%s'" % utterance)
    for ent in doc.ents:
        print(ent.label_, ent.text)
    # pass utterance through it
    # return chunks
    # pass



