import requests
from bs4 import BeautifulSoup


URL = "https://catalogs.nmsu.edu/nmsu/arts-sciences/computer-science/#coursestext"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="coursestextcontainer")
print(results.prettify())
# job_elems = results.find_all("p", class_="courseblocktitle noindent")
# CS_COURSE = []
# for job_elem in job_elems:
#     course_elem = job_elem.find("strong")
#     course_info = str(course_elem.text)
#     course_info = course_info.split(".")
#     course_num = course_info[0]
#     course_title = course_info[1]
#     CS_COURSE.append(course_num)
#     CS_COURSE.append(course_title)
# print(CS_COURSE)
