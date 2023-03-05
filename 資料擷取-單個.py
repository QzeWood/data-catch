# Date： 2023/02/13
# Introduction：第二次嘗試使用py程式語言結合api獲取Bscscan鏈上单个用戶的交易數據。

import requests
import csv
import json

# 发送请求
response = requests.get("https://api.bscscan.com/api?module=account&action=txlist&address=0xa2665Ae7C2c061aAdD92E49988aE850D1026F59D&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=751CDDEMJGZMZ13SHPAFCKPI4842V6SIG4")

# 解析数据
data = json.loads(response.text)
print(data)


# 写入CSV文件
with open('dc.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["blockNumber", "timeStamp", "hash", "nonce", "blockHash", "transactionIndex", "from", "to", "value", "gas", "gasPrice", "isError", "txreceipt_status", "input", "contractAddress", "cumulativeGasUsed", "gasUsed", "confirmations", "methodId", "functionName"])
    for item in data['result']:
        writer.writerow([item['blockNumber'], item['timeStamp'], item['hash'], item['nonce'], item['blockHash'], item['transactionIndex'], item['from'], item['to'], item['value'], item['gas'], item['gasPrice'], item['isError'], item['txreceipt_status'], item['input'], item['contractAddress'], item['cumulativeGasUsed'], item['gasUsed'], item['confirmations'], item['methodId'], item['functionName']])
csv_output = r'D:\pytemp\data\uxlab\dc.csv'

print("ok！")