# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 22:37:34 2017

@author: ldh
"""

# document_helper.py
import os

def clean_file(directory,suffix):
    '''
    清除指定目录下，带有指定后缀的文件。
    '''
    if directory[-1] != '\\':
        directory = directory + '\\'
    name_list = os.listdir(directory)
    dir_list = []
    file_list = []
    
    for each in name_list:
        if os.path.isdir(directory + each):
            dir_list.append(each)
        else:
            file_list.append(each)
    
    for each in file_list:
        if os.path.splitext(each)[1] == suffix:
            os.remove(directory + each)
            print '清除文件%s'%(directory + each)
        else:
            continue
        
    for each in dir_list:
        clean_file(directory + each,suffix)
        

if __name__ == '__main__':
    directory = 'G:\Work_ldh\Backtest\VectorTrader'
    suffix = '.pyc'
    a = clean_file(directory,suffix)