department1 = 'security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_PYTHON = 1234.3456

# line1 = "Department1 name:%-10s Manager:%-10s COURSE FEES:%-20s The End!" %(department1,depart1_m,COURSE_FEES_SEC)
# line2 = "Department2 name:%-10s Manager:%-10s COURSE FEES:%-20s The End!" %(department2,depart2_m,COURSE_FEES_PYTHON)

line1 = "Department1 name:{:10} Manager:{:10} COURSE FEES:{:<20} The End!" .format(department1,depart1_m,COURSE_FEES_SEC)
line2 = "Department2 name:{:10} Manager:{:10} COURSE FEES:{:<20} The End!" .format(department2,depart2_m,COURSE_FEES_PYTHON)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)

