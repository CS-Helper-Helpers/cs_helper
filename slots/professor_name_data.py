def get_substring_label_truple(intent, label_indicator, label):
    start = intent.find(label_indicator)
    end = start + len(label_indicator)
    return (start, end, label)


def get_data():
    PROFESSOR_NAMES = [
        "Tran",
        "Pontelli",
        "Cao",
        "Cook",
        "Hamilton",
        "Le",
        "Misra",
        "Nagarkar",
        "Parth",
        "Pivkina",
        "Song",
        "Toups",
        "Vishwanathan",
        "Wang",
        "Muhammad Hamdi",
        "Cooper",
        "Steiner",
    ]
    PROFESSOR_NAME_LABEL = "PROFESSOR_NAME"
    PROFESSOR_NAME_TRAIN_DATA = []

    for prof in PROFESSOR_NAMES:
        text = "Is dr " + prof + " available to meet?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )

        text = "What are doctor " + prof + " office hours?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
        text = "Is professor " + prof + " involved in any research?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
        text = "Does dr " + prof + " teach databases?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
        text = "How can I reach dr " + prof + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
        text = "Is " + prof + " going to be teaching summer courses?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
        text = "What courses does professor " + prof + " teach?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, prof, PROFESSOR_NAME_LABEL)
                ]
            },
        )
        PROFESSOR_NAME_TRAIN_DATA.append(my_tuple)
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
    return PROFESSOR_NAME_TRAIN_DATA, [PROFESSOR_NAME_LABEL]
