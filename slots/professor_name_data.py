def get_substring_label_truple(intent, label_indicator, label):
    start = intent.find(label_indicator)
    end = start + len(label_indicator)
    return (start, end, label)


def get_data():

    PROFESSOR_NAME_LABEL = "PROFESSOR_NAME"
    PROFESSOR_NAME_TRAIN_DATA = [
        (
            "When are Tran office hours?",
            {
                "entities": [
                    get_substring_label_truple(
                        "When are Tran office hours?", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Does Tran have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What are Tran office hours", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Is Tran available to meet",
            {
                "entities": [
                    get_substring_label_truple(
                        "Is Tran available to meet", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Does Tran have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What time is Tran office hours", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "can Tran meet with me today",
            {
                "entities": [
                    get_substring_label_truple(
                        "can Tran meet with me today", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What room is Tran in?",
            {
                "entities": [
                    get_substring_label_truple(
                        "What room is Tran in?", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Where is Tran office?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where is Tran office?", "Tran", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Does Tran have an office in this building",
            {
                "entities": [
                    get_substring_label_truple(
                        "Does Tran have an office in this building",
                        "Tran",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Where can I find Tran?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where can I find Tran?", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Do you know where Tran office is?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What's Tran room number", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can I reach Tran",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can I reach Tran", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I get the email address for Tran?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What is Tran phone number", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Tran?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Tran?", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have Tran contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have Tran contact info", "Tran", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call Tran",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call Tran", "Tran", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "When are Cooper office hours?",
            {
                "entities": [
                    get_substring_label_truple(
                        "When are Cooper office hours?", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Does Cooper have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What are Cooper office hours", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Is Cooper available to meet",
            {
                "entities": [
                    get_substring_label_truple(
                        "Is Cooper available to meet", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Does Cooper have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What time is Cooper office hours",
                        "Cooper",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "can Cooper meet with me today",
            {
                "entities": [
                    get_substring_label_truple(
                        "can Cooper meet with me today", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What room is Cooper in?",
            {
                "entities": [
                    get_substring_label_truple(
                        "What room is Cooper in?", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Where is Cooper office?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where is Cooper office?", "Cooper", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Does Cooper have an office in this building",
            {
                "entities": [
                    get_substring_label_truple(
                        "Does Cooper have an office in this building",
                        "Cooper",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Where can I find Cooper?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where can I find Cooper?", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Do you know where Cooper office is?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What's Cooper room number", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can I reach Cooper",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can I reach Cooper", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I get the email address for Cooper?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What is Cooper phone number", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Cooper?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Cooper?",
                        "Cooper",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Can I have Cooper contact info",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "I need to call Cooper", "Cooper", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "When are Pontelli office hours?",
            {
                "entities": [
                    get_substring_label_truple(
                        "When are Pontelli office hours?",
                        "Pontelli",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Does Pontelli have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What are Pontelli office hours",
                        "Pontelli",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Is Pontelli available to meet",
            {
                "entities": [
                    get_substring_label_truple(
                        "Is Pontelli available to meet",
                        "Pontelli",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Does Pontelli have any available office hours this week?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What time is Pontelli office hours",
                        "Pontelli",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "can Pontelli meet with me today",
            {
                "entities": [
                    get_substring_label_truple(
                        "can Pontelli meet with me today",
                        "Pontelli",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "What room is Pontelli in?",
            {
                "entities": [
                    get_substring_label_truple(
                        "What room is Pontelli in?", "Pontelli", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Where is Pontelli office?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where is Pontelli office?", "Pontelli", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Does Pontelli have an office in this building",
            {
                "entities": [
                    get_substring_label_truple(
                        "Does Pontelli have an office in this building",
                        "Pontelli",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Where can I find Pontelli?",
            {
                "entities": [
                    get_substring_label_truple(
                        "Where can I find Pontelli?", "Pontelli", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Do you know where Pontelli office is?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What's Pontelli room number", "Pontelli", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can I reach Pontelli",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can I reach Pontelli", "Pontelli", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I get the email address for Pontelli?",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "What is Pontelli phone number",
                        "Pontelli",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Pontelli?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Pontelli?",
                        "Pontelli",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Can I have Pontelli contact info",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "I need to call Pontelli", "Pontelli", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Cook phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Cook phone number", "Cook", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Cook?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Cook?", "Cook", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have Cook contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have Cook contact info", "Cook", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call Cook",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call Cook", "Cook", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Cao phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Cao phone number", "Cao", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Cao?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Cao?", "Cao", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have Cao contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have Cao contact info", "Cao", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call Cao",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call Cao", "Cao", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Hamilton phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Hamilton phone number",
                        "Hamilton",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Hamilton?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Hamilton?",
                        "Hamilton",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Can I have Hamilton contact info",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "I need to call Hamilton", "Hamilton", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Tuan phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Tuan phone number", "Tuan", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Tuan?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Tuan?", "Tuan", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have Tuan contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have Tuan contact info", "Tuan", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call Tuan",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call Tuan", "Tuan", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Misra phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Misra phone number", "Misra", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Misra?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Misra?", "Misra", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have Misra contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have Misra contact info", "Misra", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call Misra",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call Misra", "Misra", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Parth phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Parth phone number", "Parth", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Parth?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Parth?", "Parth", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have Parth contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have Parth contact info", "Parth", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call Parth",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call Parth", "Parth", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Pivkini phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Pivkini phone number", "Pivkini", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Pivkini?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Pivkini?",
                        "Pivkini",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Can I have Pivkini contact info",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "I need to call Pivkini", "Pivkini", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Song phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Song phone number", "Song", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Song?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Song?", "Song", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have Song contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have Song contact info", "Song", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call Song",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call Song", "Song", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Toups phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Toups phone number", "Toups", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Toups?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Toups?", "Toups", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have Toups contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have Toups contact info", "Toups", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call Toups",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call Toups", "Toups", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Wang phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Wang phone number", "Wang", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Wang?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Wang?", "Wang", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "Can I have Wang contact info",
            {
                "entities": [
                    get_substring_label_truple(
                        "Can I have Wang contact info", "Wang", PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "I need to call Wang",
            {
                "entities": [
                    get_substring_label_truple(
                        "I need to call Wang", "Wang", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "What is Steiner phone number",
            {
                "entities": [
                    get_substring_label_truple(
                        "What is Steiner phone number", "Steiner", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
        (
            "How can a get a hold of Steiner?",
            {
                "entities": [
                    get_substring_label_truple(
                        "How can a get a hold of Steiner?",
                        "Steiner",
                        PROFESSOR_NAME_LABEL,
                    )
                ]
            },
        ),
        (
            "Can I have Steiner contact info",
            {
                "entities": [
                    get_substring_label_truple(
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
                    get_substring_label_truple(
                        "I need to call Steiner", "Steiner", PROFESSOR_NAME_LABEL
                    )
                ]
            },
        ),
    ]

    return PROFESSOR_NAME_TRAIN_DATA, [PROFESSOR_NAME_LABEL]
