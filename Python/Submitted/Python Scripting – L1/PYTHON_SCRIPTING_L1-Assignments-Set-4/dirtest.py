import sys
import os
import time
import datetime

# files = os.listdir('.')
# for name in files:
# 	print(name)
# 	print(os.stat(name).st_size)
# 	print(time.ctime(os.path.getmtime(name)))
# 	print(datetime.datetime.strptime(time.ctime(os.path.getmtime(name)), "%a %b %d %H:%M:%S %Y"))
# 	print()


dir_list = []
for name in os.listdir('.'):
	temp = []
	temp.append(str(datetime.datetime.strptime(time.ctime(os.path.getmtime(name)), "%a %b %d %H:%M:%S %Y")))
	temp.append(os.stat(name).st_size)
	temp.append(name)
	dir_list.append(temp)

print(dir_list)

