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

    COURSE_TRAIN_DATA = []
    COURSE_LABEL = "COURSE"

    for course in CS_COURSES:
        text = "What time is " + course + "?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","' + course + '","' + COURSE_LABEL + '"),')

        text = "When is " + course + "?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","' + course + '","' + COURSE_LABEL + '"),')

        text = "Is " + course + " offered in the fall?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","' + course + '","' + COURSE_LABEL + '"),')

        text = "Who is teaching " + course + "?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","' + course + '","' + COURSE_LABEL + '"),')

        text = "Do I need to take " + course + "?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","' + course + '","' + COURSE_LABEL + '"),')

        text = "IS " + course + " required to graduate?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, course, COURSE_LABEL)]},
        )
        COURSE_TRAIN_DATA.append(my_tuple)
        # print('("' + text + '","course","' + course + '","' + COURSE_LABEL + '"),')

    return COURSE_TRAIN_DATA, [COURSE_LABEL]
