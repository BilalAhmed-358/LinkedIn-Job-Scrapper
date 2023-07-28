from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
import streamlit as st

driver = None


def read_email_and_password_from_file(filename="credentials.txt"):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        # Remove any leading/trailing whitespaces and newline characters
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
    global driver

    if driver is None:
        opts = Options()
        service = Service(executable_path='./chrome.exe')
        driver = webdriver.Chrome(options=opts, service=service)
        driver.maximize_window()

    if (companyUrl[len(companyUrl)-1] == '/'):
        companyUrl += "jobs"
        driver.get("https://www.linkedin.com")
        # idk why the page doesn't load in the first go that's why have to refresh the page
        driver.refresh()
        sleep(3)
        email, loginpassword = read_email_and_password_from_file()
        username = driver.find_element(By.ID, 'session_key')
        username.send_keys(email)
        sleep(0.5)
        password = driver.find_element(By.ID, 'session_password')
        password.send_keys(loginpassword)
        sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
        sign_in_button.click()
        sleep(10)
        driver.close()
