import re
from datetime import datetime

current_date = datetime.now().strftime("%Y_%m_%d")
base_url = "https://www.99acres.com/builders-in-vadodara-bffid"
file_name = re.search(r'(?!.*/).+', base_url.replace('-', '_')).group(0) + "_" + current_date+".csv"
print(file_name)
