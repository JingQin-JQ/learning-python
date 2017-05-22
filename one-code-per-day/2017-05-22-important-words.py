# -*- coding: utf-8 -*-
'''
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

2017-05-22 
Jing Qin
'''

import re
import os
import os.path
import sys
from collections import Counter
from stop_words import get_stop_words

# The directory where the target file is located
#FILE_PATH = '/Users/jingqin/Github/learning-python/one-code-per-day'

def getCounter(filename):
    '''Enter an English plain text file that counts the number of words in which the word appears'''
    pattern = re.compile('[A-Za-z]+|\$?\d+%?$')
    with open(filename) as f:
        r = re.findall(pattern, f.read())
        return Counter(map(str.lower,r))

  

def run(directory):
    '''
    Get "directory" as arguments of function "run",
     find txt file, call function "getCounter" to counts the number of words.
    '''
    for root, dirs, files in os.walk(directory):
        for name in files:
            if os.path.splitext(name)[1] == '.txt':
                print('')
                print os.path.splitext(name)[0],".txt :"
                # Exclude the effect of stopword
                each_counter = getCounter(name)
                for i in get_stop_words('en'):
                    each_counter[i] = 0
                for i in range(10):
                    if each_counter.most_common()[i][1] != 0:
                        print each_counter.most_common()[i] 

if __name__ == '__main__':
    run(sys.argv[1])