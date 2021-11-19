
import re
str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

# key = re.split('[ ,]',str1)
# key.pop(-3)
# key.pop(-5)
# key.pop(-7)
# time = key[-5].split(":")
# time_Chinese = time[0]+"小时"+time[1]+"分钟"+time[2].strip(",")+"秒"
# print("{0:<20}:  {1:<10}".format("protocol",key[0]))
# print("{0:<20}:  {1:<10}".format(key[1],key[2]))
# print("{0:<20}:  {1:<10}".format(key[3],key[4]))
# print("{0:<20}:  {1:<10}".format(key[5],time_Chinese))
# print("{0:<20}:  {1:<10}".format(key[7],key[8]))
# print("{0:<20}:  {1:<10}".format(key[9],key[10]))

# str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
# key = str1.split(" ")
# time = key[-5].split(":")
# time_Chinese = time[0]+"小时"+time[1]+"分钟"+time[2].strip(",")+"秒"
# print("{0:<20}:  {1:<10}".format("protocol",key[0]))
# print("{0:<20}:  {1:<10}".format(key[1],key[2]))
# print("{0:<20}:  {1:<10}".format(key[3],key[4].strip(",")))
# print("{0:<20}:  {1:<10}".format(key[5],time_Chinese))
# print("{0:<20}:  {1:<10}".format(key[7],key[8].strip(",")))
# print("{0:<20}:  {1:<10}".format(key[9],key[10].strip(",")))



key = re.match(r'([A-Z]+)\s+\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d+)\s\w+\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}),\s\w+\s(\w):(\w+):(\w+),\s\w+\s(\d+),\s\w+\s(\w+)',str1).groups()
print(key)
print("{0:<20}:  {1:<10}".format("protocol",key[0]))
print("{0:<20}:  {1:<10}".format("Server",key[1]))
print("{0:<20}:  {1:<10}".format("localserver",key[2]))
print("{0:<20}:  {1:<0}小时{2:<0}分钟{3:<0}秒".format("idle",key[3],key[4],key[5]))
print("{0:<20}:  {1:<10}".format("bytes",key[6]))
print("{0:<20}:  {1:<10}".format("flags",key[7]))