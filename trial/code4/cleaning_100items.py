import scrapy
import datetime
import w3lib
from scrapy.crawler import CrawlerProcess
from w3lib.http import basic_auth_header
import pandas as pd
import numpy as np



df = pd.read_csv('/home/ec2-user/c4c100items.csv')
df.dropna(inplace=True)
df.reset_index(drop=True,inplace=True)

# e1 = []
# e2 = []
# e3 = []
e4 = []
e5 = []
e6 = []
e7 = []
e8 = []
e9 = []

z = "https://www.amazon.in"

for num in range(0, len(df)):

    for b in df['rank'][num].split(","):
        e4.append(b)
        e6.append(df['cat'][num])
        e7.append(df['main_url'][num])

    for c in df['urls_100'][num].split(","):
        e5.append(z + ("?".join(c.split("?")[:1])))

    for d in df['asin'][num].split(","):
        e8.append(("/".join(d.split("/")[3:])))

for x in e8:
    e9.append(("?".join(x.split("?")[:1])))



dataframe=dict(Category=np.array(e6),Main_Url=np.array(e7),Product_Url=np.array(e5),ASIN=np.array(e9),Rank=np.array(e4))
dataf = pd.DataFrame.from_dict(dataframe, orient='index')
dataf = dataf.transpose()
dataf.dropna(inplace=True)
print(dataf)



dataf.to_csv('/home/ec2-user/e/trial/code4/cleaned_100items.csv', index=False)






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