import os
import csv
import re

def insert_zero(string, index):
    return string[:index+2] + '0' + string[index+2:]

state_list_final = []
state_list = []

outfile = open("./data/table_school_US_new.csv", "w", newline='')
writer = csv.writer(outfile)

if os.path.isfile('./data/table_school_US.csv'):
    print("File exist")
    f = open('./data/table_school_US.csv', "r")
    line = f.readline()
    while line:
        list_of_cells = []
        n = 1
        l = line.split(',')
        if not l[9].isnumeric() and l[11].isnumeric():
            for k in line.split(','):
                if n != 8 and n != 9 and n < 12:
                    list_of_cells.append(k.strip())
                n = n + 1
        elif not l[9].isnumeric() and l[10].isnumeric():
            for k in line.split(','):
                if n != 8 and n < 12:
                    list_of_cells.append(k.strip())
                n = n + 1
        elif not l[9].isnumeric() and l[12].isnumeric():
            for k in line.split(','):
                if n != 7 and n != 8 and n != 9 and n < 12:
                    list_of_cells.append(k.strip())
                n = n + 1
        else:
            for k in line.split(','):
                if n < 12:
                    list_of_cells.append(k.strip())
                n = n + 1
        #print(list_of_cells)
        writer.writerow(list_of_cells)
        n = 1
        line = f.readline()
        #print(line)
    f.close()
