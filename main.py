import re
from striprtf.striprtf import rtf_to_text

rtf = open("nwt_E.rtf/nwt_01_Ge_E.rtf").read()
text = rtf_to_text(rtf)
lines = text.split('\n')
title = lines[0]
subString = ["Chapter", "\t"]

outlines = []
testList2 = []

for line in lines:
    for sub in subString:
        if line.find(sub) != -1:
            outlines.append(line)


content = [x for x in lines if x not in outlines]
cleanContent = content[2:]
str1 = ''.join(cleanContent)

print(str1)

