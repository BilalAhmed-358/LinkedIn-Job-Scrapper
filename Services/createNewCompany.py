from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import random
import streamlit as st
import os
from Services.ExtractCompanyName import extract_company_name


# Creates a new driver session


def getDriver():
    opts = Options()
    # opts.add_argument("--remote-debugging-port=9225")
    service_ = Service(executable_path='chromedriver.exe')
    try:
        driver = webdriver.Chrome(options=opts, service=service_)
    except Exception as e:
        print("Driver couldn't be created error is ", e)

    driver.maximize_window()
    return driver

# Deletes the current driver session


def close_driver(driver):
    driver.close()
    driver.quit()

# Reading email and password from the credentials file


def read_email_and_password_from_file(filename="credentials.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        email = lines[0]
        password = lines[1]

        return email, password
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except IndexError:
        print(
            f"File '{filename}' should have at least 2 lines (email and password).")
        return None


def generateCompanyUrl(companyUrl):
    # if the link contains '/' as the last character

    if (companyUrl[len(companyUrl)-1] == '/'):
        companyUrl += "jobs"

    # if the link doesn't contain a '/' as the last character
    elif (companyUrl[len(companyUrl)-1] != '/'):
        companyUrl += "/jobs"

    return companyUrl


def loginToLinkedin(driver):
    driver.get("https://www.linkedin.com")
    sleep(random.uniform(2, 3))
    # idk why the page doesn't load in the first go that's why have to refresh the page
    driver.refresh()
    sleep(random.uniform(2, 3))
    email, loginpassword = read_email_and_password_from_file()
    username = driver.find_element(By.ID, 'session_key')
    username.send_keys(email)
    password = driver.find_element(By.ID, 'session_password')
    password.send_keys(loginpassword)
    sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
    sign_in_button.click()
    sleep(15)


def createCompanyPage(companyName, link_data):
    new_File = True
    fileName = companyName+".py"
    # creating the separate page for the company
    filePath = os.path.join("companies", fileName)
    # writing the boiler plate code that will be present in the company page
    job_list = []
    for i in range(min(3, len(link_data))):
        job_entry = f"JOB: {i}, {link_data[i]}"
        job_list.append(job_entry)
    file_code = f"""
import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")
job_list_for_company= {job_list}
st.write("This is the page for {companyName} company")
st.write("The following jobs are available in the company")
for i in range(len(job_list_for_company)):
    st.write(job_list_for_company[i])
"""
    if not os.path.exists(filePath):
        with open(filePath, "w") as file:
            file.write(file_code)
    else:
        new_File = False
        with open(filePath, "a") as file:
            file_code_update = f"""
job_list_for_company= {job_list}
st.write("This is the page for {companyName} company")
st.write("The following jobs are available in the company")
for i in range(len(job_list_for_company)):
    st.write(job_list_for_company[i])
"""
            file.write(file_code_update)
        print(f"The company {companyName} already exists in the directory")

    # modifying the pages.toml file to show the newly added page in the side menu
    if new_File:
        toml_file_code = f"""
    
[[pages]]
path = "companies/{fileName}"
name = "{companyName}"
icon = ""
"""

        with open(".streamlit/pages.toml", "a") as file:
            file.write(toml_file_code)
        st.experimental_rerun()


def scrapData(url, driver):
    driver.get(url)
    emptyJobsClassName = "org-jobs-empty-jobs-module"
    # checking if there are any jobs posted the function will return false if there are no jobs
    try:
        element = driver.find_element(
            by=By.CLASS_NAME, value=emptyJobsClassName)
        return False
    # Here I will scrap the jobs and them in a data structure
    except NoSuchElementException:
        # print("There are jobs in this company!")
        # Get the element by the JS selector
        # print("Now selecting the job, hopefully everything goes well")
        job_list = driver.find_element(
            By.CSS_SELECTOR, ".artdeco-carousel__slider")
        children = job_list.find_elements(By.XPATH, '*')
        noOfChildren = len(children)
        limitOfJobs = min(noOfChildren, 3)
        job_links = []
        for i in range(3):
            post_link = driver.find_element(
                By.CSS_SELECTOR, f".artdeco-carousel__slider>li[data-item-index='{i}']>.artdeco-carousel__item-container>.full-height>.full-height>.job-card-container>.job-card-square__main>a")
            href = post_link.get_attribute("href")
            job_links.append(href)

            # print(href)
        # for child in children:
        #     print("\nChild Element")
        #     print(child.get_attribute('outerHTML'))
        # print("chal gaya!")
        # # Get the href attribute of the element
        # href = element.get_attribute("href")

        # # Print the href attribute
        # print(href)
        return job_links


def addNewCompany(Url):
    driver = getDriver()
    companyUrl = generateCompanyUrl(Url)
    loginToLinkedin(driver)
    driver.get(companyUrl)
    companyName = extract_company_name(companyUrl)
    data = scrapData(companyUrl, driver)
    # print("the value of data is", data)
    if data is False:
        return False
    else:
        createCompanyPage(companyName, data)
    sleep(10)
    close_driver(driver)
