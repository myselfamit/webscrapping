import scrapy
import datetime
import w3lib
from scrapy.crawler import CrawlerProcess
from w3lib.http import basic_auth_header
import pandas as pd
import numpy as np


df = pd.read_csv('/home/ec2-user/c5product_details_urls.csv')
# df.dropna(inplace=True)
df.reset_index(drop=True,inplace=True)


for i in range(0,len(df['ASIN'])):
    df['ASIN'][i] = ("/".join(df['ASIN'][i].split("/")[5:]))
print(df['ASIN'])

for num in range(0, len(df['name'])):
    df['name'][num] = df['name'][num].strip()



df.to_csv('/home/ec2-user/e/trial/code5/cleaned_product_details_urls.csv', index=False)






# for a in df['name'][num].split("\n"):
#     e1.append(a.strip())



# for x in e1:
#     if len(x) == 1:
#         pass
#     if len(x) > 2:
#         e2.append(x)
#     e3 = list(dict.fromkeys(e2))



# iter1=[]
# final = []
# for num in range(0,len(df)):
#     for i in df['Product_Url'][num].split(","):
#         iter1.append(("/".join(i.split("/")[6:])))
#     for x in iter1:
#         final.append(("?".join(x.split("?")[:1])))
# final