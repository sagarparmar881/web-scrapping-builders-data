import json
import os
import re
import time
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import WebDriverException


def get_total_pages(url):
    """This method counts total pages to srap from the website."""
    print("LOG: [STARTED] Counting total pages to be extracted ...")
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
    except WebDriverException:
        print("LOG: [ERROR] Problem in parsing URL" + " ...")
    except:
        print("LOG: [ERROR] Problem in program" + " ...")
    else:
        counter = len(soup.find_all("div", {"class": "Pagination__builderSrpPageBubble"}))
        print("LOG: [INFO] Total pages to be extracted: " + str(counter))
        return counter
    finally:
        driver.close()


def scrap_data(url):
    """Extracts the data from every webpage into lists."""
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
    except:
        print("LOG: [ERROR] Problem in scrapping data" + " ...")
    else:
        all_script_tags = soup.find_all("script", {"charset": "UTF-8"})
        script_tag = str(all_script_tags[2])
        pattern = r".*?\{(.*)}.*"
        extracted_raw_data = re.search(pattern, script_tag).group(1)
        extracted_json_data = json.loads("{" + extracted_raw_data + "}")
        extracted_tag_builder_info = extracted_json_data["builderSrp"]["builderInfo"]

        for builder in range(len(extracted_tag_builder_info)):
            extracted_builder_data = extracted_tag_builder_info[builder]["data"]

            # Extracts the builder name
            builder_name = extracted_builder_data["name"]
            builder_names.append(builder_name)

            # Extracts the builder projects (total)
            extracted_builder_projects = extracted_builder_data["projectCount"]
            project_total = extracted_builder_projects["total"]["value"]
            projects_total.append(project_total)

            # Extracts the builder projects (completed)
            project_completed = extracted_builder_projects["tuples"][0]["value"]
            projects_completed.append(project_completed)

        print("LOG: [COMPLETED] Extracting data from URL: " + url)
    finally:
        driver.close()
        time.sleep(5)


def write_to_csv():
    """This method writes the extracted data to CSV file"""
    print("LOG: [STARTED] Writing data to CSV " + " ...")

    # Generates the file name as '[WEBSITE]_[CITY_NAME]_[DATE_STAMP].[CSV]'
    current_date = datetime.now().strftime("%d%m%Y_%H%M%S")
    file_name_0 = '99acers'
    file_name_1 = re.search(r'(?!.*/).+', base_url.replace('-', '_')).group(0)
    file_name = str.lower(file_name_0 + '_' + file_name_1[:-6] + '_' + current_date + '.csv')

    builders_data = {
        "builder_name": builder_names,
        "projects_total": projects_total,
        "projects_completed": projects_completed,
    }
    builders_data_scrapped = pd.DataFrame(builders_data)
    dataframe = dataframe_final._append(builders_data_scrapped, ignore_index=True)

    # Checks if the dataframe are empty before saving to CSV file
    if is_empty(dataframe):
        print("LOG: [COMPLETED] No Data found to write CSV ...")
    else:
        dataframe.to_csv('data/' + file_name, encoding="utf-8")
        print("LOG: [COMPLETED] Writing data to CSV: " + file_name)


def is_empty(dataframe):
    """This method checks if the extracted dataframe is empty"""
    return dataframe.empty


# ----- MAIN PROGRAM -----

load_dotenv()
base_url = os.getenv("BASE_URL_99_ACERS")

builder_names = []
projects_total = []
projects_completed = []
dataframe_final = pd.DataFrame()

try:
    total_pages = get_total_pages(base_url)
    for page in range(1, total_pages + 1):
        if page == 1:
            scrap_data(base_url)
        else:
            scrap_data(base_url + '-page-{}'.format(page))
    write_to_csv()
except:
    print("LOG: [ERROR] Problem in program" + " ...")
