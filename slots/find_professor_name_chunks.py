"""Example of training an additional entity type
This script shows how to add a new entity type to an existing pretrained NER
model. To keep the example short and simple, only four sentences are provided
as examples. In practice, you'll need many more — a few hundred would be a
good start. You will also likely need to mix in examples of other entity
types, which might be obtained by running the entity recognizer over unlabelled
sentences, and adding their annotations to the training set.
The actual training is performed by looping over the examples, and calling
`nlp.entity.update()`. The `update()` method steps through the words of the
input. At each word, it makes a prediction. It then consults the annotations
provided on the GoldParse instance, to see whether it was right. If it was
wrong, it adjusts its weights so that the correct action will score higher
next time.
After training your model, you can save it to a directory. We recommend
wrapping models as Python packages, for ease of deployment.
For more details, see the documentation:
* Training: https://spacy.io/usage/training
* NER: https://spacy.io/usage/linguistic-features#named-entities
Compatible with: spaCy v2.1.0+
Last tested with: v2.1.0
"""
from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding

professor = {}


def get_substring_label_tuple(intent, label_indicator, label):
    start = intent.find(label_indicator)
    end = start + len(label_indicator)
    return (start, end, label)


# Professor Names
PROFESSOR_NAME_LABEL = "PROFESSOR_NAME"
PROFESSOR_NAME_TRAIN_DATA = [
    (
        "When are Tran office hours?",
        {
            "entities": [
                get_substring_label_tuple(
                    "When are Tran office hours?", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Does Tran have any available office hours this week?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Does Tran have any available office hours this week?",
                    "Tran",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What are Tran office hours",
        {
            "entities": [
                get_substring_label_tuple(
                    "What are Tran office hours", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Is Tran available to meet",
        {
            "entities": [
                get_substring_label_tuple(
                    "Is Tran available to meet", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Does Tran have any available office hours this week?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Does Tran have any available office hours this week?",
                    "Tran",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What time is Tran office hours",
        {
            "entities": [
                get_substring_label_tuple(
                    "What time is Tran office hours", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "can Tran meet with me today",
        {
            "entities": [
                get_substring_label_tuple(
                    "can Tran meet with me today", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What room is Tran in?",
        {
            "entities": [
                get_substring_label_tuple(
                    "What room is Tran in?", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Where is Tran office?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Where is Tran office?",
                    "Tran",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "Does Tran have an office in this building",
        {
            "entities": [
                get_substring_label_tuple(
                    "Does Tran have an office in this building", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Where can I find Tran?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Where can I find Tran?", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Do you know where Tran office is?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Do you know where Tran office is?",
                    "Tran",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What's Tran room number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What's Tran room number", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can I reach Tran",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can I reach Tran", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I get the email address for Tran?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I get the email address for Tran?",
                    "Tran",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What is Tran phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Tran phone number", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Tran?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Tran?", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Tran contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Tran contact info",
                    "Tran",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Tran",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Tran", "Tran", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "When are Cooper office hours?",
        {
            "entities": [
                get_substring_label_tuple(
                    "When are Cooper office hours?", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Does Cooper have any available office hours this week?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Does Cooper have any available office hours this week?",
                    "Cooper",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What are Cooper office hours",
        {
            "entities": [
                get_substring_label_tuple(
                    "What are Cooper office hours", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Is Cooper available to meet",
        {
            "entities": [
                get_substring_label_tuple(
                    "Is Cooper available to meet", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Does Cooper have any available office hours this week?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Does Cooper have any available office hours this week?",
                    "Cooper",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What time is Cooper office hours",
        {
            "entities": [
                get_substring_label_tuple(
                    "What time is Cooper office hours", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "can Cooper meet with me today",
        {
            "entities": [
                get_substring_label_tuple(
                    "can Cooper meet with me today", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What room is Cooper in?",
        {
            "entities": [
                get_substring_label_tuple(
                    "What room is Cooper in?", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Where is Cooper office?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Where is Cooper office?",
                    "Cooper",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "Does Cooper have an office in this building",
        {
            "entities": [
                get_substring_label_tuple(
                    "Does Cooper have an office in this building", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Where can I find Cooper?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Where can I find Cooper?", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Do you know where Cooper office is?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Do you know where Cooper office is?",
                    "Cooper",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What's Cooper room number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What's Cooper room number", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can I reach Cooper",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can I reach Cooper", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I get the email address for Cooper?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I get the email address for Cooper?",
                    "Cooper",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What is Cooper phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Cooper phone number", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Cooper?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Cooper?", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Cooper contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Cooper contact info",
                    "Cooper",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Cooper",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Cooper", "Cooper", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "When are Pontelli office hours?",
        {
            "entities": [
                get_substring_label_tuple(
                    "When are Pontelli office hours?", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Does Pontelli have any available office hours this week?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Does Pontelli have any available office hours this week?",
                    "Pontelli",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What are Pontelli office hours",
        {
            "entities": [
                get_substring_label_tuple(
                    "What are Pontelli office hours", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Is Pontelli available to meet",
        {
            "entities": [
                get_substring_label_tuple(
                    "Is Pontelli available to meet", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Does Pontelli have any available office hours this week?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Does Pontelli have any available office hours this week?",
                    "Pontelli",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What time is Pontelli office hours",
        {
            "entities": [
                get_substring_label_tuple(
                    "What time is Pontelli office hours", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "can Pontelli meet with me today",
        {
            "entities": [
                get_substring_label_tuple(
                    "can Pontelli meet with me today", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What room is Pontelli in?",
        {
            "entities": [
                get_substring_label_tuple(
                    "What room is Pontelli in?", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Where is Pontelli office?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Where is Pontelli office?",
                    "Pontelli",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "Does Pontelli have an office in this building",
        {
            "entities": [
                get_substring_label_tuple(
                    "Does Pontelli have an office in this building", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Where can I find Pontelli?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Where can I find Pontelli?", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Do you know where Pontelli office is?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Do you know where Pontelli office is?",
                    "Pontelli",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What's Pontelli room number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What's Pontelli room number", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can I reach Pontelli",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can I reach Pontelli", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I get the email address for Pontelli?",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I get the email address for Pontelli?",
                    "Pontelli",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "What is Pontelli phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Pontelli phone number", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Pontelli?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Pontelli?", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Pontelli contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Pontelli contact info",
                    "Pontelli",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Pontelli",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Pontelli", "Pontelli", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Cook phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Cook phone number", "Cook", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Cook?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Cook?", "Cook", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Cook contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Cook contact info",
                    "Cook",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Cook",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Cook", "Cook", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Cao phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Cao phone number", "Cao", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Cao?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Cao?", "Cao", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Cao contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Cao contact info",
                    "Cao",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Cao",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Cao", "Cao", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Hamilton phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Hamilton phone number", "Hamilton", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Hamilton?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Hamilton?", "Hamilton", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Hamilton contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Hamilton contact info",
                    "Hamilton",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Hamilton",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Hamilton", "Hamilton", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Tuan phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Tuan phone number", "Tuan", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Tuan?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Tuan?", "Tuan", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Tuan contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Tuan contact info",
                    "Tuan",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Tuan",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Tuan", "Tuan", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Misra phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Misra phone number", "Misra", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Misra?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Misra?", "Misra", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Misra contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Misra contact info",
                    "Misra",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Misra",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Misra", "Misra", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Parth phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Parth phone number", "Parth", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Parth?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Parth?", "Parth", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Parth contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Parth contact info",
                    "Parth",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Parth",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Parth", "Parth", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Pivkini phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Pivkini phone number", "Pivkini", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Pivkini?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Pivkini?", "Pivkini", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Pivkini contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Pivkini contact info",
                    "Pivkini",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Pivkini",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Pivkini", "Pivkini", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Song phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Song phone number", "Song", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Song?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Song?", "Song", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Song contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Song contact info",
                    "Song",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Song",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Song", "Song", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Toups phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Toups phone number", "Toups", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Toups?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Toups?", "Toups", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Toups contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Toups contact info",
                    "Toups",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Toups",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Toups", "Toups", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Wang phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Wang phone number", "Wang", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Wang?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Wang?", "Wang", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Wang contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Wang contact info",
                    "Wang",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Wang",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Wang", "Wang", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "What is Steiner phone number",
        {
            "entities": [
                get_substring_label_tuple(
                    "What is Steiner phone number", "Steiner", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "How can a get a hold of Steiner?",
        {
            "entities": [
                get_substring_label_tuple(
                    "How can a get a hold of Steiner?", "Steiner", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
    (
        "Can I have Steiner contact info",
        {
            "entities": [
                get_substring_label_tuple(
                    "Can I have Steiner contact info",
                    "Steiner",
                    PROFESSOR_NAME_LABEL,
                )
            ]
        },
    ),
    (
        "I need to call Steiner",
        {
            "entities": [
                get_substring_label_tuple(
                    "I need to call Steiner", "Steiner", PROFESSOR_NAME_LABEL
                )
            ]
        },
    ),
]


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
)
def chunk_professor_name(model=None, new_model_name="class", output_dir=None, n_iter=30):
    """Set up the pipeline and entity recognizer, and train the new entity."""
    random.seed(0)
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe("ner")

    ner.add_label(PROFESSOR_NAME_LABEL)  # add new entity label to entity recognizer
    if model is None:
        optimizer = nlp.begin_training()
    else:
        optimizer = nlp.resume_training()
    move_names = list(ner.move_names)
    # get names of other pipes to disable them during training
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    with nlp.disable_pipes(*other_pipes):  # only train NER
        sizes = compounding(1.0, 4.0, 1.001)
        # batch up the examples using spaCy's minibatch
        for itn in range(n_iter):
            random.shuffle(PROFESSOR_NAME_TRAIN_DATA)
            batches = minibatch(PROFESSOR_NAME_TRAIN_DATA, size=sizes)
            losses = {}
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)
            print("Losses", losses)

    # test the trained model
    test_text = "Can Cooper meet today?"
    # test_text = "Are There office hours today?"
    doc = nlp(test_text)
    print("Entities in '%s'" % test_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta["name"] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        # Check the classes have loaded back consistently
        assert nlp2.get_pipe("ner").move_names == move_names
        doc2 = nlp2(test_text)
        for ent in doc2.ents:
            print(ent.label_, ent.text)


chunk_professor_name()


    