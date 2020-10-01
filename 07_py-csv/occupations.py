# May Hathaway (with Erin Lee and Victoria Gao — Team Burgers)
# SoftDev
# K07 — StI/O: Divine your Destiny! Returning an occupation based on the percentage.
# 2020-10-02

"""
Our approach: We created a dictionary with an interval's end number as the keys and occupations as the values.
We generated a random number from 0 to 99.8, and based on which interval it lied in, we returned the occupation corresponding to that interval.

-----------------------------------------------
Dictionary:                                     |Intervals:
{6.1: 'Management',                             | [0,6.1)
 11.1:'Business and Financial operations',      | [6.1,11.1)
 ...,                                           |  ...
 93.3: 'Production',                            | [87.2,93.3)
 99.8: 'Transportation and material moving'     | [93.3,99.8)
}

If an occupation has 5% chance, its corresponding dictionary key is the previous occupation's interval end number + 5%.

We used a for loop to iterate through the dictionary:
If the random number is less than a key, return the occupation (dictionary value).
If not, check if the random number is less than the next dictionary key.
"""

import random
# read CSV file
occupations = open("occupations.csv", "r")
data = occupations.readlines()
occupations.close()

current_total = 0
percent_dict = {}
#for each row of data except heading and last row
for i in range(1, len(data)-1):
    #if occupation is between quotation marks
    if data[i][0] == '"':
        data_set = data[i].split('",')
        title = data_set[0][1:]
    #if only one comma separates occupation and percentage
    else:
        data_set = data[i].split(",")
        title = data_set[0]
    #store percent as number
    percent = float(data_set[1])
    #add key-value pair to dictionary
    percent_dict[round(percent + current_total, 1)] = title
    #update current_total to the next interval's end number
    current_total = current_total + percent

#return_occupation: a function that returns a randomly selected occupation where the results are weighted by the percentage given.
def return_occupation():
    #generate random number between 0 and 99.8
    rand_num = random.randrange(0,998) / 10
    #compare random number to a dictionary key until random number is less than key and occupation is returned.
    for percent in percent_dict:
        if rand_num < percent:
            return(percent_dict[percent])

print(return_occupation())
