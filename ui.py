import streamlit as st
from pathlib import Path
from st_pages import show_pages_from_config
import time
import requests


def is_valid_url(url):
    try:
        response = requests.head(url)
        response.raise_for_status()  # Raises an exception for non-2xx status codes
        return True
    except requests.exceptions.RequestException:
        return False


# taking input of new companies
new_company_url = st.text_input("Enter the linkedin url of the company", "")
if is_valid_url(new_company_url):
    success_placeholder = st.empty()
    success_placeholder.success("new_company" + " added on the sidebar " + "!")
    time.sleep(2)  # Wait for 2 seconds
    success_placeholder.empty()
else:
    failure_placeholder = st.empty()
    e = RuntimeError("Please provide a valid url!")
    failure_placeholder.exception(e)
    time.sleep(2)  # Wait for 2 seconds
    failure_placeholder.empty()
show_pages_from_config()
