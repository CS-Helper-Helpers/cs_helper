
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

def load_chunker_training_questions(self):
    engine = db.getBotDBEngine()
    query = "select question as Utterance, slot as Slot, label as Label from TrainingQuestions"
    df = pd.read_sql_query(query, con = engine)

    print(df.head())