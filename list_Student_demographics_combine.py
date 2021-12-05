import os
import csv

state_list_final = []
state_list = []
outfile = open("./data/table_US_combine.csv", "a", newline='')
writer = csv.writer(outfile)

if os.path.isfile('./data/table_race.csv'):
    print("File exist")
    f = open('./data/table_race.csv', "r")
    line = f.readline()
    line = f.readline()
    org_schoolID = ""
    header_line = "School ID, White, Black, Hispanic, Indian, Hawaiian, Asia, Two_or_more_races, Low_in_come, Male, Female"
    writer.writerow(header_line.split(','))

    v_line = ["id", "Wh", "Bl", "Hi", "In", "Ha", "As", "Tw", "Lo", "Ma", "Fe"]
    v_line_value_org = ["", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"]
    v_line_value = v_line_value_org
    while line:
        line_element = line.replace("\n", "").split(',')
        if line_element[0] == org_schoolID:
            #if else condition
            if "White" in line_element[1]:
                v_line_value[1] = line_element[2]
            elif "Black" in line_element[1]:
                v_line_value[2] = line_element[2]
            elif "Hispanic" in line_element[1]:
                v_line_value[3] = line_element[2]
            elif "American Indian" in line_element[1]:
                v_line_value[4] = line_element[2]
            elif "Hawaiian Native" in line_element[1]:
                v_line_value[5] = line_element[2]
            elif "Asian" in line_element[1]:
                v_line_value[6] = line_element[2]
            elif "Two or more races" in line_element[1]:
                v_line_value[7] = line_element[2]
            elif "Lowincome" in line_element[1]:
                v_line_value[8] = line_element[2]
            elif "Male" in line_element[1]:
                v_line_value[9] = line_element[2]
            elif "Female" in line_element[1]:
                v_line_value[10] = line_element[2]
        else:
            if org_schoolID == '':
                org_schoolID = line_element[0]
                v_line_value = v_line_value_org
                v_line_value[0] = org_schoolID
            else:
                writer.writerow(v_line_value)
                org_schoolID = line_element[0]
                v_line_value = v_line_value_org
                v_line_value[0] = org_schoolID
                for k in range(1, 11):
                    v_line_value[k] = -1
            # if else condition
            if "White" in line_element[1]:
                v_line_value[1] = line_element[2]
            elif "Black" in line_element[1]:
                v_line_value[2] = line_element[2]
            elif "Hispanic" in line_element[1]:
                v_line_value[3] = line_element[2]
            elif "American Indian" in line_element[1]:
                v_line_value[4] = line_element[2]
            elif "Hawaiian Native" in line_element[1]:
                v_line_value[5] = line_element[2]
            elif "Asian" in line_element[1]:
                v_line_value[6] = line_element[2]
            elif "Two or more races" in line_element[1]:
                v_line_value[7] = line_element[2]
            elif "Lowincome" in line_element[1]:
                v_line_value[8] = line_element[2]
            elif "Male" in line_element[1]:
                v_line_value[9] = line_element[2]
            elif "Female" in line_element[1]:
                v_line_value[10] = line_element[2]
        line = f.readline()
writer.writerow(v_line_value)
outfile.close()