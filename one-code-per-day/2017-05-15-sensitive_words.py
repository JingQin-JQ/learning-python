# -*- coding: utf-8 -*-

'''
敏感词文本文件 filtered_words.txt，
里面的内容为以下内容（"北京 程序员 公务员 领导 牛比 牛逼 你娘 你妈 love sex jiangge"，
当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

2017-05-15 
Jing Qin

'''
import sys

def sensitive_words(filtered_file):
    # read file and save it as a sensitive_words list
    with open(filtered_file, 'r') as f:
        lines =f.read()
        sensitive_words = lines.split()
    return sensitive_words

def test_words(test_file):
    #read from input, if there is word in the sensitive_words list print "Freedom",otherwise print"Human Rights"
    with open(test_file, 'r') as t:
        lines =t.read()
        test_words = lines.split()
    return test_words


def filter_sensitive_word(filtered_file,test_file):
    '''
     Get filtered_file and test_file as arguments of function "replace_sensitive_word",
     call function "test_words" and "sensitive_words" inside. 
     Since the "sensitive_words" function will be called multiple times, 
     in order to improve efficiency, the output of the function is pre-assigned 
     to the variable “sensitive_words_list”。

    '''
    sensitive = False
    sensitive_words_list = sensitive_words(filtered_file)
    for ch in test_words(test_file):
        if ch in sensitive_words_list:
            sensitive = True
            break
    if sensitive:
        print "Freedom"
    else:
        print "Human Rights"
        

if __name__ == '__main__':
    filter_sensitive_word(sys.argv[1],sys.argv[2])   