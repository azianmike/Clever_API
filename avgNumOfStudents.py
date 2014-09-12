__author__ = 'michaelluo'

import requests
import json

#Gets a list of sections you have access to
#seems like the sections include students and num of students
r = requests.get('https://api.clever.com/v1.1/sections', headers={'Authorization':'Bearer DEMO_TOKEN'})
dataObj = json.loads(r.text)
sections = dataObj['data'] #Assume that each entry is one unique section
allStudents = 0
for section in sections:
    allStudents += len(section['data']['students'])  #count length of 'students' list

print 'Total students: ' + str(allStudents)
print 'Total sections: ' + str(len(sections))
print 'Avg number of students in section: ' + str((allStudents+0.0)/len(sections))
