import pandas as pd

df1 = pd.read_csv(r'D:\pytemp\data\uxlab\bscdata\CSV档案\遊玩行為\Test1Ee.csv') #讀取文件，並存入DataFrame，並命名為df1
df1_new = df1.iloc[:,6] #選擇文件中的第6列，並將其存為一個新的pandas Series，並命名為df1_new
df1_new.values.tolist() #將 'df1_new' 轉換為 Python 的列表格式，並賦值給 'df1_new'。
Test1Ee = [] #創建一個空列表 'Test1Ee'。
for items in df1_new: #這是一個循環，將df1_new中的每個元素添加到“items”，
    if items not in Test1Ee: #如果“items”不存在於'Test1Ee' 中，
        Test1Ee.append(items) #則將 'items' 添加到 'Test1Ee' 列表的末尾
    else:   #否則，就繼續
        continue
df1 = pd.DataFrame(Test1Ee) #將 'Test1Ee' 轉換為 pandas DataFrame，並命名為 'df1'。
#df1.to_csv(r'D:\pytemp\data\uxlab\bscdata\CSV档案\遊玩行為\Test1Ee_new.csv')

print(df1_new)
print('success')
