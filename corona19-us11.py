import re
import time
import json
import a as a
import csv
import os.path
import driver as driver
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime

def insert_comma(string, index):
    return string[:index] + ',' + string[index:]

def get_country_corona(country):
    global driver
    # https://www.greatschools.org/virginia/schools/?page=1&sort=name&view=table&limit=1000&offset=100
    str1 = 'https://www.worldometers.info/coronavirus/country/'
    country = country + '/'
    driver = webdriver.Chrome("/usr/bin/chromium/chromedriver.exe")
    # schoolName=[] #List to store name of the product
    n = 2
    for counter in range(1, n):
        offset_var = (counter - 1) * 1000
        driver.get(str1 + country)
        content = driver.page_source
        #print(content)
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find('table')
        table = soup.find('table', id="usa_table_countries_yesterday")
        # list_of_rows = []
        if (table is not None):
            state_order = offset_var
            for row in table.findAll('tr'):
                list_of_cells = []
                for cell in row.findAll(["td"]):
                    text1 = cell.text.replace('\n', ' ')
                    list_of_cells.append(text1)
                writer.writerow(list_of_cells)
        else:
            break

# statename_list = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west-virginia", "wisconsin", "wyoming"]
country_list = ["us"]


def main_function():
    global writer
    print("File not exist")
    #today = str(date.today())
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterdaystr = str(yesterday)
    #outfile = open("./data/country_US.csv", "a", newline='')
    list_of_cellshead = []
    headertext = 'USA State, Total Cases, New Cases, Total Deaths, New Deaths, Active Cases, Tot Cases / 1 M pop, Deaths / 1 M pop, Total Tests, Test / 1 M pop '

    for country in country_list:
        outfile = open("./data/country_" + country + "_" + yesterdaystr + ".csv", "w", newline='')
        writer = csv.writer(outfile)
        for k in headertext.split(','):
            list_of_cellshead.append(k.strip())
        writer.writerow(list_of_cellshead)
        get_country_corona(country)
        outfile.close()

while True:
    main_function()
    time.sleep(86400)


