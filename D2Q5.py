import re
str1 = 'Port-channel1.189 192.168.189.254 YES CONFIG up'
Important = re.match('^([A-Z]\w*.\w+.\d+)\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s\w+\s\w+\s(\w+)',str1).groups()
print('接口     :{0:10}'.format(Important[0]))
print('IP地址   :{0:10}'.format(Important[1]))
print('状态     :{0:10}'.format(Important[2]))


