import requests
from bs4 import BeautifulSoup

# COURSE CATALOG
# URL = "https://catalogs.nmsu.edu/nmsu/arts-sciences/computer-science/#coursestext"

# PROFESSOR PAGE
URL = "https://www.cs.nmsu.edu/wp/people/faculty/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="awsm-team-5096")
# print(results.prettify())

# COURSES
# job_elems = results.find_all("p", class_="courseblocktitle noindent")
# for job_elem in job_elems:
#     course_elem = job_elem.find("strong")
#     course_info = str(course_elem.text)
#     course_info = course_info.split(".")
#     course_num = course_info[0]
#     course_title = course_info[1]
#     # print(course_num)
#     print(course_title)

# PROF NAMES
job_elems = results.find_all("div", class_="awsm-personal-info")
for job_elem in job_elems:
    prof_names = job_elem.find("h3")
    print(prof_names.text)
