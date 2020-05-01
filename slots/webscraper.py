import requests
from bs4 import BeautifulSoup
import pprint

# COURSE CATALOG
# URL = "https://catalogs.nmsu.edu/nmsu/arts-sciences/computer-science/#coursestext"

# PROFESSOR PAGE
URL = "https://www.cs.nmsu.edu/wp/people/faculty/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Courses Results
# results = soup.find(class_="sc_sccoursedescs")

# Professor Results
results = soup.find(class_="entry-content")


# print(results.prettify())

# Courses
# job_elems = results.find_all("p", class_="courseblocktitle noindent")
# for job_elem in job_elems:
#     course_elem = job_elem.find("strong")
#     course_info = str(course_elem.text)
#     course_info = course_info.split(".")
#     course_num = course_info[0]
#     course_title = course_info[1]
#     print(course_num)
#     print(course_title)

# PROF NAMES
job_elems = results.find_all("div", class_="awsm-detailed-info")
contacts_array = []
for job_elem in job_elems:
    contact = []
    prof_name = job_elem.find("h2").text
    contact_info = job_elem.find("div", class_="awsm-contact-details")
    contact_info = contact_info.find_all("p")
    for info in contact_info:
        contact.append(info.text)
    entry = {prof_name: contact}
    contacts_array.append(entry)
# pprint.pprint(contacts_array)

prof_dict = []
for c in contacts_array:
    res = [[i for i in c[x]] for x in c.keys()]
    res = res[0]
    name = list(c.keys())[0]
    email = "not listed"
    phone = "not listed"
    office = "not listed"
    prof_entry = {name: [{"Email": email}, {"Phone": phone}, {"Office": office}]}
    for r in res:
        substring_list = ["Email:", "Office:", "Phone:"]
        if any(substring in r for substring in substring_list):
            if "Email:" in r:
                email = r[6:]
                prof_entry[name][0]["Email"] = email

                # print(prof_entry[name][0]["Email"])
            elif "Phone:" in r:
                phone = r[6:]
                prof_entry[name][1]["Phone"] = phone
            elif "Office:" in r:
                office = r[7:]
                prof_entry[name][2]["Office"] = office
    prof_dict.append(prof_entry)
pprint.pprint(prof_dict)
