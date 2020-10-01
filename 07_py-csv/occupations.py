# May Hathaway (with Erin Lee and Victoria Gao — Team Burgers)
# SoftDev
# K07 — StI/O: Divine your Destiny! Returning an occupation based on the percentage.
# 2020-10-02

#Our approach: for this assignment, we created a dictionary with intervals as our keys.
#We generated a random number from 0 to 99.8, and based on which interval it lied in, we returned the occupation corresponding to that interval.
#We created our interval so that if an occupation had 5 percent chance, the next occupation would start at the previous interval + 5.
#If the random number was just greater than an interval as you iterated through the dictionary, then you would return the occupation with that interval.

import csv
import random

occupations = open("occupations.csv", "r")
data = occupations.readlines()
occupations.close()
current_total = 0
percent_dict = {}
for i in range(1, len(data)-1):
    if data[i][0] == '"':
        data_set = data[i].split('",')
        title = data_set[0][1:]
    else:
        data_set = data[i].split(",")
        title = data_set[0]
    percent = float(data_set[1])
    percent_dict[round(percent + current_total, 1)] = title
    current_total = current_total + percent

print(percent_dict)

def return_occupation():
    rand_num = random.randrange(0,998) / 10.0
    for percent in percent_dict:
        if rand_num <= percent:
            return(percent_dict[percent])

print(return_occupation())
