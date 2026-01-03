import streamlit as st
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@st.cache_resource
def scrape_website(website):
    options = Options()
    # These 5 flags are REQUIRED for Streamlit Cloud
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
        options=options,
    )
    
    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source

        return html
    
    finally:
        driver.quit()


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:

        return str(body_content)
    
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,"html.parser")

    for script_or_style in soup(["script","style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content


def split_dom_content(dom_content,max_l = 6000):

    return[
        dom_content[i: i + max_l] for i in range(0,len(dom_content),max_l)
    ]
