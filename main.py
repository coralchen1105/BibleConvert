import re
from striprtf.striprtf import rtf_to_text
# open one rtf file and read into text, split with \n into list
rtf = open("nwt_E/nwt_01_Ge_E.rtf", encoding='UTF-8', errors='ignore').read()
text = rtf_to_text(rtf)
lines = text.split('\n')

title = lines[0]

# create subString list to remove the lines contain subString
subString = ["Chapter", "("]

outlines = []

# outlines and chapter lines into list
for line in lines:
    for sub in subString:
        if line.find(sub) != -1:
            outlines.append(line)

# get the different elements from two list (lines, outlines)
content = [x for x in lines if x not in outlines]
cleanContent = content[2:]

print(cleanContent)

# test to find "\xa0"
for e in cleanContent:
    x = re.search("\xa0", e)
    if x:
        print("found")

# join the whole list (remove outline, title, and chapter) into one string
str1: str = ''.join(cleanContent)

# to-do: use regex to split all scripts into a list, means each script(with script number) will be an element
y = re.search("\xa0", str1)


