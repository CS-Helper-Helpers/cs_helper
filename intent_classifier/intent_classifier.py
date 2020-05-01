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
from tensorflow.keras.layers import Dense, LSTM, Bidirectional, Embedding, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint
from slots.find_chunks import chunk_important_date


class IntentClassifier:
    def __init__(self):
        self.hello = "hello"

    # def __init__(self, *args, **kwargs):
    #     super(IntentClassifier, self).__init__(*args, **kwargs)
    def load_dataset(self, piece=False):

        if not piece:
            engine = db.getBotDBEngine()
            query = "select question as Sentence, cat as Intent from TrainingQuestions"
            df = pd.read_sql_query(query, con=engine)

            print(df.head())
            intent = df["Intent"]
            unique_intent = list(set(intent))
            sentences = list(df["Sentence"])

            query = "select count(*) from Categories"
            df = pd.read_sql_query(query, con=engine)
            catlength = df.loc[0].at["count(*)"]

            return (intent, unique_intent, sentences, catlength)

        else:
            if piece == "sentences":
                engine = db.getBotDBEngine()
                query = "select question as Sentence from TrainingQuestions"
                df = pd.read_sql_query(query, con=engine)
                return list(df["Sentence"])

            if piece == "uniqueintents":
                engine = db.getBotDBEngine()
                query = "select distinct cat as Intent from TrainingQuestions"
                df = pd.read_sql_query(query, con=engine)
                return list(df["Intent"])

    def cleaning(self, sentences):
        words = []
        for s in sentences:
            clean = re.sub(r"[^ a-z A-Z 0-9]", " ", s)
            w = word_tokenize(clean)
            # lemmatizing
            words.append([i.lower() for i in w])
        return words

    def create_tokenizer(self, words, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'):
        """Create tokenizer
        """
        token = Tokenizer(filters=filters)
        token.fit_on_texts(words)
        return token

    def get_max_length(self, words):
        """Gets max length of a word
        """
        return len(max(words, key=len))

    def encoding_doc(self, token, words):
        return token.texts_to_sequences(words)

    def padding_doc(self, encoded_doc, max_length):
        return pad_sequences(encoded_doc, maxlen=max_length, padding="post")

    def one_hot(self, encode):
        o = OneHotEncoder(sparse=False)
        return o.fit_transform(encode)

    def create_model(self, vocab_size, max_length, catlength):
        model = Sequential()
        model.add(Embedding(vocab_size, 128, input_length=max_length, trainable=False))
        model.add(Bidirectional(LSTM(128)))
        #   model.add(LSTM(128))
        model.add(Dense(32, activation="relu"))
        model.add(Dropout(0.5))
        model.add(Dense(catlength, activation="softmax"))

        return model

    def train_model(self):

        intent, unique_intent, sentences, catlength = self.load_dataset()

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
            padded_doc, output_one_hot, shuffle=True, test_size=0.2
        )
        print("Shape of train_X = %s and train_Y = %s" % (train_X.shape, train_Y.shape))
        print("Shape of val_X = %s and val_Y = %s" % (val_X.shape, val_Y.shape))

        model = self.create_model(vocab_size, max_length, len(unique_intent))

        model.compile(
            loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
        )
        model.summary()

        filename = "model.h5"
        checkpoint = ModelCheckpoint(
            filename, monitor="val_loss", verbose=0, save_best_only=True, mode="min"
        )

        model.fit(
            train_X,
            train_Y,
            epochs=250,
            batch_size=32,
            validation_data=(val_X, val_Y),
            callbacks=[checkpoint],
            verbose=0,
        )

    #    hist = model.fit(train_X, train_Y, epochs = 100, batch_size = 32, validation_data = (val_X, val_Y), callbacks = [checkpoint], verbose = 0)

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

        return pred

    def get_final_output(self, text, pred, classes):
        print("In get final output")
        predictions = pred[0]

        classes = np.array(classes)
        ids = np.argsort(-predictions)
        classes = classes[ids]
        predictions = -np.sort(-predictions)

        for i in range(pred.shape[1]):
            print("%s has confidence = %s" % (classes[i], (predictions[i])))

            chunks = self.chunk_utterance(classes[i], text)
            # now we query database for an answer
            # if an answer is found, we break out of this loop
            # else we go to the next intent category ?? maybe break early given low confidence

        return ""

    def query_database(self, intent_cat_class, doc):
        entity_list = []
        for ent in doc.ents:
            entity_list.append((ent.label_, ent.text))

        engine = db.getBotDBEngine()

        # Fix cat_class names in model to match table names in DB
        if intent_cat_class == "important_date":
            intent_cat_class = "ImportantDates"

        query = "select event_date, important_event from {0} where important_event = '{1}'".format(
            intent_cat_class, ent.label_
        )
        df = pd.read_sql_query(query, con=engine)
        # print(df)

        if df.empty:
            # then we did not get a result
            return None
        else:
            # then return the result found
            return df

    def chunk_utterance(self, intent, utterance):
        """ chunk_utterance finds variable slots """
        # print("In chunk utterance")
        # print("Utterance: ", utterance, "\tIntent: ", intent)

        if intent == "important_date":
            # print("in important date chunk")
            doc = chunk_important_date(utterance)
            # print("Entities in '%s'" % utterance)
            # for ent in doc.ents:
            #    print(ent.label_, ent.text)
        elif intent == "course":
            pass
        elif intent == "professor":
            pass
        elif intent == "location":
            pass
        else:
            print("intent didn't match")
        return doc

    def answer(self, text):
        print("In answer")

        # Load model
        model = load_model("model.h5")  # GGRRRRRR

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

            df_result = self.query_database(classes[i], doc)

            if df_result is not None:
                # print("Found a result: \n", df_result)

                # clean and return string response
                answer = df_result["event_date"][0]  # Will need to fix later
                return answer
