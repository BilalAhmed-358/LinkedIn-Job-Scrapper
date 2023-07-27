from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


print("new company create function called!")
# opts = Options()
# service = Service(executable_path='./chrome.exe')
# driver = webdriver.Chrome(options=opts, service=service)


def addNewCompany(companyUrl):
    # print("The url of the company is ", companyUrl)
    if (companyUrl[len(companyUrl)-1] == '/'):
        companyUrl += "jobs"
        print(companyUrl)


# driver.get("https://www.linkedin.com")

# time.sleep(25)
