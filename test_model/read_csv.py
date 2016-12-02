import csv

# 读取本地 CSV 文件
date = csv.reader(open('./config_file/info.csv', 'r'))

# 循环输出每一行信息
for user in date:
    print(user)