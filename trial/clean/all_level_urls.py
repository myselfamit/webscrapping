import pandas as pd


d2 = pd.read_csv('/home/ec2-user/e/trial/clean/cll2.csv')
d3 = pd.read_csv('/home/ec2-user/e/trial/clean/cll3.csv')
d4 = pd.read_csv('/home/ec2-user/e/trial/clean/cll4.csv')
d5 = pd.read_csv('/home/ec2-user/e/trial/clean/cll5.csv')
d6 = pd.read_csv('/home/ec2-user/e/trial/clean/cll6.csv')


frames = [d2, d3, d4, d5, d6]
result = pd.concat(frames)


res = []
for i in result["0"]:
    if i not in res:
        res.append(i)

res1 = res.copy()


data1=[]
for i in res1:
    data1.append(i + "/ref=zg_bs_pg_1")

data2=[]
for i in res:
    data2.append(i + "/ref=zg_bs_pg_2?ie=UTF8&pg=2")

data = data1 + data2


final = []
for i in data:
    if i not in final:
        final.append(i)


df = pd.DataFrame({'urls':final})
print (df)


df.to_csv('/home/ec2-user/e/trial/clean/all_level_urls.csv', index=False)

# df.to_csv('/home/ec2-user/D/trial/clean/all_level_urls.csv', index=False)