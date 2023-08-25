# Web Scrapping Builders Data

Extracts the data of builders from websites.

## Description

This repository contains a Python script that can be used to scrape data of builders and their projects from the websites 99acres and Magicbricks. The script uses the BeautifulSoup library to parse the HTML code of the websites and extract the desired data.

## Getting Started

### Dependencies

* Python3

### Cloning and Downloading Libraries

* Clone this repository.
* Get all required libraries.
```
pip install -r requirements.txt
```

## File Structure

This repository contains two files:
* data_scrap_99acers.py
* data_scrap_magicbricks.py

## How to run 

### [1] Webscraping from MagicBricks.com
* Update the base url of website in file: "*data_scrap_magicbricks.py*"
```
base_url = "https://www.magicbricks.com/mbutility/builders-in-Vadodara?page={}".format(page)
```
* Execute file: "*data_scrap_magicbricks.py*"

### [2] Webscraping from 99acers.com
Update the base url in file: "*data_scrap_99acers.py*"
```
base_url = "https://www.99acres.com/builders-in-vadodara-bffid"
```
Execute file: "*data_scrap_99acers.py*"

## How to run 

Results will the saved in the *.csv* file of respective folder. 