
FACULTY_REPORT_LABEL = "FACULTY_REPORT"
FACULTY_REPORT_TRAIN_DATA = [
    # faculty_report
    (
        "When is faculty report?",
        {"entities": [
            get_substring_label_truple(
                "When is faculty report",
                "faculty report",
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    
    (
        "When do I need to turn in the faculty report?",
        {"entities": [
            get_substring_label_truple(
                "When do I need to turn in the faculty report?", 
                "faculty report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "When is the faculty report due?", # START COUNTING HERE
        {"entities": [
            get_substring_label_truple(
                "When is the faculty report due?", 
                "faculty report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "Spring report is due when?",
        {"entities": [
            get_substring_label_truple(
                "Spring report is due when?", 
                "Spring report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "When do I need to turn in the spring report?",
        {"entities": [
            get_substring_label_truple(
                "When do I need to turn in the spring report?", 
                "spring report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "When is the spring report due?",
        {"entities": [
            get_substring_label_truple(
                "When is the spring report due?", 
                "spring report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "When is the spring report due?",
        {"entities": [
            get_substring_label_truple(
                "When is the spring report due?", 
                "spring report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "When do I need to have the fall report done by?",
        {"entities": [
            get_substring_label_truple(
                "When do I need to have the fall report done by?", 
                "fall report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "When is the fall report due?",
        {"entities": [
            get_substring_label_truple(
                "When is the fall report due?", 
                "fall report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "When is the annual report due?",
        {"entities": [
            get_substring_label_truple(
                "When is the annual report due?", 
                "annual report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "When is the research professor report due?",
        {"entities": [
            get_substring_label_truple(
                "When is the research professor report due?", 
                "research professor report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "When is the report due?",
        {"entities": [
            get_substring_label_truple(
                "When is the report due?", 
                "report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
    (
        "Am I supposed to turn a report in before the semester starts?",
        {"entities": [
            get_substring_label_truple(
                "Am I supposed to turn a report in before the semester starts?", 
                "report", 
                FACULTY_REPORT_LABEL
            )]
        },
    ),
] # End faculty report training data

CURRICULUM_STUDY_LABEL = "CURRICULUM_STUDY"

CURRICULUM_STUDY_TRAIN_DATA = [
    # faculty_report
    (
        "When is curriculum study?",
        {"entities": [
            get_substring_label_truple(
                "When is curriculum study",
                "curriculum study",
                CURRICULUM_STUDY_LABEL
            )]
        },
    ),
    
    (
        "When do I need to go to the curriculum study",
        {"entities": [
            get_substring_label_truple(
                "When do I need to go to the curriculum study", 
                "curriculum study",
                CURRICULUM_STUDY_LABEL
            )]
        },
    ),
    (
        "Is there a curriculum study?", # START COUNTING HERE
        {"entities": [
            get_substring_label_truple(
                "Is there a curriculum study?", 
                "curriculum study",
                CURRICULUM_STUDY_LABEL
            )]
        },
    ),
    # Ask about how other people would ask this question
] # End curriculum report training data


OPEN_RESIDENCE_HALLS_LABEL = "OPEN_RESIDENCE_HALLS"
OPEN_RESIDENCE_HALLS_TRAIN_DATA = [
    (
        "When do residence halls open up?",
        {"entities": [
            get_substring_label_truple(
                "When do residence halls open up?",
                "residence halls",
                OPEN_RESIDENCE_HALLS_LABEL
            )]
        },
    ),
    
    (
        "When can I move in?",
        {"entities": [
            get_substring_label_truple(
                "When can I move in?", 
                "move in", 
                OPEN_RESIDENCE_HALLS_LABEL
            )]
        },
    ),
    (
        "When do the dorms open up?",
        {"entities": [
            get_substring_label_truple(
                "When do the dorms open up?", 
                "dorms open", 
                OPEN_RESIDENCE_HALLS_LABEL
            )]
        },
    ),
    (
        "Are the dorms open yet?",
        {"entities": [
            get_substring_label_truple(
                "Are the dorms open yet?", 
                "dorms open", 
                OPEN_RESIDENCE_HALLS_LABEL
            )]
        },
    ),
    (
        "Am I allowed to move in yet?",
        {"entities": [
            get_substring_label_truple(
                "Am I allowed to move in yet?", 
                "move in", 
                OPEN_RESIDENCE_HALLS_LABEL
            )]
        },
    ),

] # End open residence halls training data

HOLIDAYS_LABEL = "HOLIDAYS"
HOLIDAYS_TRAIN_DATA = [
    # New Year's Day
    (
        "When is New Year's Day?",
        {"entities": [
            get_substring_label_truple(
                "When is New Year's Day?",
                "New Year's Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "When is New Years?",
        {"entities": [
            get_substring_label_truple(
                "When is New Years?",
                "New Years",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for New Years Day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for New Years Day?",
                "New Years Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for New Years?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for New Years?",
                "New Years",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for New Year's Day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for New Year's Day?",
                "New Year's Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for New Years?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for New Years?",
                "New Years",
                HOLIDAYS_LABEL
            )]
        },
    ),

    # MLK Day
    (
        "When is Martin Luther King day?",
        {"entities": [
            get_substring_label_truple(
                "When is Martin Luther King day??",
                "Martin Luther King",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "When is MLK day?",
        {"entities": [
            get_substring_label_truple(
                "When is MLK day?",
                "MLK",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "When is Martin Luther King Junior day?",
        {"entities": [
            get_substring_label_truple(
                "When is Martin Luther King Jr day?",
                "Martin Luther King Junior",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Martin Luther King's day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Martin Luther King's day?",
                "Martin Luther King",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for MLK?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for MLK?",
                "MLK",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for MLK day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for MLK day?",
                "MLK",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for MLK junior day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for MLK junior day?",
                "MLK",
                HOLIDAYS_LABEL
            )]
        },
    ),

    # Presidents Day
    (
        "When is Presidents Day?",
        {"entities": [
            get_substring_label_truple(
                "When is Presidents Day?",
                "Presidents Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Presidents Day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Presidents Day?",
                "Presidents Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for Presidents Day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for Presidents Day?",
                "Presidents Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    
    # Memorial Day
    (
        "When is Memorial Day?",
        {"entities": [
            get_substring_label_truple(
                "When is Memorial Day?",
                "Memorial Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Memorial Day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Memorial Day?",
                "Memorial Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for Memorial Day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for Memorial Day?",
                "Memorial Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    
    # Independence Day, Fourth of July, 4th of July,
    (
        "When is Independence Day?",
        {"entities": [
            get_substring_label_truple(
                "When is Independence Day?",
                "Independence Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "When is Fourth of July",
        {"entities": [
            get_substring_label_truple(
                "When is Fourth of July",
                "Fourth of July",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "When is the 4th of July?",
        {"entities": [
            get_substring_label_truple(
                "When is the 4th of July?",
                "4th of July",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Independence Day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Independence Day?",
                "Independence Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Fourth of July?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Fourth of July?",
                "Fourth of July",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for the 4th of July?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for the 4th of July?",
                "4th of July",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for Independence Day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for Independence Day?",
                "Independence Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for Fourth of July?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for Fourth of July?",
                "Fourth of July",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for the 4th of July?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed the 4th of July?",
                "4th of July",
                HOLIDAYS_LABEL
            )]
        },
    ),

    # Labor Day
    (
        "When is Labor Day?",
        {"entities": [
            get_substring_label_truple(
                "When is Labor Dayy?",
                "Labor Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Labor Day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Labor Day?",
                "Labor Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for Labor Day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for Labor Day?",
                "Labor Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    
    # Columbus Day
    (
        "When is Columbus Day?",
        {"entities": [
            get_substring_label_truple(
                "When is Columbus Dayy?",
                "Columbus Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Columbus Day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Columbus Day?",
                "Columbus Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for Columbus Day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for Columbus Day?",
                "Columbus Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    
    # Veterans Day
    (
        "When is Veterans Day?",
        {"entities": [
            get_substring_label_truple(
                "When is Veterans Dayy?",
                "Veterans Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Veterans Day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Veterans Day?",
                "Veterans Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for Veterans Day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for Veterans Day?",
                "Veterans Day",
                HOLIDAYS_LABEL
            )]
        },
    ),

    # Thanksgiving Day
    (
        "When is Thanksgiving Day?",
        {"entities": [
            get_substring_label_truple(
                "When is Thanksgiving Dayy?",
                "Thanksgiving Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Thanksgiving Day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Thanksgiving Day?",
                "Thanksgiving Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for Thanksgiving Day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for Thanksgiving Day?",
                "Thanksgiving Day",
                HOLIDAYS_LABEL
            )]
        },
    ),

    # Christmas Day
    (
        "When is Christmas Day?",
        {"entities": [
            get_substring_label_truple(
                "When is Christmas Dayy?",
                "Christmas Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Are you open for Christmas Day?",
        {"entities": [
            get_substring_label_truple(
                "Are you open for Christmas Day?",
                "Christmas Day",
                HOLIDAYS_LABEL
            )]
        },
    ),
    (
        "Is the university closed for Christmas Day?",
        {"entities": [
            get_substring_label_truple(
                "Is the university closed for Christmas Day?",
                "Christmas Day",
                HOLIDAYS_LABEL
            )]
        },
    ),    

] # End holidays training data


INSTRUCTION_BEGINS_LABEL = "INSTRUCTION_BEGINS"

INSTRUCTION_BEGINS_TRAIN_DATA = [
    # instruction begins
    (
        "When does instruction begin?",
        {"entities": [
            get_substring_label_truple(
                "When does instruction begin?",
                "instruction begin",
                INSTRUCTION_BEGINS_LABEL
            )]
        },
    ),
    (
        "Has instruction began?",
        {"entities": [
            get_substring_label_truple(
                "Has instruction began?",
                "instruction began",
                INSTRUCTION_BEGINS_LABEL
            )]
        },
    ),
    
    (
        "When does school start?",
        {"entities": [
            get_substring_label_truple(
                "When does school start?", 
                "school start",
                INSTRUCTION_BEGINS_LABEL
            )]
        },
    ),
    (
        "Has school started yet?",
        {"entities": [
            get_substring_label_truple(
                "Has school started yet?", 
                "school start",
                INSTRUCTION_BEGINS_LABEL
            )]
        },
    ),
    (
        "When do classes begin?",
        {"entities": [
            get_substring_label_truple(
                "When does classes begin?",
                "classes begin",
                INSTRUCTION_BEGINS_LABEL
            )]
        },
    ),

    (
        "Have classes started yet?",
        {"entities": [
            get_substring_label_truple(
                "Has school started yet?", 
                "school start",
                INSTRUCTION_BEGINS_LABEL
            )]
        },
    ),
    # Ask about how other people would ask this question
] # End curriculum report training data


ADD_DATE_LABEL = 'ADD_DATE'
ADD_DATE_TRAIN_DATA = [
    (
        "When is the last day to add a class?",
        {"entities": [
            get_substring_label_truple(
                "When is the last day to add a class?", 
                "add a class",
                ADD_DATE_LABEL
            )]
        },
    ),
    (
        "Can I still add a course?",
        {"entities": [
            get_substring_label_truple(
                "Can I still add a course?", 
                "add a course",
                ADD_DATE_LABEL
            )]
        },
    ),
    (
        "Is it too late to add a course for this semester?",
        {"entities": [
            get_substring_label_truple(
                "Is it too late to add a course for this semester?", 
                "add a course",
                ADD_DATE_LABEL
            )]
        },
    ),
    (
        "I was wondering if I could still add a class?",
        {"entities": [
            get_substring_label_truple(
                "I was wondering if I could still add a class?", 
                "add a class",
                ADD_DATE_LABEL
            )]
        },
    ),
    (
        "Are we past the add date?",
        {"entities": [
            get_substring_label_truple(
                "Are we past the add date?", 
                "add date",
                ADD_DATE_LABEL
            )]
        },
    ),
    (
        "When is the final add date?",
        {"entities": [
            get_substring_label_truple(
                "When is the final add date?", 
                "add date",
                ADD_DATE_LABEL
            )]
        },
    ),
    
]


WITHDRAW_DATE_LABEL = 'WITHDRAW_DATE'
WITHDRAW_DATE_TRAIN_DATA = [
    (
        "When is the last day to withdraw from a class?",
        {"entities": [
            get_substring_label_truple(
                "When is the last day to withdraw from a class?", 
                "withdraw from a class",
                WITHDRAW_DATE_LABEL
            )]
        },
    ),
    (
        "Can I still withdraw from a course?",
        {"entities": [
            get_substring_label_truple(
                "Can I still withdraw from a course?", 
                "withdraw from a course",
                WITHDRAW_DATE_LABEL
            )]
        },
    ),
    (
        "Is it too late to withdraw from a course for this semester?",
        {"entities": [
            get_substring_label_truple(
                "Is it too late to withdraw from a course for this semester?", 
                "withdraw from a course",
                WITHDRAW_DATE_LABEL
            )]
        },
    ),
    (
        "I was wondering if I could still withdraw from a class?",
        {"entities": [
            get_substring_label_truple(
                "I was wondering if I could still withdraw from a class?", 
                "withdraw from a class",
                WITHDRAW_DATE_LABEL
            )]
        },
    ),
    (
        "Are we past the withdraw date?",
        {"entities": [
            get_substring_label_truple(
                "Are we past the withdraw date?", 
                "withdraw date",
                WITHDRAW_DATE_LABEL
            )]
        },
    ),
    (
        "When is the last day to withdraw?",
        {"entities": [
            get_substring_label_truple(
                "When is the last day to withdraw?", 
                "day to withdraw",
                WITHDRAW_DATE_LABEL
            )]
        },
    ),
    
]

DROP_DATE_LABEL = 'DROP_DATE'
DROP_DATE_TRAIN_DATA = [
    (
        "When is the last day to drop a class?",
        {"entities": [
            get_substring_label_truple(
                "When is the last day to drop a class?", 
                "drop a class",
                DROP_DATE_LABEL
            )]
        },
    ),
    (
        "Can I still drop a course?",
        {"entities": [
            get_substring_label_truple(
                "Can I still drop a course?", 
                "drop a course",
                DROP_DATE_LABEL
            )]
        },
    ),
    (
        "Is it too late to drop a course for this semester?",
        {"entities": [
            get_substring_label_truple(
                "Is it too late to drop a course for this semester?", 
                "drop a course",
                DROP_DATE_LABEL
            )]
        },
    ),
    (
        "I was wondering if I could still drop a class?",
        {"entities": [
            get_substring_label_truple(
                "I was wondering if I could still drop a class?", 
                "drop a class",
                DROP_DATE_LABEL
            )]
        },
    ),
    (
        "Are we past the drop date?",
        {"entities": [
            get_substring_label_truple(
                "Are we past the drop date?", 
                "drop date",
                DROP_DATE_LABEL
            )]
        },
    ),
    (
        "When is the last day to drop?",
        {"entities": [
            get_substring_label_truple(
                "When is the last day to drop?", 
                "day to drop",
                DROP_DATE_LABEL
            )]
        },
    ),
    (
        "Can I still drop my classes?",
        {"entities": [
            get_substring_label_truple(
                "Can I still drop my classes?", 
                "drop",
                DROP_DATE_LABEL
            )]
        },
    ),
    (
        "Can I still drop my classes?",
        {"entities": [
            get_substring_label_truple(
                "Can I still drop my classes?", 
                "drop",
                DROP_DATE_LABEL
            )]
        },
    ),
    
]

SEMESTER_START_LABEL = 'SEMESTER_START'
SEMESTER_START_TRAIN_DATA = [
    (
        "When does the semester start?",
        {"entities": [
            get_substring_label_truple(
                "When does the semester start?", 
                "semester start",
                SEMESTER_START_LABEL
            )]
        },
    ),
    (
        "When is the start of the semester?",
        {"entities": [
            get_substring_label_truple(
                "When is the start of the semester?", 
                "start of the semester",
                SEMESTER_START_LABEL
            )]
        },
    ),
    (
        "What day does the semester start?",
        {"entities": [
            get_substring_label_truple(
                "What day does the semester start?", 
                "semester start",
                SEMESTER_START_LABEL
            )]
        },
    ),
    (
        "What day is the start of the semester?",
        {"entities": [
            get_substring_label_truple(
                "What day is the start of the semester?", 
                "start of the semester",
                SEMESTER_START_LABEL
            )]
        },
    ),
    (
        "Which day does the semester start?",
        {"entities": [
            get_substring_label_truple(
                "Which day does the semester start?", 
                "semester start",
                SEMESTER_START_LABEL
            )]
        },
    ),
    (
        "Which day is the start of the semester?",
        {"entities": [
            get_substring_label_truple(
                "Which day is the start of the semester?", 
                "start of the semester",
                SEMESTER_START_LABEL
            )]
        },
    ),
]


SEMESTER_END_LABEL = 'SEMESTER_END'
SEMESTER_END_TRAIN_DATA = [
    (
        "When does the semester end?",
        {"entities": [
            get_substring_label_truple(
                "When does the semester end?", 
                "semester end",
                SEMESTER_END_LABEL
            )]
        },
    ),
    (
        "When is the end of the semester?",
        {"entities": [
            get_substring_label_truple(
                "When is the end of the semester?", 
                "end of the semester",
                SEMESTER_END_LABEL
            )]
        },
    ),
    (
        "What day does the semester end?",
        {"entities": [
            get_substring_label_truple(
                "What day does the semester end?", 
                "semester end",
                SEMESTER_END_LABEL
            )]
        },
    ),
    (
        "What day is the end of the semester?",
        {"entities": [
            get_substring_label_truple(
                "What day is the end of the semester?", 
                "end of the semester",
                SEMESTER_END_LABEL
            )]
        },
    ),
    (
        "Which day does the semester end?",
        {"entities": [
            get_substring_label_truple(
                "Which day does the semester end?", 
                "semester end",
                SEMESTER_END_LABEL
            )]
        },
    ),
    (
        "Which day is the end of the semester?",
        {"entities": [
            get_substring_label_truple(
                "Which day is the end of the semester?", 
                "end of the semester",
                SEMESTER_END_LABEL
            )]
        },
    ),
]


BREAK_LABEL = 'BREAK'
BREAK_TRAIN_DATA = [
    (
        "When is the break?",
        {"entities": [
            get_substring_label_truple(
                "When is the break?", 
                "break",
                BREAK_LABEL
            )]
        },
    ),
    (
        "When is spring break?",
        {"entities": [
            get_substring_label_truple(
                "When is spring break?", 
                "break",
                BREAK_LABEL
            )]
        },
    ),
    (
        "When is fall break?",
        {"entities": [
            get_substring_label_truple(
                "When is fall break?", 
                "break",
                BREAK_LABEL
            )]
        },
    ),
]


FINALS_LABEL = 'FINALS'
FINALS_TRAIN_DATA = [
    (
        "When are finals?",
        {"entities": [
            get_substring_label_truple(
                "When are finals?", 
                "finals",
                FINALS_LABEL
            )]
        },
    ),
    (
        "When do finals start?",
        {"entities": [
            get_substring_label_truple(
                "When do finals start?", 
                "finals",
                FINALS_LABEL
            )]
        },
    ),
]

REGISTRATION_LABEL = 'REGISTRATION'
REGISTRATION_TRAIN_DATA = [
    (
        "When can I begin to register for classes?",
        {"entities": [
            get_substring_label_truple(
                "When can I begin to register for classes?", 
                "register",
                REGISTRATION_LABEL
            )]
        },
    ),
    (
        "When does registration start?",
        {"entities": [
            get_substring_label_truple(
                "When does registration start?", 
                "registration",
                REGISTRATION_LABEL
            )]
        },
    ),
]




