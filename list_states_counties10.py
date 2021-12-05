import os
import csv

state_list_final = []
state_list = []

if os.path.isfile('./data/uszips.csv'):
    print("File exist")
    f = open('uszips.csv', "r")
    line = f.readline()
    n = 1
    while line:
        line_element = line.split(',')
        statecitity = line_element[4] + ',' + line_element[11]
        state_list.append(statecitity)
        if n > 10000:
            state_list_final = list(dict.fromkeys(state_list_final + state_list))
            print(state_list)
            print(state_list_final)
            n = 1
            state_list = []
        else:
            n = n + 1
        line = f.readline()
    state_list_final = list(dict.fromkeys(state_list_final + state_list))
    print(state_list)
    print(state_list_final)
    f.close()
    state_list_final.sort()
    print(state_list_final)
result_file = open('./data/List_State_Counties.csv', "w")

for element in state_list_final:
    print(element, file = result_file)
result_file.close()