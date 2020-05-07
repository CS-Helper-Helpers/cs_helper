def get_substring_label_truple(intent, label_indicator, label):
    start = intent.find(label_indicator)
    end = start + len(label_indicator)
    return (start, end, label)


def get_data():
    PROFESSOR_NAMES = [
        "Son Tran",
        "Enrico Pontelli",
        "Huiping Cao",
        "Jonathan Cook",
        "Bill Hamilton",
        "Tuan Le",
        "Satyajayant Misra",
        "Parth Nagarkar",
        "Inna Pivkina",
        "Joe Song",
        "Z O. Toups",
        "Roopa Vishwanathan",
        "Tao Wang",
        "Shah Muhammad Hamdi",
        "Esther Steiner",
        "Shaun H. Cooper",
        "Roger Hartley",
        "Hing Leung",
        "Hue McCoy",
        "Joseph Pfeiffer",
    ]
    PROFESSOR_NAME_LABEL = "PROFESSOR_NAME"
    PROFESSOR_NAME_TRAIN_DATA = []

    for prof in PROFESSOR_NAMES:
        text = "Is " + prof + " available to meet?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)

        text = "What are " + prof + " office hours?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)

        text = "Is " + prof + " involved in any research?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)

        text = "Does " + prof + " teach databases?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)

        text = "How can I reach " + prof + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)

        text = "Is " + prof + " goint to be teaching summer courses?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)

        text = "What courses does " + prof + " teach?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)

    return PROFESSOR_NAME_TRAIN_DATA, [PROFESSOR_NAME_LABEL]
