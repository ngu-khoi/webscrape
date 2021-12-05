import os
import csv

state_list_final = []
state_list = []
outfile = open("./data/table_US_combine_final.csv", "a", newline='')
writer = csv.writer(outfile)
#f = open('./data/table_school_US_new.csv', "r")
#outfile = open("./data/table_US_combine.csv", "a", newline='')

if os.path.isfile('./data/table_US_combine.csv'):
    print("File exist")
    f_main = open('./data/table_school_US_new.csv', "r")
    line_main = f_main.readline()
    line_main = f_main.readline()
    org_schoolID = ""
    header_line = "State Order,State,School Link,Score,Rate,School,Address,City,State,Zip Code,Type, White, Black, Hispanic, Indian, Hawaiian, Asia, Two_or_more_races, Low_in_come, Male, Female"
    writer.writerow(header_line.split(','))

    v_line = ["id", "Wh", "Bl", "Hi", "In", "Ha", "As", "Tw", "Lo", "Ma", "Fe"]
    v_line_value_org = ["", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"]
    v_line_value = v_line_value_org
    list_of_cells = []
    while line_main:
        line_main_details = line_main.split(',')
        f = open('./data/table_US_combine.csv', "r")
        line = f.readline()
        line = f.readline()
        while line:
            flag_found = 0
            line_element = line.replace("\n", "").replace("\n", "").split(',')
            if line_main_details[2] == line_element[0]:
                #print(line_element[0])
                for k in line_main.split(','):
                    list_of_cells.append(k.strip())
                for k in line.split(','):
                    if len(k) < 20:
                        list_of_cells.append(k.strip())
                writer.writerow(list_of_cells)
                list_of_cells = []
                line_main = f_main.readline()
                flag_found = 1
                break
            else:
                line = f.readline()
        if flag_found == 0:
            #print(line_element[0])
            for k in line_main.split(','):
                list_of_cells.append(k.strip())
            for counter in range(1, 11):
                list_of_cells.append(-1)
            writer.writerow(list_of_cells)
            list_of_cells = []
            line_main = f_main.readline()
print("Done")
outfile.close()