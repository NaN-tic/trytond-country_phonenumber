#!/usr/bin/python
# create phonenumber.csv file from phonenumber
import csv
from phonenumbers import COUNTRY_CODE_TO_REGION_CODE

with open('phonenumber.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
    for prefix, countries in COUNTRY_CODE_TO_REGION_CODE.items():
        for country in countries:
            filewriter.writerow([country, prefix])
