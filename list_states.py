import os
import csv

state_list_final = []
state_list = []

if os.path.isfile('./data/uszips.csv'):
    print("File exist")
    f = open('./data/uszips.csv', "r")
    line = f.readline()
    n = 1
    while line:
        line_element = line.split(',')
        state_list.append(line_element[4])
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
