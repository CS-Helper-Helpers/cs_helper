import csv
import time
import mysql.connector as sqlcon

def insert_training_questions(file_name='important_dates.csv'):
    vals=[]
    with open(file_name) as input_file:
        reader = csv.reader(input_file, delimiter=',')
    
        for row in reader:
            vals.append(tuple(row))
        
        start = time.time()

        for row in vals:
            sql = "INSERT INTO TrainingQuestions (question, cat, slot, label) VALUES (%s, %s, %s, %s)"
            
            try:
                cursor.execute(sql, row)
            except sqlcon.Error as e:
                return e.msg
                
        db.commit()
                
        end = time.time()
        print(end - start, 'seconds for single insert training questions')
        s=str(end - start) + 'seconds'
        return s

insert_training_questions()
                