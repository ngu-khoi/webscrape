import os
import re
import a as a
import csv
import driver as driver
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


def insert_comma(string, index):
    return string[:index] + ',' + string[index:]


# schoolName=[] #List to store name of the product

def get_student_demographics(schoolId):
    str1 = 'https://www.greatschools.org' + schoolId
    driver.get(str1)
    content = driver.page_source
    # print(content)
    soup = BeautifulSoup(content, "html.parser")
    student = soup.select('div#Students')
    # list_of_rows = []
    if (student is not None):
        # race = student[0].findAll('div',{"class": "legend-separator js-highlightPieChart clearfix"})
        list_of_races = []
        list_of_percent = []
        try:
            for row in student[0].findAll('div', {"class": "legend-title", "style": "float:left;"}):
                list_of_races.append(row.text)
            for row in student[0].findAll('div', {"class": "legend-title", "style": "float: right"}):
                list_of_percent.append(row.text)
            length = len(list_of_races)
            for i in range(length):
                list_of_cells = []
                list_of_cells.append(schoolId)
                list_of_cells.append(list_of_races[i])
                list_of_cells.append(list_of_percent[i])
                writer.writerow(list_of_cells)
        except IndexError:
            print('No student race data')

    low_income = soup.select('div#students-participating-in-free-or-reduced-price-lunch-program')
    if (low_income is not None):
        try:
            list_of_cells = []
            list_of_cells.append(schoolId)
            low_income_percent = low_income[0].find('text', {"class": "highcharts-title"})
            list_of_cells.append('Lowincome')
            list_of_cells.append(low_income_percent.text)
            writer.writerow(list_of_cells)
        except IndexError:
            print('No Low income race data')

    gender = soup.select('div#gender')
    if (gender is not None):
        try:
            list_of_cells = []
            list_of_percent = []
            for row in student[0].findAll('div', {"class": "open-sans"}):
                list_of_percent.append(row.text)
            list_of_cells.append(schoolId)
            list_of_cells.append('Male')
            list_of_cells.append(list_of_percent[0])
            writer.writerow(list_of_cells)
            list_of_cells = []
            list_of_cells.append(schoolId)
            list_of_cells.append('Female')
            list_of_cells.append(list_of_percent[1])
            writer.writerow(list_of_cells)
        except IndexError:
            print('No GENDER data')


def main():
    global writer
    if os.path.isfile("./data/table_race.csv"):
        print("File exist")
        fileHandle = open("./data/table_race.csv", "r")
        last_line = list(fileHandle)[-1]
        last_line_element = last_line.split(',')
        last_school_infile = last_line_element[0].strip()
        print(str(last_school_infile))
        outfile = open("./data/table_race.csv", "a", newline='')
        writer = csv.writer(outfile)
    else:
        print("File not exist")
        outfile = open("./data/table_race.csv", "a", newline='')
        writer = csv.writer(outfile)
        headertext = 'School ID, Race, Percent '
        list_of_cellshead = []
        for k in headertext.split(','):
            list_of_cellshead.append(k.strip())
        writer.writerow(list_of_cellshead)
        last_school_infile = 'School ID'
    line = f.readline()
    flag_value = 0
    while line:
        l = line.split(',')
        print(l[2])
        init_school = l[2]
        if (flag_value == 0):
            if (l[2] != last_school_infile):
                if (last_school_infile == 'School ID'):
                    last_school_infile = init_school
                    flag_value = 1
                else:
                    line = f.readline()
                    continue
            else:
                line = f.readline()
                l = line.split(',')
                flag_value = 1
        get_student_demographics(l[2])
        line = f.readline()
    f.close()



for i in range(1, 10000):
    driver = webdriver.Chrome("/usr/bin/chromium/chromedriver.exe")
    try:
        f = open('./data/table_school_US_new.csv', "r")
        if os.path.isfile("./data/table_race.csv"):
            fileHandle = open("./data/table_race.csv", "r")
            main()
    except:
        print('Restarting!')
        f.close()
        if os.path.isfile("./data/table_raceUSA.csv"):
            fileHandle.close()
        sleep(2)
        continue
    else:
        break