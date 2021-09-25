# https://www.geeksforgeeks.org/how-to-run-multiple-python-file-in-a-folder-one-after-another/

import os
import time
import datetime
date_time = format(datetime.date.today())

# ======================level2================================
# deleting if exits ll2.csv
if os.path.exists('/home/ec2-user/ll2.csv'):
    os.remove('/home/ec2-user/ll2.csv')
    print("xxxxxxxxxxx           ll2 removed successfully")

# level 2
os.system('python3 /home/ec2-user/e/trial/link/ll2.py')
time.sleep(10)
print("===========      created ll2.csv")
print(datetime.datetime.now())

# deleting if exits cll2.csv
if os.path.exists('/home/ec2-user/e/trial/clean/cll2.csv'):
    os.remove('/home/ec2-user/e/trial/clean/cll2.csv')
    print("xxxxxxxxxxx           cll2.csv removed successfully")

os.system('python3 /home/ec2-user/e/trial/cdata/cll2.py')
time.sleep(10)
print("===========      created cll2.csv")
print(datetime.datetime.now())

# ======================level3================================
# deleting if exits ll3.csv
if os.path.exists('/home/ec2-user/ll3.csv'):
    os.remove('/home/ec2-user/ll3.csv')
    print("xxxxxxxxxxx           ll3.csv removed successfully")

# level 3
os.system('python3 /home/ec2-user/e/trial/link/ll3.py')
time.sleep(10)
print("===========      created ll3.csv")
print(datetime.datetime.now())

# deleting if exits cll3.csv
if os.path.exists('/home/ec2-user/e/trial/clean/cll3.csv'):
    os.remove('/home/ec2-user/e/trial/clean/cll3.csv')
    print("xxxxxxxxxxx           cll3.csv removed successfully")

os.system('python3 /home/ec2-user/e/trial/cdata/cll3.py')
time.sleep(10)
print("===========      created cll3.csv")
print(datetime.datetime.now())

# ======================level4================================
# deleting if exits ll4.csv
if os.path.exists('/home/ec2-user/ll4.csv'):
    os.remove('/home/ec2-user/ll4.csv')
    print("xxxxxxxxxxx           ll4.csv removed successfully")

# level 4
os.system('python3 /home/ec2-user/e/trial/link/ll4.py')
time.sleep(10)
print("===========      created ll4.csv")
print(datetime.datetime.now())

# deleting if exits cll4.csv
if os.path.exists('/home/ec2-user/e/trial/clean/cll4.csv'):
    os.remove('/home/ec2-user/e/trial/clean/cll4.csv')
    print("xxxxxxxxxxx           cll4.csv removed successfully")

os.system('python3 /home/ec2-user/e/trial/cdata/cll4.py')
time.sleep(10)
print("===========      created cll4.csv")
print(datetime.datetime.now())

# ======================level5================================
# deleting if exits ll5.csv
if os.path.exists('/home/ec2-user/ll5.csv'):
    os.remove('/home/ec2-user/ll5.csv')
    print("xxxxxxxxxxx           ll5.csv removed successfully")

# level 5
os.system('python3 /home/ec2-user/e/trial/link/ll5.py')
time.sleep(10)
print("===========      created ll5.csv")
print(datetime.datetime.now())

# deleting if exits cll5.csv
if os.path.exists('/home/ec2-user/e/trial/clean/cll5.csv'):
    os.remove('/home/ec2-user/e/trial/clean/cll5.csv')
    print("xxxxxxxxxxx           cll5.csv removed successfully")

os.system('python3 /home/ec2-user/e/trial/cdata/cll5.py')
time.sleep(10)
print("===========      created cll5.csv")
print(datetime.datetime.now())

# ======================level6================================
# deleting if exits ll6.csv
if os.path.exists('/home/ec2-user/ll6.csv'):
    os.remove('/home/ec2-user/ll6.csv')
    print("xxxxxxxxxxx           ll6.csv removed successfully")

