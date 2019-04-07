##!/user/bin/env python
## coding = utf-8

import jieba
from gensim.models import word2vec
import os
import time
import sys

filePath = 'E:\dataset\sogou.txt'
fileSegWordDonePath = 'E:\dataset\sogouSegDone.txt'
# read the file by line
fileTrainRead = []
# fileTestRead = []
with open(filePath, errors='ignore') as fileTrainRaw:
    for line in fileTrainRaw:
        fileTrainRead.append(line)
# define this function to print a list with chinese
def PrintListChinese(list):
    for i in range(len(list)):
        print(list[i])
#segment word with jieba
fileTrainSeg=[]
for i in range(len(fileTrainRead)):
    fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i],cut_all=False)))])
    if i%100 == 0:
        print(i)

#to test the segment result
#PrintListChinese(fileTrainSeg[10])

#save the result
with open(fileSegWordDonePath, 'wb') as fw:
    for i in range(len(fileTrainSeg)):
        fw.write((fileTrainSeg[i][0].encode("utf-8")))
        fw.write('\n'.encode("utf-8"))

