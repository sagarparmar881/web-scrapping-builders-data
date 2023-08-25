import json
import os
import time
import pandas as pd
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from dotenv import load_dotenv

def scrap_data(url):
    """Extracts the data from every webpage into variable"""
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    scripts = soup.find_all("script", {"charset": "UTF-8"})
    data = str(scripts[2])
    pattern = r".*?\{(.*)}.*"
    data = re.search(pattern, data).group(1)
    data_new = json.loads("{" + data + "}")
    for builder in range(len(data_new["builderSrp"]["builderInfo"])):
        builder_name = data_new["builderSrp"]["builderInfo"][builder]["data"]["name"]
        builder_names.append(builder_name)
        project_total = data_new["builderSrp"]["builderInfo"][builder]["data"][
            "projectCount"
        ]["total"]["value"]
        projects_total.append(project_total)
        project_completed = data_new["builderSrp"]["builderInfo"][builder]["data"][
            "projectCount"
        ]["tuples"][0]["value"]
        projects_completed.append(project_completed)
    print("LOG: [COMPLETED] Extracting data from URL: " + url)
    time.sleep(5)


def write_csv():
    """Writes the extracted data to CSV file"""
    current_date = datetime.now().strftime("%Y_%m_%d")
    file_name = ('99acers_'
                 + re.search(r'(?!.*/).+', base_url.replace('-', '_')).group(0)
                 + "_" + current_date + ".csv")
    print("LOG: [STARTED] Writing data to CSV: " + file_name)
    builders_data = {
        "builder_name": builder_names,
        "projects_total": projects_total,
        "projects_completed": projects_completed,
    }
    builders_data_scrapped = pd.DataFrame(builders_data)
    dataframe = dataframe_final._append(builders_data_scrapped, ignore_index=True)
    dataframe.to_csv('data/'+file_name, encoding="utf-8")
    print("LOG: [COMPLETED] Writing data to CSV: " + file_name)


def get_total_pages(url):
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    counter = len(soup.find_all("div", {"class": "Pagination__builderSrpPageBubble"}))
    print("LOG: [INFO] Total pages to be extracted: " + str(counter))
    return counter


# ----- MAIN PROGRAM -----

load_dotenv()

builder_names = []
projects_total = []
projects_completed = []
dataframe_final = pd.DataFrame()

base_url = os.getenv("BASE_URL_99_ACERS")

total_pages = get_total_pages(base_url)
for page in range(1, total_pages+1):
    if page == 1:
        scrap_data(base_url)
    else:
        scrap_data(base_url+'-page-{}'.format(page))
write_csv()
