from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import streamlit as st


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


def close_driver(driver):
    driver.close()
    driver.quit()


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


def addNewCompany(companyUrl):
    driver = getDriver()
    # if the link contains '/' as the last character

    if (companyUrl[len(companyUrl)-1] == '/'):
        companyUrl += "jobs"

    # if the link doesn't contain a '/' as the last character
    elif (companyUrl[len(companyUrl)-1] != '/'):
        companyUrl += "/jobs"
    driver.get("https://www.linkedin.com")
    sleep(2)
    driver.refresh()
    sleep(3)
    # idk why the page doesn't load in the first go that's why have to refresh the page
    email, loginpassword = read_email_and_password_from_file()
    username = driver.find_element(By.ID, 'session_key')
    username.send_keys(email)
    sleep(2)
    password = driver.find_element(By.ID, 'session_password')
    password.send_keys(loginpassword)
    sleep(2)
    sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
    sign_in_button.click()
    sleep(2)
    driver.get(companyUrl)
    sleep(10)
    close_driver(driver)
