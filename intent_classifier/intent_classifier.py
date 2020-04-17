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

class IntentClassifier:

    def __init__(self):
        self.hello = "hello"

    # def __init__(self, *args, **kwargs):
    #     super(IntentClassifier, self).__init__(*args, **kwargs)


    def load_dataset(self, piece = False):
        
        if (not piece):
            engine = db.getBotDBEngine()
            query = "select question as Sentence, cat as Intent from TrainingQuestions"
            df = pd.read_sql_query(query, con = engine)

            print(df.head())
            intent = df["Intent"]
            unique_intent = list(set(intent))
            sentences = list(df["Sentence"])

            query = "select count(*) from Categories"
            df = pd.read_sql_query(query, con = engine)
            catlength = df.loc[0].at["count(*)"]

            return (intent, unique_intent, sentences, catlength)

        else:
            if (piece == "sentences"):
                engine = db.getBotDBEngine()
                query = "select question as Sentence from TrainingQuestions"
                df = pd.read_sql_query(query, con = engine)
                return list(df["Sentence"])

            if (piece == "uniqueintents"):
                engine = db.getBotDBEngine()
                query = "select distinct cat as Intent from TrainingQuestions"
                df = pd.read_sql_query(query, con = engine)
                return list(df["Intent"])

    
    def cleaning(self, sentences):
        words = []
        for s in sentences:
            clean = re.sub(r'[^ a-z A-Z 0-9]', " ", s)
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

    def get_max_length(words):
        """Gets max length of a word
        """
        return(len(max(words, key=len)))

    def encoding_doc(token, words):
        return(token.texts_to_sequences(words))

    def padding_doc(encoded_doc, max_length):
        return(pad_sequences(encoded_doc, maxlen=max_length, padding="post"))

    def one_hot(self, encode):
        o = OneHotEncoder(sparse=False)
        return(o.fit_transform(encode))

    def create_model(self, vocab_size, max_length, catlength):
        model = Sequential()
        model.add(Embedding(vocab_size, 128, input_length = max_length, trainable = False))
        model.add(Bidirectional(LSTM(128)))
    #   model.add(LSTM(128))
        model.add(Dense(32, activation = "relu"))
        model.add(Dropout(0.5))
        model.add(Dense(catlength, activation = "softmax"))
    
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
        output_tokenizer = self.create_tokenizer(unique_intent, filters='!"#$%&()*+,-/:;<=>?@[\\]^`{|}~')
                                        
        output_tokenizer.word_index

        encoded_output = self.encoding_doc(output_tokenizer, intent)
        encoded_output = np.array(encoded_output).reshape(len(encoded_output), 1)
        encoded_output.shape  

        output_one_hot = self.one_hot(encoded_output)
        output_one_hot.shape

        from sklearn.model_selection import train_test_split
        train_X, val_X, train_Y, val_Y = train_test_split(padded_doc, output_one_hot, shuffle = True, test_size = 0.2)
        print("Shape of train_X = %s and train_Y = %s" % (train_X.shape, train_Y.shape))
        print("Shape of val_X = %s and val_Y = %s" % (val_X.shape, val_Y.shape))

        model = self.create_model(vocab_size, max_length, catlength)

        model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])
        model.summary()

        filename = 'model.h5'
        checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=0, save_best_only=True, mode='min')

        model.fit(train_X, train_Y, epochs = 100, batch_size = 32, validation_data = (val_X, val_Y), callbacks = [checkpoint], verbose = 0)
    #    hist = model.fit(train_X, train_Y, epochs = 100, batch_size = 32, validation_data = (val_X, val_Y), callbacks = [checkpoint], verbose = 0)

    def predictions(self, text, model):
        clean = re.sub(r'[^ a-z A-Z 0-9]', " ", text)
        test_word = word_tokenize(clean)
        test_word = [w.lower() for w in test_word]

        #Remove this block if possible
        sentences = load_dataset("sentences")
        cleaned_words = cleaning(sentences)
        max_length = get_max_length(cleaned_words)
        word_tokenizer = create_tokenizer(cleaned_words)

        test_ls = word_tokenizer.texts_to_sequences(test_word)
        print(test_word)
        #Check for unknown words
        if [] in test_ls:
            test_ls = list(filter(None, test_ls))
        
        test_ls = np.array(test_ls).reshape(1, len(test_ls))
    
        x = padding_doc(test_ls, max_length)
    
        pred = model.predict_proba(x)
    
        return pred

    def get_final_output(self, pred, classes):
        predictions = pred[0]
    
        classes = np.array(classes)
        ids = np.argsort(-predictions)
        classes = classes[ids]
        predictions = -np.sort(-predictions)

        max = predictions[0]
        count = 0
        for i in range(pred.shape[1]):
            if (predictions[i] > max * 0.9):
                count += 1
        if (count > 1):
            print("Uncertain result:")
            for i in range(pred.shape[1]):
                if (predictions[i] > max * 0.9):
                    print("%s has confidence = %s" % (classes[i], (predictions[i])))
        else:
            engine = db.getBotDBEngine()
            query = "select outvar from OutputVariables where inid in (select inputid from InputVariables where incat = '" + classes[0] + "')"
            df = pd.read_sql_query(query, con = engine)
            if (df.size == 1):
                print("The result is:")
                print("%s with confidence = %s" % (classes[0], (predictions[0])))
                print(df.loc[0].at["outvar"])
                return df.loc[0].at["outvar"]
            elif (df.size > 1):
                print("Unable to get unique result.")
                print("%s with confidence = %s" % (classes[0], (predictions[0])))
            else:
                print("Unable to find an answer for this question.")
                print("%s with confidence = %s" % (classes[0], (predictions[0])))
                
        return ""

    def answer(self, text):
        model = load_model("model.h5")
        pred = predictions(text, model)
        unique_intent = load_dataset("uniqueintents")
        get_final_output(pred, unique_intent)
