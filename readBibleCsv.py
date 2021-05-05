import re
from striprtf.striprtf import rtf_to_text
from filedata import files1
from filedata import files2
from filedata import files3
from filedata import John_file
import pandas as pd

scriptures = []
subString = ["^Chapter", "\(\d+\-\d+\)", "\(\d+\, \d+\)", "\(\d+\)", "\t"]


# Raw data processing
def open_file(file):
    rtf = open(file, encoding='UTF-8', errors='ignore').read()
    text = rtf_to_text(rtf)
    return text.split('\n')


def clean_up(lines):
    outlines = []
    for line in lines:
        for sub in subString:
            if re.search(sub, line):
                outlines.append(line)
    content = [x for x in lines if x not in outlines]
    cleanContent = content[2:]
    return cleanContent


def each_file_scripts(content):
    str1: str = ''.join(content)
    return re.split("\d+\xa0", str1)


def process(file) -> object:
    lines = open_file(file)
    cleanContent = clean_up(lines)
    scripts = each_file_scripts(cleanContent)
    scripts.pop(0)
    for s in scripts:
        scriptures.append(s)


def process_john(file):
    lines = open_file(file)
    cleanContent = clean_up(lines)
    scripts = each_file_scripts(cleanContent)
    scripts.pop(0)
    for index in range(336, 348):
        scripts.insert(index, "")
        index + 1
    return scripts


def get_all_scripts(files):
    for file in files:
        process(file)

# all rtf files before Mark
get_all_scripts(files1)

# add 12 null data at the end of Mark 16:8, as Mark has 12 scriptures less
i = 0
for i in range(12):
    scriptures.append("")

# process data in files2, which has normal data after Mark
get_all_scripts(files2)

# need to correct John scriptures as NWT lose John 7:53, John 7:1-11
# insert 12 null elements at index
# then process corrected John file

John_scripts = []
John_scripts = process_john(John_file)

for s in John_scripts:
    scriptures.append(i)

# process data in file3 after John as the rest of files are all match
get_all_scripts(files3)

print(len(scriptures))

# df = pd.read_csv('bibles.txt', delimiter="\t")
# df["new world translation"] = ""
# df.insert(loc=12, column="new world translation", value=scriptures)
# df.to_csv('bibles.txt', index=False)
