# import necessary modules
# import re
# import csv
# eng_bible = []
# html_cleaner = re.compile('<.*?>')
# with open('bibleTest.csv', encoding='utf-8', errors='ignore')as f:
#     data = csv.reader(f, delimiter=",")
#
#     for row in data:
#         print(": ".join(row))

import pandas as pd

df = pd.read_csv('bibleTest.csv')

print(df.head())





