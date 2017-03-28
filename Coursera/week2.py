"Finding Numbers in a Haystack"



import re
f = open('regex_sum_306515.txt', 'r')

sum_num = 0
for line in f:
    Line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    for num_str in stuff:
        sum_num = int(num_str) + sum_num

print 'SUM:',sum_num
   
   