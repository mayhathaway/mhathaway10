# May Hathaway (with Erin Lee and Victoria Gao — Team Burgers)
# SoftDev
# K06 — Learnination through amalgamation: creating optimized version of K05
# 2020-10-02


from random import choice

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

def get_random_name():
    #list out team name options for user
    print("Team names: orpheus, rex, endymion!\n")
    #get input for team name from user, lowercase to match KREWES
    name = input("Enter a team:\n").lower()
    #if the user's input doesn't match the keys in KREWES, then ask again until it does
    while name not in KREWES:
        name = input("Please Enter a correct team:\n").lower()
    #print a random name from the selected team
    print(choice(KREWES[name]))

if __name__ == "__main__":
    get_random_name()
