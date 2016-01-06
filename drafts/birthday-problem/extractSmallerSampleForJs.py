#! /usr/bin/env python3
#
# TODO cleanup logic, this is a mess
import json
txt = open('/Users/alexk/biographies.list', encoding = "ISO-8859-1")
text = txt.read()
# Split by actor
textDict = text.split("-------------------------------------------------------------------------------")
result = []
for test in textDict:
    if "DB:" in test and "NM:" in test: # Only pick actors with both Date of birth and Name set
        validBD = True
        actor = {}
        formatedTest = test.split('\n');
        for string in formatedTest: # For every line in actor
          if "DB:" in string: # If it's a Date of birth line
            dbString = string[4:] #Remove the prefix
            dbString = dbString.split(',') #Split to get actual date of birth before first comma
            dbString = dbString[0]
            dbString = dbString.split() #Split by Month Day Year
            if len(dbString) == 3: # If has math day and year
              try:
                year = int(dbString[2])
                if year > 1982 and year < 1986: #If fairly recent
                  # Join back to save space
                  actor['db'] = " ".join(dbString)
                else:
                  validBD = False
              except:
                validBD = False
            else:
              validBD = False
          if "NM:" in string: # If it's a name line
            actor['name'] = string[4:]
        if validBD == True:
          result.append(actor)

with open('birthdays-smaller.json', 'w') as outfile:
  json.dump(result, outfile)
