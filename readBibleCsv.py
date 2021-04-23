import re
from striprtf.striprtf import rtf_to_text
import pandas as pd

scriptures = []
subString = ["^Chapter", "\(\d+\-"]


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


def process(file):
    lines = open_file(file)
    cleanContent = clean_up(lines)
    scripts = each_file_scripts(cleanContent)
    scripts.pop(0)
    for s in scripts:
        scriptures.append(s)


files = ["nwt_E/nwt_01_Ge_E.rtf", "nwt_E/nwt_02_Ex_E.rtf", "nwt_E/nwt_03_Le_E.rtf", "nwt_E/nwt_04_Nu_E.rtf",
         "nwt_E/nwt_05_De_E.rtf", "nwt_E/nwt_06_Jos_E.rtf", "nwt_E/nwt_07_Jg_E.rtf", "nwt_E/nwt_08_Ru_E.rtf",
         "nwt_E/nwt_09_1Sa_E.rtf", "nwt_E/nwt_10_2Sa_E.rtf","nwt_E/nwt_11_1Ki_E.rtf","nwt_E/nwt_12_2Ki_E.rtf",
         "nwt_E/nwt_13_1Ch_E.rtf", "nwt_E/nwt_14_2Ch_E.rtf", "nwt_E/nwt_15_Ezr_E.rtf"]

files_backup = ["nwt_E/nwt_16_Ne_E.rtf",

         "nwt_E/nwt_17_Es_E.rtf", "nwt_E/nwt_18_Job_E.rtf", "nwt_E/nwt_19_Ps_E.rtf", "nwt_E/nwt_20_Pr_E.rtf"
         ]


def get_all_scripts(files):
    for file in files:
        process(file)


get_all_scripts(files)

print(len(scriptures))

# df = pd.read_csv('bibleTest.csv')
# df["new world translation"] = ""
# df.to_csv('bibleTest.csv', index=False)
# print(df.head())
