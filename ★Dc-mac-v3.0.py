# Date： 2023/4/10 18:41
# Author: Mr. Q
# Introduction：超级自动化版本的资料抓取代码，您只需要将表格第一列键入"玩家钱包地址"，第二列插入"used"，值全部输入为"0"，即可进行自动化资料抓取，
#成功抓完的"地址"会在"used"列被标记为"1"。如果出现网路故障或是API受限也不用担心，因为此代码会贴心地帮你自动校准并实时更新，所以完全不用担心从头再来~

import time

start_time = time.time()
print(start_time)
print("======================================")
import time
import csv
import pandas as pd
import requests
import json
import urllib3
urllib3.disable_warnings()

df = pd.read_csv('/Users/wood/Desktop/UXLab/knife/2Mobox-0.csv')
df_list = df.iloc[:, 0].values.tolist()

with open('/Users/wood/Desktop/UXLab/data_v2/Mobox-v2.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["timeStamp", "from", "to", "value", "isError", "methodId", "functionName"])

    while True:
      try:
        for i, item in enumerate(df.iloc[:, 0]):
            if df.iloc[i, 1] == 0:
                address = item
            else:
                continue
            start_time1 = time.time()
            url = "https://api.bscscan.com/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=751CDDEMJGZMZ13SHPAFCKPI4842V6SIG4".format(item)
            # API-1
            # url = "https://api.bscscan.com/api?module=account&action=txlist&address={}&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=2WEFUT419XVIBYRP4U1IG4BGZEBIH6T1PZ".format(item)
            # API-2
            print(f"{i} \t {address}")
            # df.iloc[i, 1] = 1  # mark the item as used
            # df.to_csv('/Users/wood/Desktop/UXLab/knife/Bnx-left.csv', index=False)
            response = requests.get(url, verify=False)
            data = json.loads(response.text)
            second_time = time.time()
            if second_time - start_time1 > 30:
                print("========Rerun========")
                time.sleep(3)
            # print(data)

            for row in data['result']:
                writer.writerow([row['timeStamp'], row['from'], row['to'], row['value'], row['isError'], row['methodId'], row['functionName']])
                file.flush()  # flush the buffer to write data to the file in real-time

            if not data['result']:
                print(f"No data returned for {address}, stopping the loop.")
                break
            end_time1 = time.time()
            df.iloc[i, 1] = 1  # mark the item as used
            df.to_csv('/Users/wood/Desktop/UXLab/knife/2Mobox-0.csv', index=False)
            duration = end_time1 - start_time1
            print(f"API執行時間為 {duration:.2f} 秒")
        if not df.iloc[i, 1] == 0:
            print('Done')
            break
      except Exception as e:
        print("Error", e)
        time.sleep(3)

        # time.sleep(15)  # wait for 60 seconds before trying again

print("======================================")
print("ok!!")



end_time = time.time()
print(end_time)
duration = end_time - start_time
print(f"程式執行時間為 {duration:.2f} 秒")
