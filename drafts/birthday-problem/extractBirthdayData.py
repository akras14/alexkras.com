import json
txt = open('/Users/alexk/biographies.list', encoding = "ISO-8859-1")
text = txt.read()
textDict = text.split("-------------------------------------------------------------------------------")
result = []
for test in textDict:
    if "DB:" in test and "NM:" in test:
        validBD = True
        actor = {}
        formatedTest = test.split('\n');
        for string in formatedTest:
          if "DB:" in string:
            dbString = string[4:]
            dbString = dbString.split(',')
            dbString = dbString[0]
            if len(dbString.split()) == 3:
              actor['db'] = dbString
            else:
              validBD = False
          if "NM:" in string:
            actor['name'] = string[4:]
        if validBD == True:
          result.append(actor)

with open('birthdays.json', 'w') as outfile:
  json.dump(result, outfile)
