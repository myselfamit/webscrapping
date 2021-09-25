import pandas as pd
import datetime


df1 = pd.read_csv('/home/ec2-user/e/trial/code4/cleaned_100items.csv')

df2 = pd.read_csv('/home/ec2-user/e/trial/code4/cleaned_product_details_urls.csv')

# Removing rupee symbol

df2["price1"] = df2["price1"].astype(str)
df2["price2"] = df2["price2"].astype(str)
df2["price3"] = df2["price3"].astype(str)

df2["sold_1"] = df2["sold_1"].astype(str)
df2["sold_2"] = df2["sold_2"].astype(str)
df2["sold_3"] = df2["sold_3"].astype(str)
df2["sold_4"] = df2["sold_4"].astype(str)



for i in range(0,len(df2["price1"])):
    df2["price1"][i] = df2["price1"][i].replace("₹","")
print("ignore warning, created successfully")


for i in range(0,len(df2["price2"])):
    df2["price2"][i] = df2["price2"][i].replace("₹","")
print("ignore warning, created successfully")


for i in range(0,len(df2["price3"])):
    df2["price3"][i] = df2["price3"][i].replace("₹","")
print("ignore warning, created successfully")



# Review editing

for i in range(0,len(df2["review"])):
    if df2["review"][i].count(",") == 0:
        pass
    if df2["review"][i].count(",") == 1:
        df2["review"][i] = (",".join(df2["review"][i].split(",")[:-1]))
    if df2["review"][i].count(",") == 3:
        df2["review"][i] = (",".join(df2["review"][i].split(",")[:-2]))
    if df2["review"][i].count(",") == 5:
        df2["review"][i] = (",".join(df2["review"][i].split(",")[:-4]))
print("ignore warning, created successfully")


# removing the spaces

for i in range(0,len(df2["sold_1"])):
    df2["sold_1"][i] = df2["sold_1"][i].replace("\n","")
print("ignore warning, created successfully")

for i in range(0,len(df2["sold_2"])):
    df2["sold_2"][i] = df2["sold_2"][i].replace("\n","")
print("ignore warning, created successfully")

for i in range(0,len(df2["sold_3"])):
    df2["sold_3"][i] = df2["sold_3"][i].replace("\n","")
print("ignore warning, created successfully")

for i in range(0,len(df2["sold_4"])):
    df2["sold_4"][i] = df2["sold_4"][i].replace("\n","")
print("ignore warning, created successfully")




# Removing '#' from rank

for i in range(0,len(df1['Rank'])):
    df1["Rank"][i] = df1["Rank"][i].replace("#","")
print("ignore warning, created successfully")


df = pd.merge(df1, df2, how='inner', left_on=['ASIN'], right_on=['ASIN'])
print("========================= X ========================= X =========================")
print(len(df))
print("========================= X ========================= X =========================")
print(df.isnull().sum())
print("========================= X ========================= X =========================")



df.drop(['Product_Url_y'], axis=1,inplace= True)


df["review"] = df["review"].astype(str)

for i in range(0,len(df["review"])):
    if df['review'][i].count(",") > 5:
        df['review'][i] = (",".join(df["review"][i].split(",")[:-4]))

for i in range(0,len(df["review"])):
    df['review'][i] = df['review'][i].replace(" ratings","")




x = format(datetime.date.today())
path3 = f"/home/ec2-user/e/trial/code4/final/final_amazon_{x}.csv"

df.to_csv(path3, index=False)
print("df is successfully created")



#
# x = format(datetime.date.today())
# path3 = f"/home/ec2-user/D/trial/final output/final_amazon_{x}.csv"
# path4 = f"/home/ec2-user/D/trial/final output/final_amazon_{x}.zip"
# na=f'file_{x}.csv'
# print(na)
# compression_opts = dict(method='zip',archive_name=na)
# df.to_csv(path3, index=False)
# print("converted to csv")
# df.to_csv(path4, index=False,compression=compression_opts)
# print("converted to zip")




# x = round(len(df)/4)
# x

# x1 = df[:x]
# print(len(x1))
# x2 = df[x:(x+x)]
# print(len(x2))
# x3 = df[(x+x):(x+x+x)]
# print(len(x3))
# x4 = df[(x+x+x):]
# print(len(x4))
