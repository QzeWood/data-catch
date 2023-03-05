# Date： 2023/02/23
# Introduction：
import os
import requests
import csv
import json
import pandas as pd

file_dir = "D:/pytemp/data/uxlab/bscdata/1111"  # file directory
all_csv_list = os.listdir(file_dir)  # get csv list
for single_csv in all_csv_list:
    df = pd.read_csv(os.path.join(file_dir, single_csv))
    print(single_csv)

    df = df.iloc[:,1]
    df_list = df.values.tolist()
    data_list = []
    for items in df_list:
        url = "https://api.bscscan.com/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=751CDDEMJGZMZ13SHPAFCKPI4842V6SIG4".format(items)
        response = requests.get(url)
        data = json.loads(response.text)
        data_list.extend(data['result'])

with open('1.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timeStamp", "from", "to", "value", "isError", "methodId", "functionName"])
    for item in data_list:
        writer.writerow([item['timeStamp'], item['from'], item['to'], item['value'], item['isError'], item['methodId'], item['functionName']])


csv_output = r'D:\pytemp\data\uxlab\bscdata\usertxn\jiance1111.csv'
print(csv_output)
print("============================================================================")
print("ok!")