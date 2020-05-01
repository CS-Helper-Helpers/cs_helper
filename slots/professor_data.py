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
        "Shaun Cooper",
        "Esther Steiner",
    ]

    for prof in PROFESSOR_NAMES:
        OFFICE_HOURS_LABEL = "OFFICE_HOURS"
        OFFICE_HOURS_TRAIN_DATA = []

        my_tuple = (
            "When are " + prof + " office hours?",
            {
                "entities": [
                    get_substring_label_truple(
                        "When are " + prof + " office hours?",
                        "office hours",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        )
        OFFICE_HOURS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Does " + prof + " have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Does " + prof + " have any available office hours this week?",
                        "office hours",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        )
        OFFICE_HOURS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "What are " + prof + " office hours",
            {
                "entities": [
                    get_substring_label_truple(
                        "What are " + prof + " office hours",
                        "office hours",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        )
        OFFICE_HOURS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Is " + prof + " available to meet",
            {
                "entities": [
                    get_substring_label_truple(
                        "Is " + prof + " available to meet",
                        "available",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        )
        OFFICE_HOURS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Does " + prof + " have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Does " + prof + " have any available office hours this week?",
                        "office hours",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        )
        OFFICE_HOURS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "What time is " + prof + " office hours",
            {
                "entities": [
                    get_substring_label_truple(
                        "What time is " + prof + " office hours",
                        "office hours",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        )
        OFFICE_HOURS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "can " + prof + " meet with me today",
            {
                "entities": [
                    get_substring_label_truple(
                        "can " + prof + " meet with me today",
                        "meet",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        )
        OFFICE_HOURS_TRAIN_DATA.append(my_tuple)

        OFFICE_LOCATION_LABEL = "OFFICE_LOCATION"
        OFFICE_LOCATION_TRAIN_DATA = []
        my_tuple = (
            "What room is " + prof + " in?",
            {
                "entities": [
                    get_substring_label_truple(
                        "What room is " + prof + " in?",
                        "what room",
                        OFFICE_LOCATION_LABEL,
                    )
                ]
            },
        )
        OFFICE_LOCATION_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Where is " + prof + " office?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where is " + prof + " office?",
                        "office",
                        OFFICE_LOCATION_LABEL,
                    )
                ]
            },
        )
        OFFICE_LOCATION_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Does " + prof + " have an office in this building",
            {
                "entities": [
                    get_substring_label_truple(
                        "Does " + prof + " have an office in this building",
                        "office",
                        OFFICE_LOCATION_LABEL,
                    )
                ]
            },
        )
        OFFICE_LOCATION_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Where can I find " + prof + "?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where can I find " + prof + "?",
                        "Where",
                        OFFICE_LOCATION_LABEL,
                    )
                ]
            },
        )
        OFFICE_LOCATION_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Do you know where " + prof + " office is?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Do you know where " + prof + " office is?",
                        "office",
                        OFFICE_LOCATION_LABEL,
                    )
                ]
            },
        )
        OFFICE_LOCATION_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "What's " + prof + " room number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What's " + prof + " room number",
                        "room number",
                        OFFICE_LOCATION_LABEL,
                    )
                ]
            },
        )
        OFFICE_LOCATION_TRAIN_DATA.append(my_tuple)

        CONTACT_INFO_LABEL = "CONTACT_INFO"
        CONTACT_INFO_TRAIN_DATA = []
        my_tuple = (
            "How can I reach " + prof + "",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can I reach " + prof + "", "reach", CONTACT_INFO_LABEL
                    )
                ]
            },
        )
        CONTACT_INFO_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Can I get the email address for " + prof + "?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I get the email address for " + prof + "?",
                        "email",
                        CONTACT_INFO_LABEL,
                    )
                ]
            },
        )
        CONTACT_INFO_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "What is " + prof + " phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is " + prof + " phone number",
                        "phone number",
                        CONTACT_INFO_LABEL,
                    )
                ]
            },
        )
        CONTACT_INFO_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "How can a get a hold of " + prof + "?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of " + prof + "?",
                        "hold of",
                        CONTACT_INFO_LABEL,
                    )
                ]
            },
        )
        CONTACT_INFO_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Can I have " + prof + " contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have " + prof + " contact info",
                        "contact info",
                        CONTACT_INFO_LABEL,
                    )
                ]
            },
        )
        CONTACT_INFO_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "I need to call " + prof + "",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call " + prof + "", "call", CONTACT_INFO_LABEL
                    )
                ]
            },
        )
        CONTACT_INFO_TRAIN_DATA.append(my_tuple)

        PROFESSOR_ACTIONS_LABEL = "PROFESSOR_ACTIONS"
        PROFESSOR_ACTIONS_TRAIN_DATA = []
        my_tuple = (
            "Can I reserve a room?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I reserve a room?", "reserve", PROFESSOR_ACTIONS_LABEL
                    )
                ]
            },
        )
        PROFESSOR_ACTIONS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Can I reserve room X?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I reserve room X?", "reserve", PROFESSOR_ACTIONS_LABEL,
                    )
                ]
            },
        )
        PROFESSOR_ACTIONS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "Can you reserve room X for me?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can you reserve room X for me?",
                        "reserve",
                        PROFESSOR_ACTIONS_LABEL,
                    )
                ]
            },
        )
        PROFESSOR_ACTIONS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "What do I do for a substitution?",
            {
                "entities": [
                    get_substring_label_truple(
                        "What do I do for a substitution?",
                        "substitution",
                        PROFESSOR_ACTIONS_LABEL,
                    )
                ]
            },
        )
        PROFESSOR_ACTIONS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "What do I do for a class substitution?",
            {
                "entities": [
                    get_substring_label_truple(
                        "What do I do for a class substitution?",
                        "class substitution",
                        PROFESSOR_ACTIONS_LABEL,
                    )
                ]
            },
        )
        PROFESSOR_ACTIONS_TRAIN_DATA.append(my_tuple)
        my_tuple = (
            "What do I do for a course substitution?",
            {
                "entities": [
                    get_substring_label_truple(
                        "What do I do for a course substitution?",
                        "course substitution",
                        PROFESSOR_ACTIONS_LABEL,
                    )
                ]
            },
        )

        PROFESSOR_ACTIONS_TRAIN_DATA.append(my_tuple)

    PROFESSOR_TRAIN_DATA = []
    PROFESSOR_TRAIN_DATA.extend(OFFICE_HOURS_TRAIN_DATA)
    PROFESSOR_TRAIN_DATA.extend(OFFICE_LOCATION_TRAIN_DATA)
    PROFESSOR_TRAIN_DATA.extend(CONTACT_INFO_TRAIN_DATA)
    PROFESSOR_TRAIN_DATA.extend(PROFESSOR_ACTIONS_TRAIN_DATA)

    PROFESSOR_LABELS = []
    PROFESSOR_LABELS.append(OFFICE_HOURS_LABEL)
    PROFESSOR_LABELS.append(OFFICE_LOCATION_LABEL)
    PROFESSOR_LABELS.append(CONTACT_INFO_LABEL)
    PROFESSOR_LABELS.append(PROFESSOR_ACTIONS_LABEL)

    return PROFESSOR_TRAIN_DATA, PROFESSOR_LABELS
