# ----- EXTRACT DATA -----
import json
import re

import pandas as pd


def extract_key_value(json_data, key):
    """Extracts a specific key-value pair from a JSON data"""
    temp_data = json.loads(json_data)
    value = temp_data.get(key)
    return value


# ----- READ FROM FILE -----
f = open("99acers.txt", "r")
html_doc = f.read()

data = re.search(r"window.__initialData__=(.*?);", html_doc).group(1)
data = json.loads(data)
json_object = json.dumps(data, indent=4)


builderSrp = extract_key_value(json.dumps(data, indent=4), "builderSrp")
builderInfo = extract_key_value(json.dumps(builderSrp, indent=4), "builderInfo")

builder_name = []
projects_total = []
projects_completed = []
dataframe_final = pd.DataFrame()

for builder in range(len(data['builderSrp']['builderInfo'])):
    # print(builder)
    builderName = data['builderSrp']['builderInfo'][builder]['data']['name']
    builder_name.append(builderName)
    # print(builderName)

    totalProperties = data['builderSrp']['builderInfo'][builder]['data']['projectCount']['total']['value']
    projects_total.append(totalProperties)
    # print(totalProperties)

    readyToMove = data['builderSrp']['builderInfo'][builder]['data']['projectCount']['tuples'][0]['value']
    # print(readyToMove)
    projects_completed.append(readyToMove)

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
dataframe_final.to_csv("builders2.csv",encoding="utf-8")
