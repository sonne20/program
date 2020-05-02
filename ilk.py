import time
import re

for i in range(5):
	print('Hello Kemal')
	time.sleep(1)
#deneme2	
#deneme2
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(0) : ", matchObj.group(2))
else:
   print('No match!!')
