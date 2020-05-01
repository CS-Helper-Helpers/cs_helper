def get_substring_label_truple(intent, label_indicator, label):
    start = intent.find(label_indicator)
    end = start + len(label_indicator)
    return (start, end, label)


def get_data():

    OFFICE_HOURS_LABEL = "OFFICE_HOURS"
    OFFICE_HOURS_TRAIN_DATA = [
        (
            "When are <X> office hours?",
            {
                "entities": [
                    get_substring_label_truple(
                        "When are <X> office hours?", "office hours", OFFICE_HOURS_LABEL
                    )
                ]
            },
        ),
        (
            "Does <X> have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Does <X> have any available office hours this week?",
                        "office hours",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        ),
        (
            "What are <X> office hours",
            {
                "entities": [
                    get_substring_label_truple(
                        "What are <X> office hours", "office hours", OFFICE_HOURS_LABEL
                    )
                ]
            },
        ),
        (
            "Is <X> available to meet",
            {
                "entities": [
                    get_substring_label_truple(
                        "Is <X> available to meet", "available", OFFICE_HOURS_LABEL
                    )
                ]
            },
        ),
        (
            "Does <X> have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Does <X> have any available office hours this week?",
                        "office hours",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        ),
        (
            "What time is <X> office hours",
            {
                "entities": [
                    get_substring_label_truple(
                        "What time is <X> office hours",
                        "office hours",
                        OFFICE_HOURS_LABEL,
                    )
                ]
            },
        ),
        (
            "can <x> meet with me today",
            {
                "entities": [
                    get_substring_label_truple(
                        "can <x> meet with me today", "meet", OFFICE_HOURS_LABEL
                    )
                ]
            },
        ),
    ]

    OFFICE_LOCATION_LABEL = "OFFICE_LOCATION"
    OFFICE_LOCATION_TRAIN_DATA = [
        (
            "What room is <X> in?",
            {
                "entities": [
                    get_substring_label_truple(
                        "What room is <X> in?", "what room", OFFICE_LOCATION_LABEL
                    )
                ]
            },
        ),
        (
            "Where is <X> office?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where is <X> office?", "office", OFFICE_LOCATION_LABEL,
                    )
                ]
            },
        ),
        (
            "Does <X> have an office in this building",
            {
                "entities": [
                    get_substring_label_truple(
                        "Does <X> have an office in this building",
                        "office",
                        OFFICE_LOCATION_LABEL,
                    )
                ]
            },
        ),
        (
            "Where can I find <X>?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where can I find <X>?", "Where", OFFICE_LOCATION_LABEL
                    )
                ]
            },
        ),
        (
            "Do you know where <X> office is?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Do you know where <X> office is?",
                        "office",
                        OFFICE_LOCATION_LABEL,
                    )
                ]
            },
        ),
        (
            "What's <X> room number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What's <X> room number", "room number", OFFICE_LOCATION_LABEL
                    )
                ]
            },
        ),
    ]

    CONTACT_INFO_LABEL = "CONTACT_INFO"
    CONTACT_INFO_TRAIN_DATA = [
        (
            "How can I reach <x>",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can I reach <x>", "reach", CONTACT_INFO_LABEL
                    )
                ]
            },
        ),
        (
            "Can I get the email address for <X>?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I get the email address for <X>?",
                        "email",
                        CONTACT_INFO_LABEL,
                    )
                ]
            },
        ),
        (
            "What is <X> phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is <X> phone number", "phone number", CONTACT_INFO_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of <X>?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of <X>?", "hold of", CONTACT_INFO_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have <X> contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have <X> contact info",
                        "contact info",
                        CONTACT_INFO_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call <X>",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call <X>", "call", CONTACT_INFO_LABEL
                    )
                ]
            },
        ),
    ]

    PROFESSOR_ACTIONS_LABEL = "PROFESSOR_ACTIONS"
    PROFESSOR_ACTIONS_TRAIN_DATA = [
        (
            "Can I reserve a room?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I reserve a room?", "reserve", PROFESSOR_ACTIONS_LABEL
                    )
                ]
            },
        ),
        (
            "Can I reserve room X?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I reserve room X?", "reserve", PROFESSOR_ACTIONS_LABEL,
                    )
                ]
            },
        ),
        (
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
        ),
        (
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
        ),
        (
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
        ),
        (
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
        ),
    ]

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
