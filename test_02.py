import re
import json
import requests
import json


def extract_key_value(json_data, key):
    """Extracts a specific key-value pair from a JSON data"""
    temp_data = json.loads(json_data)
    value = temp_data.get(key)
    return value


url = "https://www.99acres.com/builders-in-vadodara-bffid"

# html_doc = requests.get(url).text
f = open("99acers.txt", "r")
html_doc = f.read()

data = re.search(r"window.__initialData__=(.*?);", html_doc).group(1)
data = json.loads(data)

# pretty print the data:
# print(json.dumps(data, indent=4))
json_object = json.dumps(data, indent=4)

# -----

project_info = extract_key_value(json_object, "ProjectInfo")

with open("sample99.json", "w") as outfile:
    outfile.write(json.dumps(data, indent=4))

