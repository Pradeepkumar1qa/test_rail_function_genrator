from testrail import *
import re as Regex


def getdata():
	with open('config.txt') as f:
		l=f.readlines()

	username=l[0].split("=")[1].replace("\n","").strip()
	password=l[1].split("=")[1].strip()
	return username,password

usrname,password=getdata()



client = APIClient('https://mnv.testrail.com')
client.user =str(usrname)
client.password =str(password)

alltestcases= client.send_get('get_cases/30/&suite_id=1925')
# testrun=client.send_get('get_projects/')
# print(case)



def sanitizeString(l,testid):

      l=Regex.sub("[^0-9a-zA-Z]+",'_', l.strip())

      # print(testid)
      l='@DbMapper(testcaseid={"'+str(testid)+'"})\n public void '+l
      # l[i]=Regex.sub("()$",'()\n{}\n',l[i])
      l=l+'()\n{}\n'
      print(l)

      return l

for testcase in alltestcases:
	sanitizeString(testcase['title'], testcase['id'])


# client.send_post('add_run/30',{
# 	"suite_id": 1925,
# 	"name": "This is a new test run created by automation",
# 	"assignedto_id": 5
# 	})

# client.send_post('add_milestone/30',{
# 	"name": "Release created by automation.0"
#
# })


