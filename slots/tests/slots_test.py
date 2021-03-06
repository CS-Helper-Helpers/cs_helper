import unittest
from slots.find_chunks import chunk_important_date, chunk_course, chunk_professor, chunk_professor_name


class TestSlots(unittest.TestCase):

    
    def test_chunk_important_date_faculty_report(self):
        utterance = "When does faculty report?"
        expected_result = ("FACULTY_REPORT", "faculty report")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    
    def test_chunk_important_date_curriculum_study(self):
        utterance = "When is curriculum study?"
        expected_result = ("CURRICULUM_STUDY", "curriculum study")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    def test_chunk_important_date_open_residence_halls(self):
        utterance = "When do the residence halls open?"
        expected_result = ("OPEN_RESIDENCE_HALLS", "residence halls")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    def test_chunk_important_date_add_date(self):
        utterance = "When is the last day to add a class?"
        expected_result = ("ADD_DATE", "add a class")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)


    def test_chunk_important_date_withdraw_date(self):
        utterance = "When is the last day to withdraw from a class?"
        expected_result = ("WITHDRAW_DATE", "day to withdraw from a class")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    def test_chunk_important_date_drop_date(self):
        utterance = "When is the last day to drop a class?"
        expected_result = ("DROP_DATE", "drop a class")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    def test_chunk_important_date_semester_start(self):
        utterance = "When does the semester start?"
        expected_result = ("SEMESTER_START", "semester start")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    def test_chunk_important_date_semester_end(self):
        utterance = "When does the semester end?"
        expected_result = ("SEMESTER_END", "semester end")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    def test_chunk_important_date_break(self):
        utterance = "When is the break?"
        expected_result = ("BREAK", "break")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)


    def test_chunk_important_date_finals(self):
        utterance = "When are finals?"
        expected_result = ("FINALS", "finals")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)
        

    def test_chunk_important_date_registration(self):
        utterance = "When is registration?"
        expected_result = ("REGISTRATION", "registration")
        doc = chunk_important_date(utterance, important_date_dir="../important_date/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    def test_chunk_course_number(self):
        utterance = "Is C S 474 offered this fall?"
        expected_result = ("COURSE", "C S 474")
        doc = chunk_course(utterance, course_dir="../course/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    def test_chunk_professor_office_hours(self):
        utterance = "When are Son Tran office hours?"
        expected_result = ("OFFICE_HOURS", "office hours")
        doc = chunk_professor(utterance, professor_dir="../professor/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)


    def test_chunk_professor_office_location(self):
        utterance = "Where can I find Son Tran?"
        expected_result = ("OFFICE_LOCATION", "Where")
        doc = chunk_professor(utterance, professor_dir="../professor/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)


    def test_chunk_professor_contact_info(self):
        utterance = "I need to call Huiping Cao"
        expected_result = ("CONTACT_INFO", "call")
        doc = chunk_professor(utterance, professor_dir="../professor/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)

    def test_chunk_professor_name(self):
        utterance = "I need to call Huiping Cao"
        expected_result = ("PROFESSOR_NAME", "Huiping Cao")
        doc = chunk_professor_name(utterance, professor_name_dir="../professor_name/")
        for ent in doc.ents:
            result = (ent.label_, ent.text)
        self.assertEqual(expected_result, result)



#if __name__ == '__main__':
#    unnittest.main()