# level 6
os.system('python3 /home/ec2-user/e/trial/link/ll6.py')
time.sleep(10)
print("===========      created ll6.csv")
print(datetime.datetime.now())

# deleting if exits cll6.csv
if os.path.exists('/home/ec2-user/e/trial/clean/cll6.csv'):
    os.remove('/home/ec2-user/e/trial/clean/cll6.csv')
    print("xxxxxxxxxxx           cll6.csv removed successfully")

os.system('python3 /home/ec2-user/e/trial/cdata/cll6.py')
time.sleep(10)
print("===========      created cll6.csv")
print(datetime.datetime.now())

#deleting if exits all_level_urls.csv
if os.path.exists('/home/ec2-user/e/trial/clean/all_level_urls.csv'):
    os.remove('/home/ec2-user/e/trial/clean/all_level_urls.csv')
    print("xxxxxxxxxxx           all_level_urls.csv removed successfully")

# time.sleep(15)

# step 1 , all_level_urls.py
os.system('python3 /home/ec2-user/e/trial/clean/all_level_urls.py')
time.sleep(10)
print("===========      created all_level_urls.csv")
print(datetime.datetime.now())


# ============================== break ==========================

# time.sleep(60)

# ============================= break =====================
#
#
#
# # deleting if exits c100items.csv
# if os.path.exists('/home/ec2-user/onec100items.csv'):
#     os.remove('/home/ec2-user/onec100items.csv')
#     print("xxxxxxxxxxx           c100items.csv removed successfully")
# # time.sleep(15)
#
# # step 2 , c100items.py
# os.system('python3 /home/ec2-user/e/trial/clean/c100items.py')
# time.sleep(10)
# print("===========      created c100items.csv")
# print(datetime.datetime.now())
#
#
#
# # deleting if exits cleaning_100items.csv
# if os.path.exists('/home/ec2-user/e/trial/clean/cleaned_100items.csv'):
#     os.remove('/home/ec2-user/e/trial/clean/cleaned_100items.csv')
#     print("xxxxxxxxxxx           cleaned_100items.csv removed successfully")
#
# # time.sleep(15)
#
# # step 3 , cleaning_100items.py
# os.system('python3 /home/ec2-user/e/trial/clean/cleaning_100items.py')
# time.sleep(10)
# print("===========      created cleaning_100items.csv")
# print(datetime.datetime.now())
#
#
#
# # deleting if exits products_details_urls.csv
# if os.path.exists('/home/ec2-user/oneproduct_details_urls.csv'):
#     os.remove('/home/ec2-user/oneproduct_details_urls.csv')
#     print("xxxxxxxxxxx           cleaned_product_details_urls.csv removed successfully")
#
# # time.sleep(15)
#
# # step 4 , products_details.py
# os.system('python3 /home/ec2-user/e/trial/clean/products_details.py')
# time.sleep(10)
# print("===========      created products_details.csv")
# print(datetime.datetime.now())
#
#
# # deleting if exits cleaning_products_details.csv
# if os.path.exists('/home/ec2-user/e/trial/clean/cleaned_product_details_urls.csv'):
#     os.remove('/home/ec2-user/e/trial/clean/cleaned_product_details_urls.csv')
#     print("xxxxxxxxxxx           cleaned_product_details_urls.csv removed successfully")
#
# # time.sleep(15)
#
# # step 5 , cleaning_products_details.py
# os.system('python3 /home/ec2-user/e/trial/clean/cleaning_products_details.py')
# time.sleep(10)
# print("===========      created cleaning_products_details.csv")
# print(datetime.datetime.now())
#
#
# # step 6 , joining.py
# os.system('python3 /home/ec2-user/e/trial/clean/joining.py')
# time.sleep(15)
# print("===========      created joining.csv")
# print(datetime.datetime.now())
#
#
# # ======================================== email =========================
#
# # mail 1
# time.sleep(5)
# os.system('python3 /home/ec2-user/e/trial/clean/em1.py')
# print("===========      email-one   1  successful")
# print(datetime.datetime.now())
#
