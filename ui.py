import streamlit as st
from st_pages import show_pages_from_config
import time
import os
import sys
import requests
from Services.createNewCompany import addNewCompany


def is_valid_url(url):
    try:
        response = requests.head(url)
        response.raise_for_status()  # Raises an exception for non-2xx status codes
        return True
    except requests.exceptions.RequestException:
        return False


# declaring custom css for the webpage
css = """
    <style>
    .stButton>button {
        width: 100px;
        height: 25px;
        font-size: 15px;
    }
    .css-q8sbsg p{
    font-size: 20px;
    }
    </style>
    
    """
st.set_page_config(page_title="LinkedIn jobs", page_icon="favicon.ico")
st.markdown(css, unsafe_allow_html=True,)


st.subheader("Add new company")
# taking input of new companies
with st.form("url_input"):
    new_company_url = st.text_input(
        "Enter the linkedin url of the company", "")
    submitted = st.form_submit_button("Add")
    if submitted:
        if is_valid_url(new_company_url):
            success_placeholder = st.empty()

            addNewCompany(new_company_url)
            success_placeholder.success(
                "new_company" + " added on the sidebar " + "!")
            time.sleep(1)
            success_placeholder.empty()
        else:
            failure_placeholder = st.empty()
            e = RuntimeError("Please provide a valid url!")
            failure_placeholder.exception(e)
            time.sleep(1)
            failure_placeholder.empty()

show_pages_from_config()
