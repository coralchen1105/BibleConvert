import re
from striprtf.striprtf import rtf_to_text
# open one rtf file and read into text, split with \n into list
rtf = open("nwt_E/nwt_01_Ge_E.rtf", encoding='UTF-8', errors='ignore').read()
text = rtf_to_text(rtf)
lines = text.split('\n')

title = lines[0]

# create subString list to remove the lines contain subString
subString = ["^Chapter", "\(\d+"]

outlines = []

# outlines and chapter lines into list
for line in lines:
    for sub in subString:
        if re.search(sub, line):
            outlines.append(line)

# get the different elements from two list (lines, outlines)
content = [x for x in lines if x not in outlines]
cleanContent = content[2:]

print(cleanContent)

# join the whole list (remove outline, title, and chapter) into one string
str1: str = ''.join(cleanContent)


# to-do: use regex to split all scripts into a list, means each script(with script number) will be an element
y = re.split("\d+\xa0", str1)
i = 0
for e in y:
    i = i+1
    print(str(i) + e)




