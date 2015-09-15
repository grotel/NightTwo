
# coding: utf-8

# In[ ]:




# # Day 2 - Parsing a comma delimited file

# In[5]:

import csv
f = open('/Users/grotel/Desktop/FL_insurance_sample.csv','RU')
csv_f = csv.reader(f)

for row in csv_f:
     print row


# In[ ]:



