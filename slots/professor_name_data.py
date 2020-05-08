def get_substring_label_truple(intent, label_indicator, label):
    start = intent.find(label_indicator)
    end = start + len(label_indicator)
    return (start, end, label)


def get_data():
    PROFESSOR_NAMES = [
        "Tran",
        "Dr Tran",
        "Doctor Tran",
        "Pontelli",
        "Dr Pontelli",
        "Doctor Pontelli",
        "Cao",
        "Dr Cao",
        "Doctor Cao",
        "Cook",
        "Dr Cook",
        "Doctor Cook",
        "Hamilton",
        "Dr Hamilton",
        "Doctor Hamilton",
        "Le",
        "Dr Le",
        "Doctor Le",
        "Misra",
        "Dr Misra",
        "Doctor Misra",
        "Nagarkar",
        "Dr Nagarkar",
        "Doctor Nagarkar",
        "Parth",
        "Dr Parth",
        "Doctor Parth",
        "Pivkina",
        "Dr Pivkina",
        "Doctor Pivkina",
        "Song",
        "Dr Song",
        "Doctor Song",
        "Toups",
        "Dr Toups",
        "Doctor Toups",
        "Vishwanathan",
        "Dr Vishwanathan",
        "Doctor Vishwanathan",
        "Wang",
        "Dr Wang",
        "Doctor Wang",
        "Muhammad Hamdi",
        "Dr Muhammad Hamdi",
        "Doctor Muhammad Hamdi",
        "Cooper",
        "Dr Cooper",
        "Doctor Cooper",
        "Steiner",
        "Dr Steiner",
        "Doctor Steiner",
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
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )

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
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
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
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
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
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
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
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
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
        # print(
        #     '("'
        #     + text
        #     + '","professor","'
        #     + prof
        #     + '","'
        #     + PROFESSOR_NAME_LABEL
        #     + '"),'
        # )
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
