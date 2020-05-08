def get_substring_label_truple(intent, label_indicator, label):
    start = intent.find(label_indicator)
    end = start + len(label_indicator)
    return (start, end, label)


def get_data():
    CS_COURSES = [
        "110",
        "111",
        "117",
        "150",
        "151",
        "152",
        "153",
        "154",
        "155",
        "156",
        "157",
        "158",
        "159",
        "171G",
        "172",
        "209",
        "271",
        "272",
        "273",
        "278",
        "343",
        "370",
        "371",
        "372",
        "375",
        "409",
        "419",
        "448",
        "449",
        "450",
        "451",
        "452",
        "453",
        "454",
        "455",
        "456",
        "457",
        "458",
        "459",
        "460",
        "462",
        "463",
        "464",
        "465",
        "466",
        "468",
        "469",
        "471",
        "473",
        "474",
        "475",
        "476",
        "477",
        "478",
        "479",
        "480",
        "481",
        "482",
        "483",
        "484",
        "485",
        "486",
        "487",
        "488",
        "489",
        "491",
        "493",
        "494",
        "496",
        "502",
        "503",
        "504",
        "505",
        "506",
        "508",
        "509",
        "510",
        "513",
        "514",
        "515",
        "516",
        "517",
        "518",
        "519",
        "521",
        "522",
        "570",
        "571",
        "573",
        "574",
        "575",
        "579",
        "581",
        "582",
        "583",
        "584",
        "586",
        "587",
        "589",
        "598",
        "599",
        "600",
        "700",
        "Computer Literacy",
        "Computer Science Principles",
        "Introduction to Computer Animation",
        "C Programming",
        "C++ Programming",
        "Java Programming",
        "Python Programming I",
        "Python Programming II",
        "Internet Programming I",
        "Internet Programming II",
        "Topics in Software Programming and Applications",
        "R Programming I",
        "R Programming II",
        "Computer Science I Transition",
        "Object Oriented Programming Transition",
        "Introduction to Data Structures Transition",
        "Machine Programming and Organization Transition",
        "Discrete Math for Computer Science Transition",
        "Compilers and Automata Transition",
        "Software Development Transition",
        "Data Structure and Algorithms Transition",
        "Programming Language Structure I",
        "Architectural Concepts I",
        "Operating Systems I",
        "Computer Graphics I",
        "Digital Game Design",
        "Computer Security",
        "Special Topics",
        "Linux System Administration",
        "User Interface Design",
        "Introduction to Data Mining",
        "Algorithm Design and Implementation",
        "Database Management Systems I",
        "Introduction to Robotics",
        "Computer Networks I",
        "Artificial Intelligence I",
        "Computer Graphics I",
        "Bioinformatics Programming",
        "Automata, Languages, Computability",
        "Computer Security",
        "Introduction to Smart Grids",
        "Human-Centered Computing",
        "Bioinformatics",
        "Digital Game Design",
        "Visual Programming",
        "Applied Machine Learning I",
        "Parallel Programming",
        "Cloud and Edge Computing",
        "Analysis of Algorithms",
        "Programming Language Structure II",
        "Architectural Concepts II",
        "Operating Systems II",
        "Artificial Intelligence II",
        "Special Topics",
        "Advanced Software Engineering",
        "Database Management Systems II",
        "Advanced Cryptography",
        "Computer Networks II",
        "Algorithms in Systems Biology",
        "Advanced Human-Centered Computing",
        "Special Research Problems",
        "Master's Project",
        "Master's Thesis",
        "Pre-dissertation Research",
        "Doctoral Dissertation",
    ]

    COURSE_INFO_TRAIN_DATA = []
    COURSE_TIME_LABEL = "COURSE_TIME"
    COURSE_CRED_LABEL = "COURSE_CRED"
    COURSE_ROOM_LABEL = "COURSE_ROOM"
    COURSE_PROFESSOR_LABEL = "COURSE_PROFESSOR"

    for course in CS_COURSES:
        text = "What are the meeting times for " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "meeting times", COURSE_TIME_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","meeting times","' + COURSE_TIME_LABEL + '"),')

        text = "What days are " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "What days", COURSE_TIME_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","What days","' + COURSE_TIME_LABEL + '"),')

        text = "When is " + course + " class?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "When is", COURSE_TIME_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","When is","' + COURSE_TIME_LABEL + '"),')

        text = "How many credits is " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "credits", COURSE_CRED_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","credits","' + COURSE_CRED_LABEL + '"),')

        text = "Who is teaching " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "teaching", COURSE_PROFESSOR_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","teaching","' + COURSE_PROFESSOR_LABEL + '"),')

        text = "Who is the professor for " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(
                        text, "professor", COURSE_PROFESSOR_LABEL
                    )
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","professor","' + COURSE_PROFESSOR_LABEL + '"),')

        text = "What room is " + course + " in?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, "room", COURSE_ROOM_LABEL)]},
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","room","' + COURSE_ROOM_LABEL + '"),')

        text = "Where is " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "Where", COURSE_ROOM_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","Where","' + COURSE_ROOM_LABEL + '"),')

    COURSE_INFO_LABELS = []
    COURSE_INFO_LABELS.append(COURSE_CRED_LABEL)
    COURSE_INFO_LABELS.append(COURSE_PROFESSOR_LABEL)
    COURSE_INFO_LABELS.append(COURSE_ROOM_LABEL)
    COURSE_INFO_LABELS.append(COURSE_TIME_LABEL)

    return COURSE_INFO_TRAIN_DATA, COURSE_INFO_LABELS
