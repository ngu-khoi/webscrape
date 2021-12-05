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
    header_line = "School ID, White, Black, Hispanic, American Indian/Alaska Native, Hawaiian Native/Pacific Islander, Asian, Asian or Asian/Pacific Islander, Filipino, Pacific Islander, Asian or Pacific Islander, Native American or Native Alaskan, Native Hawaiian or Pacific Islander, African-American, American Indian/Alaskan Native, American Indian, White not Hispanic, Black not Hispanic, Native Hawaiian or Other Pacific Islander, Asian/Pacific Islander, Two_or_more_races, Low Income, Male, Female"
    writer.writerow(header_line.split(','))

   # v_line = ["id", "Wh", "Bl", "Hi", "In", "Ha", "As", "Tw", "Lo", "Ma", "Fe"]
    v_line_value_org = ["", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"]
    v_line_value = v_line_value_org
    while line:
        line_element = line.replace("\n", "").split(',')
        if line_element[0] == org_schoolID:
            #if else condition
            if "White" == line_element[1]:
                v_line_value[1] = line_element[2]
            elif "Black" == line_element[1]:
                v_line_value[2] = line_element[2]
            elif "Hispanic" == line_element[1]:
                v_line_value[3] = line_element[2]
            elif "American Indian/Alaska Native" == line_element[1]:
                v_line_value[4] = line_element[2]
            elif "Hawaiian Native/Pacific Islander" == line_element[1]:
                v_line_value[5] = line_element[2]
            elif "Asian" == line_element[1]:
                v_line_value[6] = line_element[2]
            elif "Asian or Asian/Pacific Islander" == line_element[1]:
                v_line_value[7] = line_element[2]
            elif "Filipino" == line_element[1]:
                v_line_value[8] = line_element[2]
            elif "Pacific Islander" == line_element[1]:
                v_line_value[9] = line_element[2]
            elif "Asian or Pacific Islander" == line_element[1]:
                v_line_value[10] = line_element[2]
            elif "Native American or Native Alaskan" == line_element[1]:
                v_line_value[11] = line_element[2]
            elif "Native Hawaiian or Pacific Islander" == line_element[1]:
                v_line_value[12] = line_element[2]
            elif "African-American" == line_element[1]:
                v_line_value[13] = line_element[2]
            elif "American Indian/Alaskan Native" == line_element[1]:
                v_line_value[14] = line_element[2]
            elif "American Indian" == line_element[1]:
                v_line_value[15] = line_element[2]
            elif "White, not Hispanic" == line_element[1]:
                v_line_value[16] = line_element[2]
            elif "Black, not Hispanic" == line_element[1]:
                v_line_value[17] = line_element[2]
            elif "Native Hawaiian or Other Pacific Islander" == line_element[1]:
                v_line_value[18] = line_element[2]
            elif "Asian/Pacific Islander" == line_element[1]:
                v_line_value[19] = line_element[2]
            elif "Two or more races" == line_element[1]:
                v_line_value[20] = line_element[2]
            elif "Lowincome" == line_element[1]:
                v_line_value[21] = line_element[2]
            elif "Male" == line_element[1]:
                v_line_value[22] = line_element[2]
            elif "Female" == line_element[1]:
                v_line_value[23] = line_element[2]
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
                for k in range(1, 24):
                    v_line_value[k] = -1
            # if else condition
            #if else condition
            if "White" == line_element[1]:
                v_line_value[1] = line_element[2]
            elif "Black" == line_element[1]:
                v_line_value[2] = line_element[2]
            elif "Hispanic" == line_element[1]:
                v_line_value[3] = line_element[2]
            elif "American Indian/Alaska Native" == line_element[1]:
                v_line_value[4] = line_element[2]
            elif "Hawaiian Native/Pacific Islander" == line_element[1]:
                v_line_value[5] = line_element[2]
            elif "Asian" == line_element[1]:
                v_line_value[6] = line_element[2]
            elif "Asian or Asian/Pacific Islander" == line_element[1]:
                v_line_value[7] = line_element[2]
            elif "Filipino" == line_element[1]:
                v_line_value[8] = line_element[2]
            elif "Pacific Islander" == line_element[1]:
                v_line_value[9] = line_element[2]
            elif "Asian or Pacific Islander" == line_element[1]:
                v_line_value[10] = line_element[2]
            elif "Native American or Native Alaskan" == line_element[1]:
                v_line_value[11] = line_element[2]
            elif "Native Hawaiian or Pacific Islander" == line_element[1]:
                v_line_value[12] = line_element[2]
            elif "African-American" == line_element[1]:
                v_line_value[13] = line_element[2]
            elif "American Indian/Alaskan Native" == line_element[1]:
                v_line_value[14] = line_element[2]
            elif "American Indian" == line_element[1]:
                v_line_value[15] = line_element[2]
            elif "White, not Hispanic" == line_element[1]:
                v_line_value[16] = line_element[2]
            elif "Black, not Hispanic" == line_element[1]:
                v_line_value[17] = line_element[2]
            elif "Native Hawaiian or Other Pacific Islander" == line_element[1]:
                v_line_value[18] = line_element[2]
            elif "Asian/Pacific Islander" == line_element[1]:
                v_line_value[19] = line_element[2]
            elif "Two or more races" == line_element[1]:
                v_line_value[20] = line_element[2]
            elif "Lowincome" == line_element[1]:
                v_line_value[21] = line_element[2]
            elif "Male" == line_element[1]:
                v_line_value[22] = line_element[2]
            elif "Female" == line_element[1]:
                v_line_value[23] = line_element[2]
        line = f.readline()
writer.writerow(v_line_value)
outfile.close()