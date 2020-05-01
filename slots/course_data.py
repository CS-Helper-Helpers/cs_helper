def get_substring_label_truple(intent, label_indicator, label):
    start = intent.find(label_indicator)
    end = start + len(label_indicator)
    return (start, end, label)


def get_data():
    CS_COURSES = [
        "CS 110",
        "CS 111",
        "CS 117",
        "CS 150",
        "CS 151",
        "CS 153",
        "CS 154",
        "CS 155",
        "CS 156",
        "CS 157",
        "CS 158",
        "CS 159",
        "CS 171",
        "CS 172",
        "CS 209",
        "CS 271",
        "CS 271",
        "CS 271",
        "CS 273",
        "CS 278",
        "CS 343",
        "CS 370",
        "CS 371",
        "CS 372",
        "CS 375",
        "CS 409",
        "CS 419",
        "CS 448",
        "CS 449",
        "CS 450",
        "CS 451",
        "CS 452",
        "CS 453",
        "CS 454",
        "CS 455",
        "CS 456",
        "CS 457",
        "CS 458",
        "CS 459",
        "CS 460",
        "CS 462",
        "CS 463",
        "CS 464",
        "CS 465",
        "CS 466",
        "CS 468",
        "CS 469",
        "CS 471",
        "CS 473",
        "CS 474",
        "CS 475",
        "CS 476",
        "CS 477",
        "CS 478",
        "CS 479",
        "CS 480",
        "CS 481",
        "CS 482",
        "CS 483",
        "CS 484",
        "CS 485",
        "CS 486",
        "CS 487",
        "CS 488",
        "CS 489",
        "CS 491",
        "CS 493",
        "CS 494",
        "CS 496",
        "CS 502",
        "CS 503",
        "CS 504",
        "CS 505",
        "CS 506",
        "CS 508",
        "CS 509",
        "CS 510",
        "CS 514",
        "CS 515",
    ]

    COURSE_TRAIN_DATA = []
    COURSE_LABEL = "COURSE"

    for course in CS_COURSES:
        text = "What time is " + course + "?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)

        text = "When is " + course + "?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)

        text = "Is " + course + " offered in the fall?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)

        text = "Who is teaching " + course + "?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)

        text = "Do I need to take " + course + "?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)

        text = "IS " + course + " required to graduate?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)

    return COURSE_TRAIN_DATA, [COURSE_LABEL]
