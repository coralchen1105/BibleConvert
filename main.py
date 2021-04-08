import re
from striprtf.striprtf import rtf_to_text

rtf = open("nwt_E.rtf/nwt_02_Ex_E.rtf").read()
text = rtf_to_text(rtf)
lines = text.split('\n')
title = lines[0]
subString1 = "Chapter"
subString2 = "\t"
testList = []

for line in lines:
    if line.find(subString2) == -1:
        testList.append(line)


def check_num_chapter():
    num = 0
    for e in testList:
        if subString1 in e:
            num = num + 1

    return num


chapterNum: int = int(check_num_chapter() / 2)

testList = testList[chapterNum + 2:]
print(testList)
str1 = ''.join(testList)

print(str1)


