# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:20:24 2020

@author: arima
"""

# https://towardsdatascience.com/a-brief-introduction-to-intent-classification-96fda6b1f557
# Classifies into 21 intents

from sqlalchemy import create_engine
import database.engine as db
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import nltk
import re
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import (
    Dense,
    LSTM,
    Bidirectional,
    Embedding,
    Dropout,
    Flatten,
)
from tensorflow.keras.callbacks import ModelCheckpoint
from slots.find_chunks import (
    chunk_important_date,
    chunk_course,
    chunk_professor,
    chunk_course_info,
    chunk_professor_name,
)


class IntentClassifier:
    def __init__(self):
        self.hello = "hello"

    def load_dataset(self, piece=False):

        if not piece:
            engine = db.getBotDBEngine()
            query = "select question as Sentence, cat as Intent from TrainingQuestions"
            df = pd.read_sql_query(query, con=engine)

            # print(df.head())
            intent = df["Intent"]
            unique_intent = list(set(intent))
            # query = "select category from Categories"
            # df_ui = pd.read_sql_query(query, con=engine)
            # unique_intent = list(df_ui['category'])
            # print("Unique intent: ", unique_intent)
            sentences = list(df["Sentence"])

            # query = "select count(*) from Categories"
            # df = pd.read_sql_query(query, con=engine)
            catlength = len(unique_intent)

            print("\n\n\nunique_intent: ", unique_intent)

            return (intent, unique_intent, sentences, catlength)

        elif piece == "sentences":
            engine = db.getBotDBEngine()
            query = "select question as Sentence from TrainingQuestions"
            df = pd.read_sql_query(query, con=engine)
            return list(df["Sentence"])

        elif piece == "uniqueintents":
            engine = db.getBotDBEngine()
            query = "select distinct cat as Intent from TrainingQuestions"
            df = pd.read_sql_query(query, con=engine)
            return list(df["Intent"])
        elif piece == "random_sample":
            engine = db.getBotDBEngine()
            sentences = []
            intent = []

            # get categories
            query = "select category from Categories"
            df = pd.read_sql_query(query, con=engine)
            cat = list(df["category"])
            for c in cat:
                query = "select cat as Intent, question as Sentence from TrainingQuestions where cat = '{}'".format(
                    c
                )
                df = pd.read_sql_query(query, con=engine)
                df = df.sample(n=100, replace=False,)
                sentences.extend(list(df["Sentence"]))
                intent.extend(list(df["Intent"]))
            unique_intent = list(set(intent))
            catlength = len(unique_intent)
            return intent, unique_intent, sentences, catlength

    def cleaning(self, sentences):
        words = []
        for s in sentences:
            clean = re.sub(r"[^ a-z A-Z 0-9]", " ", s)
            w = word_tokenize(clean)
            # lemmatizing
            words.append([i.lower() for i in w])
        return words

    def create_tokenizer(self, words, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'):
        token = Tokenizer(filters=filters)
        token.fit_on_texts(words)
        return token

    def get_max_length(self, words):
        return len(max(words, key=len))

    def encoding_doc(self, token, words):
        return token.texts_to_sequences(words)

    def padding_doc(self, encoded_doc, max_length):
        return pad_sequences(encoded_doc, maxlen=max_length, padding="post")

    def one_hot(self, encode):
        o = OneHotEncoder(sparse=False, categories="auto")
        return o.fit_transform(encode)

    def create_model(self, vocab_size, max_length, catlength):
        model = Sequential()
        model.add(Embedding(vocab_size, 128, input_length=max_length, trainable=False))
        # model.add(Bidirectional(LSTM(128, activation=“sigmoid”)))
        model.add(LSTM(128))
        model.add(Dense(32, activation="relu"))
        model.add(Dropout(0.5))
        model.add(Flatten())
        model.add(Dense(catlength, activation="softmax"))
        return model

    def train_model(self):

        intent, unique_intent, sentences, catlength = self.load_dataset()

        # print("Intent: ", intent)
        # print("Unique intent: ", unique_intent)
        # print("Sentences: ", sentences)
        # print("cat length: ", catlength)

        nltk.download("stopwords")
        nltk.download("punkt")

        #    stemmer = LancasterStemmer()
        LancasterStemmer()

        cleaned_words = self.cleaning(sentences)
        print(len(cleaned_words))
        print(cleaned_words[:3])

        word_tokenizer = self.create_tokenizer(cleaned_words)
        vocab_size = len(word_tokenizer.word_index) + 1
        max_length = self.get_max_length(cleaned_words)

        print("Vocab size = ", vocab_size, " and Maximum length = ", max_length)

        encoded_doc = self.encoding_doc(word_tokenizer, cleaned_words)

        padded_doc = self.padding_doc(encoded_doc, max_length)
        padded_doc[:5]

        print("Shape of padded docs = ", padded_doc.shape)

        # tokenizer with filter changed
        output_tokenizer = self.create_tokenizer(
            unique_intent, filters='!"#$%&()*+,-/:;<=>?@[\\]^`{|}~'
        )

        output_tokenizer.word_index

        encoded_output = self.encoding_doc(output_tokenizer, intent)
        encoded_output = np.array(encoded_output).reshape(len(encoded_output), 1)
        encoded_output.shape

        output_one_hot = self.one_hot(encoded_output)
        output_one_hot.shape

        from sklearn.model_selection import train_test_split

        train_X, val_X, train_Y, val_Y = train_test_split(
            padded_doc, output_one_hot, shuffle=True, test_size=0.65
        )
        print("Shape of train_X = %s and train_Y = %s" % (train_X.shape, train_Y.shape))
        print("Shape of val_X = %s and val_Y = %s" % (val_X.shape, val_Y.shape))

        print(
            "\n\n\nVOCAB SIZE: ",
            vocab_size,
            "MAX LENG: ",
            max_length,
            "CATLENG: ",
            catlength,
        )

        model = self.create_model(vocab_size, max_length, catlength)

        model.compile(
            loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
        )
        model.summary()

        filename = "intent_classifier/model.h5"
        checkpoint = ModelCheckpoint(
            filename, monitor="val_loss", verbose=0, save_best_only=True, mode="min"
        )

        model.fit(
            train_X,
            train_Y,
            epochs=100,
            batch_size=32,
            validation_data=(val_X, val_Y),
            callbacks=[checkpoint],
            verbose=2,
        )

        # Original
        # model.fit(
        #     train_X,
        #     train_Y,
        #     epochs=100,
        #     batch_size=32,
        #     validation_data=(val_X, val_Y),
        #     callbacks=[checkpoint],
        #     verbose=2,
        # )

        # loss, accuracy = model.evaluate(train_X, train_Y, verbose=False)
        # print("Training Accuracy: {:.4f}".format(accuracy))
        loss, accuracy = model.evaluate(val_X, val_Y, verbose=False)
        print("Testing Accuracy:  {:.4f}".format(accuracy))

    def predictions(self, utterance, model):
        clean_utter = re.sub(r"[^ a-z A-Z 0-9]", " ", utterance)
        clean_utter = word_tokenize(clean_utter)
        clean_utter = [w.lower() for w in clean_utter]

        # Remove this block if possible
        sentences = self.load_dataset("sentences")
        cleaned_words = self.cleaning(sentences)
        max_length = self.get_max_length(cleaned_words)
        word_tokenizer = self.create_tokenizer(cleaned_words)

        test_ls = word_tokenizer.texts_to_sequences(clean_utter)
        print(clean_utter)
        # Check for unknown words
        if [] in test_ls:
            test_ls = list(filter(None, test_ls))

        test_ls = np.array(test_ls).reshape(1, len(test_ls))

        x = self.padding_doc(test_ls, max_length)

        pred = model.predict_proba(x)

        print(pred)

        return pred

    # def get_final_output(self, text, pred, classes):
    #     print("In get final output")
    #     predictions = pred[0]

    #     classes = np.array(classes)
    #     ids = np.argsort(-predictions)
    #     classes = classes[ids]
    #     predictions = -np.sort(-predictions)

    #     for i in range(pred.shape[1]):
    #         print("%s has confidence = %s" % (classes[i], (predictions[i])))

    #         chunks = self.chunk_utterance(classes[i], text)
    #         # now we query database for an answer
    #         # if an answer is found, we break out of this loop
    #         # else we go to the next intent category ?? maybe break early given low confidence

    #     return ""

    def query_database(self, intent_cat_class, doc):
        entity_list = []
        for ent in doc.ents:
            print("ent: ", ent)
            entity_list.append((ent.label_, ent.text))

            engine = db.getBotDBEngine()

            # Fix cat_class names in model to match table names in DB
            if intent_cat_class == "important_date":
                intent_cat_class = "ImportantDates"

                query = "select event_date, important_event from {0} where important_event = '{1}'".format(
                    intent_cat_class, ent.label_
                )
            elif intent_cat_class == "professor":
                intent_cat_class = "Professors"

                query = "select * from {0} where prof_name like '%%{1}%%'".format(
                    intent_cat_class, ent.text
                )
            elif intent_cat_class == "course":
                intent_cat_class = "Courses"

                query = "select * from {0} where subj like '%%{1}%%' or crse like '%%{1}%%'".format(
                    intent_cat_class, ent.text
                )
            else:
                query = ""

            try:
                df = pd.read_sql_query(query, con=engine, params=())

            except:
                # then we did not get a result
                return None
            else:
                # then return the result found
                return df

    def chunk_utterance(self, intent, utterance):
        """ chunk_utterance finds variable slots """
        print("In chunk utterance")
        print("Utterance: ", utterance, "\tIntent: ", intent)
        if intent == "important_date":
            print("in important date chunk")
            doc = chunk_important_date(utterance)
            # print("Entities in '%s'" % utterance)
            # for ent in doc.ents:
            #    print(ent.label_, ent.text)
        elif intent == "course":
            print("in course chunk")
            doc = chunk_course(utterance)
        elif intent == "professor":
            print("professor chunk")
            doc = chunk_professor_name(utterance)
        elif intent == "location":
            doc = None
            print("location chunk")
        else:
            doc = None
            print("intent didn't match")

        return doc

    def answer(self, text):
        print("In answer")

        # Load model
        model = load_model("intent_classifier/model.h5")

        # Get predicted intent category classification of uterrance
        pred = self.predictions(text, model)

        for p in pred:
            print(p)

        # Get unique intent categories
        unique_intent = self.load_dataset("uniqueintents")
        print(pred, unique_intent)

        # Sort predictions
        predictions = pred[0]
        classes = np.array(unique_intent)
        ids = np.argsort(-predictions)
        print(ids)
        classes = classes[ids]
        predictions = -np.sort(-predictions)

        for i in range(pred.shape[1]):
            # Iterate through the classifications until a db query
            # is found. If we find a result, we clean it and return it.
            # Else, we look through the result with the next highest confidence.

            print("%s has confidence = %s" % (classes[i], (predictions[i])))
            doc = self.chunk_utterance(classes[i], text)
            # print("doc: ", doc)

            if doc is None:
                return "I am still learning some things and cannot help with that right now."

            else:
                df_result = self.query_database(classes[i], doc)  # THIS IS THE REAL ONE
                # df_result = self.query_database("course", doc)
                print("df ", df_result)
                if df_result is not None:
                    # print("Found a result: \n", df_result)
                    try:
                        if classes[i] == "important_date":
                            answer = df_result["event_date"][0]
                            return answer

                        # clean and return string response
                        answer = df_result.iloc[0, 1:]  # Will need to fix later
                        # answer = "TEST ANSWER WE WILL MODIFY"
                        test = ""
                        for i, v in answer.items():
                            test = test + ", " + v
                        return test
                    except:
                        return "I could not find an answer in the database for that question."

                else:
                    return (
                        "I could not find an answer in the database for that question."
                    )
