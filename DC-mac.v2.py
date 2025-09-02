# Date： 2023/02/20
# Introduction：資料擷取最終版

import os
import requests
import csv
import json
import pandas as pd
import time

start_time = time.time()
print(start_time)
print("======================================")

df = pd.read_csv('/Users/wood/Desktop/UXLab/knife/Bnx/Bnx1.csv')

df = df.iloc[:,0]
print(df)
df_list = df.values.tolist()
data_list = []

for items in df_list:
    # API-1
    url = "https://api.bscscan.com/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=YourApiKey".format(items)
    response = requests.get(url)
    data = json.loads(response.text)
    data_list.extend(data['result'])
    if not data['result']:
        print(f"No data returned for {items}, stopping the loop.")
        break

#！！！這裡記得要改文件名字！！！
with open('/Users/wood/Desktop/UXLab/data_v2/Bnx-v2.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timeStamp", "from", "to", "value", "isError", "methodId", "functionName"])
    for item in data_list:
        writer.writerow([item['timeStamp'], item['from'], item['to'], item['value'], item['isError'], item['methodId'], item['functionName']])

print("======================================")
print("ok!!")

end_time = time.time()
print(end_time)
duration = end_time - start_time
print(f"程式執行時間為 {duration:.2f} 秒")

import os
os.system('say "Done"')
