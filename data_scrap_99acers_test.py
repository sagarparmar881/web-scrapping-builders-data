import json
import re
import time
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import WebDriverException


def scrap_data(url):
    """This method extracts the data from every single webpage."""
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
    except:
        print("LOG: [ERROR] Problem in scrapping data" + " ...")
    else:
        scripts = soup.find_all("script", {"charset": "UTF-8"})
        data = str(scripts[2])
        pattern = r".*?\{(.*)}.*"
        data = re.search(pattern, data).group(1)
        data_new = json.loads("{" + data + "}")
        for builder in range(len(data_new["builderSrp"]["builderInfo"])):
            builder_name = data_new["builderSrp"]["builderInfo"][builder]["data"]["name"]
            builder_names.append(builder_name)
            project_total = data_new["builderSrp"]["builderInfo"][builder]["data"]["projectCount"]["total"]["value"]
            projects_total.append(project_total)
            project_completed = data_new["builderSrp"]["builderInfo"][builder]["data"]["projectCount"]["tuples"][0][
                "value"]
            projects_completed.append(project_completed)
        print("LOG: [COMPLETED] Extracting data from URL: " + url + " ...")
    finally:
        driver.close()
        time.sleep(5)


def write_csv(file_name):
    """This method writes the extracted data to CSV file."""
    print("LOG: [STARTED] Writing data to CSV: " + file_name + " ...")
    # global dataframe_final
    builders_data = {"builder_name": builder_names, "projects_total": projects_total,
                     "projects_completed": projects_completed, }
    builders_data_scrapped = pd.DataFrame(builders_data)
    dataframe = dataframe_final._append(builders_data_scrapped, ignore_index=True)
    now = datetime.now()
    current_date = now.strftime("%Y_%m_%d")
    dataframe.to_csv(file_name + "_" + current_date + ".csv", encoding="utf-8")
    print("LOG: [COMPLETED] Writing data to CSV: " + file_name + " ...")


def get_total_pages(url):
    """This method counts or finds total pages to load and extract data."""
    print("LOG: [STARTED] Counting total pages to be extracted.")
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
        print("LOG: [COMPLETED] Total pages to be extracted: " + str(counter) + " ...")
        return counter
    finally:
        driver.close()


# ----- MAIN PROGRAM -----

builder_names = []
projects_total = []
projects_completed = []
dataframe_final = pd.DataFrame()
base_url = "https://www.99acres.com/builders-in-ahmedabad-bffid"
total_pages = get_total_pages(base_url)
for page in range(1, total_pages + 1):
    if page == 1:
        # base_url = "https://www.99acres.com/builders-in-ahmedabad-bffid"
        scrap_data(base_url)
    else:
        # base_url = "https://www.99acres.com/builders-in-vadodara-bffid-page-{}".format(page)
        scrap_data(base_url.format(page))

write_csv("data_99acers")
