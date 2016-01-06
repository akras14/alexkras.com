import json, random

# Load birthdays
with open('birthdays.json') as data_file:
  brithdayData = json.load(data_file)

# Get day and month from the birthday string
def getDayAndMonth(birthday):
  return " ".join(birthday.split()[:2])

birthIdRange = len(brithdayData)

def oneRun(numToSample):
  testedBirthdays = []
  matchFound = False
  for i in range(0, numToSample):
    randomId = random.randint(0, birthIdRange - 1)
    for tested in testedBirthdays:
      randomBirthdayDate = getDayAndMonth(brithdayData[randomId]['db'])
      testedDate = getDayAndMonth(tested['db'])
      if randomBirthdayDate == testedDate:
        matchFound = True
        # print("Found a match")
        # print(brithdayData[randomId])
        # print("And")
        # print(tested)
        # print()
    if(matchFound == True):
      return matchFound
    else:
      testedBirthdays.append(brithdayData[randomId])
  return matchFound

# Kick off the test
def runABatch():
  matchesFound = 0
  for i in range(0, 1000):
    if oneRun(70) == True:
      matchesFound += 1
  return matchesFound*100/1000

total = 0
for i in range(0,10):
  total += runABatch()
  print(i)

print("Percentage match " + str(total/10))
