from urllib.parse import urlparse


def extract_company_name(url):
    parsed_url = urlparse(url)
    path = parsed_url.path

    # Split the path using "/" and get the last element (company name)
    company_name = path.strip("/").split("/")[-2]


    return company_name.capitalize()
