# Team Smooth Brain - Helena Williams, May Hathaway, Ryan Ma
# SoftDev
# K10 -- Putting Little Pieces Together -- Flask + K07
# 2020-10-13

import random
from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def master():
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
    rand_num = random.randrange(0,998) / 10
    occupation_list = ""
    for x in percent_dict:
        occupation_list += percent_dict[x]
        occupation_list += "<br>"
    # print(occupation_list) -- used for testing
    for percent in percent_dict:
        if rand_num < percent:
            return("Made by Team Smooth Brain: May Hathaway, Helena Williams, Ryan Ma <br><br>" +
            "Chosen Occupation: " + percent_dict[percent] + "<br><br>" + occupation_list)

app.run()
