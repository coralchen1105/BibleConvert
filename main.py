from striprtf.striprtf import rtf_to_text

rtf = open("nwt_E/nwt_02_Ex_E.rtf").read()
text = rtf_to_text(rtf)
lines = text.split('\n')
title = lines[0]
subString = ["Chapter", "\t"]

outlines = []

for line in lines:
    for sub in subString:
        if line.find(sub) != -1:
            outlines.append(line)


content = [x for x in lines if x not in outlines]
cleanContent = content[2:]
str1 = ''.join(cleanContent)

print(str1)

