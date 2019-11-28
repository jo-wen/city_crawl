#!/usr/bin/env python3

"""
This script doesn't work as is (and is written dumbly), but has all the pieces I used to organize the data.
parsing a csv file from https://simplemaps.com/data/us-cities
checks if each city has:
    1) a .gov site
    2) a .us site
    3) a .com site
    4) includes http and https entries
    5) includes www entries as well
for now this is just a giant text file to be gone through
"""

import csv
import urllib.request

csv_file = 'uscities.csv'
f_city = 'city_urls'
f_checked = 'checked_cities'

def get_all_cities():
    all_cities = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
        	all_cities.append(row[0])
        csvfile.close()
    return all_cities

def create_urls():
    f_cities = open(f_city, 'a+')
    for city in get_all_cities():
        check_gov = "http://{}.gov".format(city.lower().replace(" ", ""))
        check_us = "http://{}.us".format(city.lower().replace(" ", ""))
        check_com = "http://{}.com".format(city.lower().replace(" ", ""))
        check_gov_https = "https://{}.gov".format(city.lower().replace(" ", ""))
        check_us_https = "https://{}.us".format(city.lower().replace(" ", ""))
        check_com_https = "https://{}.com".format(city.lower().replace(" ", ""))
        while f_cities:
            f_cities.write(' '.join(map(str, check_gov)))
            f_cities.write(' '.join(map(str, check_us)))
            f_cities.write(' '.join(map(str, check_com)))
            f_cities.write(' '.join(map(str, check_gov_https)))
            f_cities.write(' '.join(map(str, check_us_https)))
            f_cities.write(' '.join(map(str, check_com_https)))
    f_cities.close()


csv_file = 'uscities.csv'
f_city = 'city_urls'
f_checked = 'checked_cities'
all_cities = []
with open(csv_file) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
    	all_cities.append(row[0])

f_cities = open(f_city, 'a')
for city in all_cities:
    check_gov = "http://{}.gov".format(city.lower().replace(" ", ""))
    check_us = "http://{}.us".format(city.lower().replace(" ", ""))
    check_com = "http://{}.com".format(city.lower().replace(" ", ""))
    check_gov_https = "https://{}.gov".format(city.lower().replace(" ", ""))
    check_us_https = "https://{}.us".format(city.lower().replace(" ", ""))
    check_com_https = "https://{}.com".format(city.lower().replace(" ", ""))
    f_cities.write(check_gov + '\n')
    f_cities.write(check_us + '\n')
    f_cities.write(check_com + '\n')
    f_cities.write(check_gov_https + '\n')
    f_cities.write(check_us_https + '\n')
    f_cities.write(check_com_https + '\n')

# with www
for city in all_cities:
    check_gov = "http://www.{}.gov".format(city.lower().replace(" ", ""))
    check_us = "http://www.{}.us".format(city.lower().replace(" ", ""))
    check_com = "http://www.{}.com".format(city.lower().replace(" ", ""))
    check_gov_https = "https://www.{}.gov".format(city.lower().replace(" ", ""))
    check_us_https = "https://www.{}.us".format(city.lower().replace(" ", ""))
    check_com_https = "https://www.{}.com".format(city.lower().replace(" ", ""))
    f_cities.write(check_gov + '\n')
    f_cities.write(check_us + '\n')
    f_cities.write(check_com + '\n')
    f_cities.write(check_gov_https + '\n')
    f_cities.write(check_us_https + '\n')
    f_cities.write(check_com_https + '\n')
f_cities.close()



gov = urllib.request.urlopen(check_gov)
us = urllib.request.urlopen(check_us)
com = urllib.request.urlopen(check_com)
gov_https = urllib.request.urlopen(check_gov_https)
us_https = urllib.request.urlopen(check_us_https)
com_https = urllib.request.urlopen(check_com_https)
        gov_status = city, gov.url, gov.status, gov.reason
        us_status = city, us.url, us.status, us.reason
        com_status = city, com.url, com.status, com.reason
        while f_cities:

        f_cities.close()
