import json, random
with open('birthdays.json') as data_file:
  brithdayData = json.load(data_file)

def getDayAndMonth(birthday):
  return " ".join(birthday.split()[:2])

birthIdRange = len(brithdayData)
testedBirthdays = []

for i in range(1, 43):
  randomId = random.randint(1, birthIdRange)
  for tested in testedBirthdays:
    if getDayAndMonth(brithdayData[randomId]['db']) == getDayAndMonth(tested['db']):
      print("Found a match")
      print(brithdayData[randomId])
      print("And")
      print(tested)
      print()
      break
  testedBirthdays.append(brithdayData[randomId])

print("Exiting")

