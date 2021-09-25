import pandas as pd
import datetime
import csv


df = pd.read_csv('/home/ec2-user/ll6.csv')
df.dropna(inplace=True)
df.reset_index(drop=True,inplace=True)


saveto = []
for num in range(0,len(df)):
    for i in df['urls'][num].split(","):
        saveto.append(("/".join(i.split("/")[:7:])))

res = []
for i in saveto:
    if i not in res:
        res.append(i)

# path2 = f"/home/ec2-user/cll6.csv"
y = pd.DataFrame(res)
y.to_csv('/home/ec2-user/e/trial/clean/cll6.csv', index=False)

# y.to_csv('/home/ec2-user/D/trial/cdata/cll6.csv', index=False)

df1 = pd.read_csv('/home/ec2-user/e/trial/clean/cll6.csv')
print(df1)

