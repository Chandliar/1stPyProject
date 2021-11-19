import re
import os
ifconfig_result = os.popen('ifconfig '+'wifi0').read()

ipv4_add = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[0]
netmask = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[1]
broadcast = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[2]
mac_addr = re.findall(r'([\w\d]{2}:[\w\d]{2}:[\w\d]{2}:[\w\d]{2}:[\w\d]{2}:[\w\d]{2})',ifconfig_result)[0]

format_string = '{0:<10}:{1:<30}'
print(format_string.format('ipv4_add',ipv4_add))
print(format_string.format('netmask',netmask))
print(format_string.format('broadcast',broadcast))
print(format_string.format('mac_addr',mac_addr)+'\n')

gw_last_dig = str(input('请输入网关IP最后一位:'))
ipv4_gw = str(re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.)',ipv4_add).group()) + gw_last_dig
print('\n网关IP地址最后一位为{}，因此网关IP地址为：'.format(gw_last_dig) + ipv4_gw + '\n')
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()
re_ping_result = re.findall(r'1 received', ping_result)
if re_ping_result:
    print("网关可达!")
else:
    print("网关不可达!")
