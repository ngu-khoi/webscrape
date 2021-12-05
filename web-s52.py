import csv
import os.path
from selenium import webdriver
from bs4 import BeautifulSoup

def insert_comma(string, index):
    return string[:index] + ',' + string[index:]

def get_all_state_school(statename, next_page):
    global driver
    # https://www.greatschools.org/virginia/schools/?page=1&sort=name&view=table&limit=1000&offset=100
    str1 = 'https://www.greatschools.org/'
    str2 = '/schools/?page='
    str3 = '&sort=name&view=table&limit=1000&offset='
    driver = webdriver.Chrome("/usr/bin/chromium/chromedriver.exe")
    # schoolName=[] #List to store name of the product
    n = 30
    for counter in range(next_page, n):
        offset_var = (counter - 1) * 1000
        driver.get(str1 + statename + str2 + str(counter) + str3 + str(offset_var))
        content = driver.page_source
        #print(content)
        soup = BeautifulSoup(content, "html.parser")
        table = soup.find('table')
        # list_of_rows = []
        if (table is not None):
            state_order = offset_var
            for row in table.findAll('tr'):
                list_of_cells = []
                list_of_cells.append(state_order)
                state_order = state_order + 1
                list_of_cells.append(statename)
                for cell in row.findAll(["td"]):
                    if ' Summary Rating provides an overall snapshot of school quality' in cell.text:
                        text0 = cell.contents[1].contents[0].attrs.get('href')
                        list_of_cells.append(text0)
                        text1 = cell.contents[0].contents[0].contents[0].contents[1].text
                        if 'Currently unrated' in text1:
                            ratevalue = '-1'
                        else:
                            ratevalue_fullrate = cell.contents[0].contents[0].contents[0].contents[0].text.split('/')
                            ratevalue = ratevalue_fullrate[0]
                        list_of_cells.append(ratevalue)
                        list_of_cells.append(text1)
                        text2 = cell.contents[1].contents[0].text
                        list_of_cells.append(text2)
                        #print(text2)
                        if 'award' in cell.text:
                            if 'Homes for sale' in cell.contents[1].contents[3].text:
                                text3 = cell.contents[1].contents[2].text
                            else:
                                text3 = cell.contents[1].contents[3].text
                        else:
                            if 'Homes for sale' in cell.contents[1].contents[2].text:
                                text3 = cell.contents[1].contents[1].text
                            else:
                                text3 = cell.contents[1].contents[2].text
                        for x in text3.split(','):
                            list_of_cells.append(x.strip())
                    else:
                        list_of_cells.append(cell.text)
                # list_of_rows.append(list_of_cells)
                if len(list_of_cells) > 3:
                    writer.writerow(list_of_cells)
        else:
            break

def last_state_infile():
    global last_state, last_state_order, next_page
    # read a text file as a list of lines
    # find the last line, change to a file you have
    fileHandle = open('table_school_US.csv', "r")
    last_line = list(fileHandle)[-1]
    last_line_element = last_line.split(',')
    last_state_order = last_line_element[0].strip()
    last_state = last_line_element[1]
    last_page = int(last_state_order) // 1000
    next_page = last_page + 1
    print(last_state)
    return last_state

def last_order_infile():
    global last_state, last_state_order
    # read a text file as a list of lines
    # find the last line, change to a file you have
    fileHandle = open('table_school_US.csv', "r")
    last_line = list(fileHandle)[-1]
    last_line_element = last_line.split(',')
    last_state_order = last_line_element[0].strip()
    print(str(last_state_order))
    return last_state_order

# statename_list = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new-hampshire", "new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west-virginia", "wisconsin", "wyoming"]
statename_list = ["new-jersey", "new-mexico", "new-york", "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island", "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "washington", "west-virginia", "wisconsin"]


def main_function():
    global writer, next_page
    if os.path.isfile('table_school_US.csv'):
        print("File exist")
        last_state_infile()
        outfile = open("table_school_US.csv", "a", newline='')
        writer = csv.writer(outfile)
        next_state = 0
        normal_run = 0
        for statename in statename_list:
            if normal_run == 0:
                if statename != last_state:
                    continue
                else:
                    if int(last_order_infile()) % 1000 == 0 and next_state == 0:
                        get_all_state_school(statename, next_page)
                        if int(last_order_infile()) % 1000 == 0:
                            next_page = next_page + 1
                        else:
                            normal_run = 1
                    else:
                        normal_run = 1
                        continue
            else:
                next_page = 1
                get_all_state_school(statename, next_page)

    else:
        print("File not exist")
        # outfile = open("table_school_"+statename+"_gradeLevels_"+gradeLevels+".csv", "a", newline='')
        outfile = open("table_school_US.csv", "a", newline='')
        writer = csv.writer(outfile)
        list_of_cellshead = []
        headertext = 'State Order, State, School Link, Score, Rate, School, Address, City, State, Zip Code, Type ,Grades ,Total students enrolled ,Students per ' \
                     'teacher ,Reviews ,District '
        for k in headertext.split(','):
            list_of_cellshead.append(k.strip())
        writer.writerow(list_of_cellshead)
        for statename in statename_list:
            get_all_state_school(statename, 1)

main_function()




