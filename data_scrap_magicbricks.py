# python program to extract data of top builders in vadodara from 'magicbricks'

# ---- IMPORT STARTS ----

# import numpy as np
import pandas as pd
import time
from datetime import timedelta
import requests
import re
from bs4 import BeautifulSoup

# -- IMPORT ENDS----

# base_url = "https://www.magicbricks.com/mbutility/builders-in-Vadodara?page=1"
# page = requests.get(base_url)
#
# soup = BeautifulSoup(page.content, "html.parser")

# total_number_of_webpages = len(soup.find_all("li", {"class": "mb-pagination__list--item"}))
# print(total_number_of_webpages)

# ----- MAIN STARTS -----
start_time = time.time()
dataframe_final = pd.DataFrame()

builder_name = []
projects_total = []
projects_completed = []

total_number_of_webpages = 1
for page in range(1, total_number_of_webpages):
    base_url = "https://www.magicbricks.com/mbutility/builders-in-Vadodara?page={}".format(page)
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, "html.parser")
    total_number_of_webpages = len(soup.find_all("li", {"class": "mb-pagination__list--item"}))
    cards = soup.find_all("div", {"class": "card"})

    for card in cards:
        # 1. builder_name
        try:
            builder_name.append(card.find("h3").text.strip())
        except:
            builder_name.append(None)

        # 2. projects_total
        try:
            projects_total.append(card.find("div", class_="builder__projects-total").text.strip())
        except:
            projects_total.append(None)

        # 3. projects_completed
        try:
            projects_completed.append(card.find("div", class_="builder__projects-status").text.strip())

        except:
            projects_completed.append(None)

    loop_time = time.time()

    # make a dictionary containing all the data extracted
    col_dic = {
        "name": builder_name,
        "projects_total": projects_total,
        "projects_completed": projects_completed
    }

    # pass the dictionary to pandas to create a dataframe (page)
    df = pd.DataFrame(col_dic)

    # append the dataframe to the final dataframe (the whole website)
    dataframe_final = dataframe_final._append(df, ignore_index=True)

    # success
    # print("success!")
    # print("time taken:", round((time.time() - loop_time) * 1000, 2), "ms")
    # print("total time elapsed:", str(timedelta(seconds=(time.time() - start_time))))
    # print()

# ---- MAIN ENDS ----
end_time = time.time()
print("full website scraped successfully!")
print("total time taken:", str(timedelta(seconds=(end_time - start_time))))
print()

# Print some statistics about the final dataframe:
print("dataframe shape", dataframe_final.shape)
print()
print("column-wise null count")
print(dataframe_final.isna().sum())
print()

# export the data to external csv
dataframe_final.to_csv("builders.csv", encoding="utf-8")

print(builder_name)
print(projects_total)
print(projects_completed)

print(len(builder_name))
print(len(projects_total))
print(len(projects_completed))
