import requests
from bs4 import BeautifulSoup
import pprint
import numpy as np
import pandas as pd
from pandas.io.html import read_html
from selenium import webdriver
import time


def printProf():
    URL = "https://www.cs.nmsu.edu/wp/people/faculty/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="entry-content")
    # print(results.prettify())

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
    print(prof_dict)


def printCourseTitles():
    URL = "https://catalogs.nmsu.edu/nmsu/arts-sciences/computer-science/#coursestext"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="sc_sccoursedescs")
    # print(results.prettify())

    job_elems = results.find_all("p", class_="courseblocktitle noindent")
    for job_elem in job_elems:
        course_elem = job_elem.find("strong")
        course_info = str(course_elem.text)
        course_info = course_info.split(".")
        course_num = course_info[0]
        course_title = course_info[1]
        print(course_num)
        print(course_title)


def printCourseInfo():
    URL = "https://accounts.nmsu.edu/catalog/"
    driver = webdriver.Safari()
    driver.implicitly_wait(30)
    driver.get(URL)
    button = driver.find_element_by_id("id_MA")
    time.sleep(5)
    button.click()
    time.sleep(5)
    button1 = driver.find_element_by_xpath(
        '//select[@name="term"]/option[@value="202010"]'
    )
    button1.click()
    button2 = driver.find_element_by_xpath(
        '//select[@name="dept"]/option[@value="C S"]'
    )
    button2.click()
    time.sleep(5)
    button3 = driver.find_element_by_xpath('//input[@value="Get Courses"]')
    button3.click()
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "lxml")
    results = soup.find(class_="zebra-table")
    # print(results.prettify())

    table = soup.find_all("table")[0]
    df = pd.read_html(str(table), header=0)
    df_clean = df[0]
    df_clean = df_clean.dropna(how="all")
    df_clean = df_clean.drop(["CRN", "Status", "Cap", "Act", "Rem"], axis=1)

    for i in range(0, len(df_clean)):
        nan = np.nan
        if pd.isnull(df_clean.iloc[i]["Subj"]):
            df_clean.iloc[i]["Subj"] = df_clean.iloc[i - 1]["Subj"]
            df_clean.iloc[i]["Crse"] = df_clean.iloc[i - 1]["Crse"] + "L"
            df_clean.iloc[i]["Sec"] = df_clean.iloc[i - 1]["Sec"]
            df_clean.iloc[i]["Cmp"] = df_clean.iloc[i - 1]["Cmp"]
            df_clean.iloc[i]["Cred"] = 0
            df_clean.iloc[i]["Title"] = df_clean.iloc[i - 1]["Title"] + "-LAB"

    pprint.pprint(df_clean.values.tolist())


printCourseInfo()
# printProf()
# printCourseTitles()
