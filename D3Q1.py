import re
str1 = '166 54a2.74f7.0726 DYNAMIC Gi1/0/11'
key_value = re.match('(\d{1,4})\s+([\d\w]+\.[\d\w]+\.[\d\w]+)\s+(\w+)\s+(\w+\/\w\/\w)',str1).groups()
print(key_value)
print("VLANID     :{}".format(key_value[0]))
print("MAC        :{}".format(key_value[1]))
print("TYPE       :{}".format(key_value[2]))
print("Interface  :{}".format(key_value[3]))
