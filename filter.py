from collections import OrderedDict
from operator import itemgetter

f = open('slab-without-whitespace', 'r', encoding='utf-8')
data = f.readlines()
f.close()

lines = []
all_data = []

for line in data:
    lines.append(line)


for line in lines:
   if line.find('192') > 0:
       line_in_list = line.strip().split()
       index = lines.index(line)
       count = int(line_in_list[-1])
       time = 0
       find_Process = False
       while not find_Process:
           time = time + 1
           if not lines[index - time].find('Process'):
               find_Process = True
               correct_line = lines[index - time]
               pid_list = correct_line.split()
               pid = pid_list[6]
               all_data.append((pid, count))

add_count = {}
for data in all_data:
    if data[0] not in add_count:
        add_count[data[0]] = data[1]
    elif data[0] in add_count:
        add_count[data[0]] += data[1]
print(add_count)


f = open('sorted_file', 'w', encoding='utf-8')
for key, value in sorted(add_count.items(), key = itemgetter(1), reverse = True):
    print(key, value,file=f)
f.close()
#








