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


def createCompanyPage(companyName):
    fileName = companyName+".py"
    # creating the separate page for the company
    filePath = os.path.join("companies", fileName)

    # writing the boiler plate code that will be present in the company page
    file_code = f"""
import streamlit as st
from st_pages import add_page_title

add_page_title(layout="wide")

st.write("This is the page for {companyName} company")
"""
    if not os.path.exists(filePath):
        with open(filePath, "w") as file:
            file.write(file_code)
    else:
        print(f"The company {companyName} already exists in the directory")

    # modifying the pages.toml file to show the newly added page in the side menu
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
    try:
        element = driver.find_element(
            by=By.CLASS_NAME, value=emptyJobsClassName)
        return False
    except NoSuchElementException:
        print("There are jobs in this company!")
        return True


def addNewCompany(Url):
    driver = getDriver()
    companyUrl = generateCompanyUrl(Url)
    loginToLinkedin(driver)
    driver.get(companyUrl)
    companyName = extract_company_name(companyUrl)
    data = scrapData(companyUrl, driver)
    print("the value of data is", data)
    if data is False:
        return False
    # if data:
    #     createCompanyPage(companyName)
    sleep(10)
    close_driver(driver)
