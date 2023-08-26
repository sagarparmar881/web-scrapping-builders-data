import os
import re
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def get_total_pages(url):
    """This method counts total pages to srap from the website."""
    print("LOG: [STARTED] Counting total pages to be extracted.")
    try:
        page_source = requests.get(url)
    except:
        print("LOG: [ERROR] Problem in parsing URL" + " ...")
    else:
        soup = BeautifulSoup(page_source.content, "html.parser")
        counter = len(soup.find_all("li", {"class": "mb-pagination__list--item"}))
        print("LOG: [INFO] Total pages to be extracted: " + str(counter))
        return counter


def scrap_data(url):
    """Extracts the data from every webpage into lists."""
    try:
        page_source = requests.get(url)
    except:
        print("LOG: [ERROR] Problem in scrapping data" + " ...")
    else:
        soup = BeautifulSoup(page_source.content, "html.parser")
        cards = soup.find_all("div", {"class": "card"})
        for card in cards:
            try:
                builder_name.append(card.find("h3").text.strip())
            except:
                builder_name.append(None)

            try:
                projects_total.append(card.find("div", class_="builder__projects-total").text.strip())
            except:
                projects_total.append(None)

            try:
                projects_completed.append(card.find("div", class_="builder__projects-status").text.strip())
            except:
                projects_completed.append(None)


def write_to_csv():
    """This method writes the extracted data to CSV file"""
    current_date = datetime.now().strftime("%d%m%Y_%H%M%S")
    file_name_0 = 'magicbricks'
    file_name_1 = re.search(r'(?!.*/).+', base_url.replace('-', '_')).group(0)
    file_name = str.lower(file_name_0 + '_' + file_name_1 + '_' + current_date + '.csv')

    builders_data = {
        "name": builder_name,
        "projects_total": projects_total,
        "projects_completed": projects_completed
    }
    builders_data_scrapped = pd.DataFrame(builders_data)
    dataframe = dataframe_final._append(builders_data_scrapped, ignore_index=True)
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
base_url = os.getenv("BASE_URL_MAGICBRICKS")

builder_name = []
projects_total = []
projects_completed = []
dataframe_final = pd.DataFrame()

try:
    total_pages = get_total_pages(base_url)
    for page in range(1, total_pages + 1):
        scrap_data(base_url + "?page={}".format(page))
    write_to_csv()
except:
    print("LOG: [ERROR] Problem in program" + " ...")
