# https://www.geeksforgeeks.org/how-to-run-multiple-python-file-in-a-folder-one-after-another/

import os
import time
import datetime
date_time = format(datetime.date.today())


# deleting if exits c100items.csv
if os.path.exists('/home/ec2-user/c5c100items.csv'):
    os.remove('/home/ec2-user/c5c100items.csv')
    print("xxxxxxxxxxx           c100items.csv removed successfully")


# step 2 , c100items.py
os.system('python3 /home/ec2-user/e/trial/code5/c100items.py')
time.sleep(10)
print("===========      created c100items.csv")
print(datetime.datetime.now())



# deleting if exits cleaning_100items.csv
if os.path.exists('/home/ec2-user/e/trial/code5/cleaned_100items.csv'):
    os.remove('/home/ec2-user/e/trial/code5/cleaned_100items.csv')
    print("xxxxxxxxxxx           cleaned_100items.csv removed successfully")



# step 3 , cleaning_100items.py
os.system('python3 /home/ec2-user/e/trial/code5/cleaning_100items.py')
time.sleep(10)
print("===========      created cleaning_100items.csv")
print(datetime.datetime.now())



# deleting if exits products_details_urls.csv
if os.path.exists('/home/ec2-user/c5product_details_urls.csv'):
    os.remove('/home/ec2-user/c5product_details_urls.csv')
    print("xxxxxxxxxxx           cleaned_product_details_urls.csv removed successfully")

# time.sleep(15)

# step 4 , products_details.py
os.system('python3 /home/ec2-user/e/trial/code5/products_details.py')
time.sleep(10)
print("===========      created products_details.csv")
print(datetime.datetime.now())


# deleting if exits cleaning_products_details.csv
if os.path.exists('/home/ec2-user/e/trial/code5/cleaned_product_details_urls.csv'):
    os.remove('/home/ec2-user/e/trial/code5/cleaned_product_details_urls.csv')
    print("xxxxxxxxxxx           cleaned_product_details_urls.csv removed successfully")

# time.sleep(15)

# step 5 , cleaning_products_details.py
os.system('python3 /home/ec2-user/e/trial/code5/cleaning_products_details.py')
time.sleep(10)
print("===========      created cleaning_products_details.csv")
print(datetime.datetime.now())


# step 6 , joining.py
os.system('python3 /home/ec2-user/e/trial/code5/joining.py')
time.sleep(15)
print("===========      created joining.csv")
print(datetime.datetime.now())


# ======================================== email =========================

# mail 1
time.sleep(5)
os.system('python3 /home/ec2-user/e/trial/code5/em1.py')
print("===========      email-one   1  successful")
print(datetime.datetime.now())

