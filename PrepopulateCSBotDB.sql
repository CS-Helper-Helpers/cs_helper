insert into Categories (primarycategory, secondarycategory) values ("faq", "important_date"), ("class", "location"), ("class", "professor"), 
("faq", "class"), ("class", "time"), ("department", "time"), ("faq", "department"), ("faq", "professor"), ("faq", "student"), ("faq", "employee");
set @fid = (select categoryid from Categories where primarycategory = "faq" and secondarycategory = "important_date");
set @cl = (select categoryid from Categories where primarycategory = "class" and secondarycategory = "location");
set @cp = (select categoryid from Categories where primarycategory = "class" and secondarycategory = "professor");
set @fc = (select categoryid from Categories where primarycategory = "faq" and secondarycategory = "class");
set @ct = (select categoryid from Categories where primarycategory = "class" and secondarycategory = "time");
set @dt = (select categoryid from Categories where primarycategory = "department" and secondarycategory = "time");
set @fd = (select categoryid from Categories where primarycategory = "faq" and secondarycategory = "department");
set @fp = (select categoryid from Categories where primarycategory = "faq" and secondarycategory = "professor");
set @fs = (select categoryid from Categories where primarycategory = "faq" and secondarycategory = "student");
set @fe = (select categoryid from Categories where primarycategory = "faq" and secondarycategory = "employee");
insert into TrainingQuestions (question, category) values ("When do classes start?", @fid), ("When does the semester start?", @fid), 
("What day does the semester start?", @fid), ("Which day does the semester start?", @fid), ("What date does the semester start on?", @fid), 
("When does school start?", @fid), ("What day does school start?", @fid), ("What is the first day of class?", @fid), ("What day do classes start?", @fid), 
("What day do classes end?", @fid), ("When do classes end?", @fid), ("When does the semester end?", @fid), ("When is the last day of classes?", @fid), 
("What day does the semester end on?", @fid), ("When is spring break?", @fid), ("When is finals week?", @fid), ("When are finals?", @fid), 
("What day do finals start?", @fid), ("When is the first day of finals week?", @fid), ("When is Thanksgiving break?", @fid), ("When is Fall break?", @fid), 
("When is the upcoming holiday?", @fid), ("When does registration open?", @fid), ("When can I register for classes?", @fid), 
("When is the last day to register for a class?", @fid), ("When is the last day to add a class?", @fid), ("With/without permission", @fid), 
("When is the last day to drop a class?", @fid), ("When is graduation?", @fid), ("What day is graduation?", @fid), 
("How many holidays/days off are there?", @fid), ("Do we have any breaks this semester?", @fid), ("Which days off do we have?", @fid), ("Where is X?", @cl), 
("Follow-up questions to figure out what they’re really asking", @cl), ("What room is class X in?", @cl), ("Location and time", @cl), 
("Where is my classroom located?", @cl), ("Where is X located?", @cl), ("Where is my office located?", @cl), ("How do I get to X building?", @cl), 
("Where is X building?", @cl), ("Where is professor X’s office?", @cl), ("Where is Dr. X’s office?", @cl), ("Where is room X?", @cl), ("Where is room X located?", @cl), 
("How do I get to office X?", @cl), ("How do I get to X floor?", @cl), ("Where is the Psychology department?", @cl), ("Where is the Sociology department?", @cl), 
("Where can I find the elevator?", @cl), ("Where is the elevator?", @cl), ("Where can I find the restroom?", @cl), ("Men/Women", @cl), ("Where is the restroom?", @cl), 
("Where is the X’s restroom?", @cl), ("Where is the lost and found?", @cl), ("Where is the YWIC office?", @cl), ("Where is my professor teaching?", @cl), 
("Where is the tutoring center for X?", @cl), ("Where is the tutoring center?", @cl), ("Where is the X tutoring center?", @cl), ("What are professor X’s office hours?", @cp), 
("What is professor X’s email?", @cp), ("Does X have any TA’s?", @cp), ("Is X involved with any research?", @cp), ("What type of research does X do?", @cp), 
("I want to drop a class but I don’t know how", @fc), ("How do I drop a class?", @fc), ("I want to audit a class but I don’t know how", @fc), ("How do I audit a class?", @fc), 
("I want to change my class to be an SU/Audit", @fc), ("When does class X start?", @ct), ("When does X start?", @ct), ("What time does my professor’s class end?", @ct), 
("What time does the office close?", @dt), ("When does the office close?", @dt), ("What are the office hours?", @dt), ("How late is the department open until?", @dt), 
("When does the department close?", @dt), ("Do you have a lost and found?", @fd), ("Is there a lost and found?", @fd), ("Can I speak with an advisor?", @fd), 
("Can I speak with X?", @fd), ("Can I speak to Dr. Tran?", @fd), ("Is Dr. Tran available?", @fd), ("Could I talk to the department head?", @fd), 
("Can I speak with the department head?", @fd), ("Who is in charge?", @fd), ("When are Dr. Tran’s office hours?", @fd), ("Can you reserve a room for me?", @fp), 
("Can I reserve a room?", @fp), ("Can I reserve room X?", @fp), ("Can you reserve room X for me?", @fp), ("Can I reserve X?", @fp), 
("What do I do for a substitution?", @fp), ("What do I do for a class substitution?", @fp), ("Can I get a change of schedule form?", @fs), 
("How do I apply to the graduate program?", @fs), ("What classes are offered next semester?", @fd), ("Where can I receive assistance for coding?", @fs), 
("Where can I get help for coding?", @fs), ("Where can I find my degree plan?", @fs), ("Where can I get my degree plan?", @fs), ("Where do I find my degree plan?", @fs), 
("Where do I get my degree plan?", @fs), ("How do I apply for my degree?", @fs), ("Is the candy free?", @fd), ("Can I have some candy?", @fd), 
("Can I take some candy?", @fs), ("Where is the candy?", @fs), ("Who do I go to talk to about the amount of money on my paycheck being decreased?", @fe), 
("When will I receive my paycheck?", @fe), ("When will I get my paycheck?", @fe), ("Where do I go to receive my paycheck?", @fe), ("Where do I go to get my paycheck?", @fe), 
("Can you process an override for a change of major?", @fs), ("Can a department head override a request for a change of schedule?", @fs), ("What do I do if I can’t attend the meeting?", @fp);