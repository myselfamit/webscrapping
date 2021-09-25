import pandas as pd
import datetime
import csv



df = pd.read_csv('/home/ec2-user/ll3.csv')


saveto = []
for num in range(0,len(df)):
    for i in df['urls'][num].split(","):
        saveto.append(("/".join(i.split("/")[:7:])))

# path2 = f"/home/ec2-user/D/trial/cdata/cll3.csv"
y = pd.DataFrame(saveto)
y.to_csv('/home/ec2-user/e/trial/clean/cll3.csv', index=False)

# y.to_csv('/home/ec2-user/D/trial/cdata/cll3.csv', index=False)

df1 = pd.read_csv('/home/ec2-user/e/trial/clean/cll3.csv')
print(df1)

