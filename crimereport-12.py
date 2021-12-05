import re
import string
import time
import json
import a as a
import csv
import os.path
import driver as driver
import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def insert_comma(string, index):
    return string[:index] + ',' + string[index:]

def get_all_state_school(police_department):
    global driver
    # https://www.greatschools.org/virginia/schools/?page=1&sort=name&view=table&limit=1000&offset=100
    str1 = 'https://www.crimemapping.com/map/agency/'
    str2 = police_department
    #str3 = '&sort=name&view=table&limit=1000&offset='
    driver = webdriver.Chrome("/usr/bin/chromium/chromedriver.exe")
    driver.maximize_window()

    url = str1 + str2
    driver.get(url)
    sleep(3)
    report_click = driver.find_element_by_id('displayReports')
    content1 = report_click.click()
    sleep(12)
    content = driver.page_source
    print(content)
    soup = BeautifulSoup(content, "html.parser")
    sleep(3)
    print(driver.page_source)
    #table = soup.find('table')
    dev1 = soup.select('div#divReportCrimeIncidents')
    item_count = soup.select('span#itemsCount')
    item_count_str = soup.find('span', {'class': 'itemsCount'})
    if (item_count_str is not None):
        item_count = int(item_count_str.text[0:3].strip())
        loop_count = item_count // 15
    #print(dev1[0])
    round = 0
    for i in range(1, loop_count + 2):
        print(dev1[0].contents[1].contents[1].contents[0])
        root = ET.fromstring(str(dev1[0].contents[1].contents[1].contents[0].contents[1]))
        for child in root.findall('tr'):
            list_of_cells = []
            list_of_cells.append(str2)
            for child1 in child.findall('td'):
                list_of_cells.append(str(child1.text).strip())
                print(child1.text)
            writer.writerow(list_of_cells)
        next_click = driver.find_element_by_link_text('arrow-e')
        content1 = next_click.click()
        sleep(5)
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        sleep(3)
        dev1 = soup.select('div#divReportCrimeIncidents')


# statename_list = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west-virginia", "wisconsin", "wyoming"]
police_department_list = ["329", "15"]


def main_function():
    global writer, next_page
    if os.path.isfile('crime_report_US.csv'):
        print("File exist")
        outfile = open("crime_report_US.csv", "a", newline='')
        writer = csv.writer(outfile)
        for police_department in police_department_list:
            get_all_state_school(police_department)

    else:
        print("File not exist")
        # outfile = open("table_school_"+statename+"_gradeLevels_"+gradeLevels+".csv", "a", newline='')
        outfile = open("crime_report_US.csv", "a", newline='')
        writer = csv.writer(outfile)
        list_of_cellshead = []
        headertext = 'Police Department, Map, Type, Description, Incident #, Location, Agency, Date'
        for k in headertext.split(','):
            list_of_cellshead.append(k.strip())
        writer.writerow(list_of_cellshead)
        for police_department in police_department_list:
            get_all_state_school(police_department)

main_function()




