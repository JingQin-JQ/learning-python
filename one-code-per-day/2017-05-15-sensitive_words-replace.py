# -*- coding: utf-8 -*-

'''
敏感词文本文件 filtered_words.txt，
里面的内容为以下内容（"北京 程序员 公务员 领导 牛比 牛逼 你娘 你妈 love sex jiangge"，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

2017-05-15 
Jing Qin

'''
import string
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

def replace_sensitive_word(filtered_file,test_file):
    '''
     Get filtered_file and test_file as arguments of function "replace_sensitive_word",
     call function "test_words" and "sensitive_words" inside. 
     Since sensitive words only contain English and Chinese,
     so the length of the none-English word (Chinese)will be divided by 3 
     to get the correct number of characters.
    '''
    new_line = ""
    sensitive = False
    sensitive_words_list = sensitive_words(filtered_file)
    for word in test_words(test_file):
        chinese = False
        len_word = len(word)
        replaced_word = word
            
        if word in sensitive_words_list:
            for ch in word:
                if ch  not in string.ascii_letters:
                    chinese = True
                    break
            if chinese:
                replaced_word = (len_word/3)*"*"
            else:
                replaced_word = len_word*"*"
    
        new_line =new_line + replaced_word +" "
    print new_line
        


if __name__ == '__main__':
    replace_sensitive_word(sys.argv[1],sys.argv[2])   
