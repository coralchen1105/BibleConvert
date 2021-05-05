import re
from striprtf.striprtf import rtf_to_text
import pandas as pd

scriptures = []
subString = ["^Chapter", "\(\d+\-\d+\)", "\(\d+\, \d+\)", "\(\d+\)", "\t"]


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


# rtf files include up to Mark as NWT version has 12 scripts less than others
files1 = ["nwt_E/nwt_01_Ge_E.rtf", "nwt_E/nwt_02_Ex_E.rtf", "nwt_E/nwt_03_Le_E.rtf", "nwt_E/nwt_04_Nu_E.rtf",
          "nwt_E/nwt_05_De_E.rtf", "nwt_E/nwt_06_Jos_E.rtf", "nwt_E/nwt_07_Jg_E.rtf", "nwt_E/nwt_08_Ru_E.rtf",
          "nwt_E/nwt_09_1Sa_E.rtf", "nwt_E/nwt_10_2Sa_E.rtf", "nwt_E/nwt_11_1Ki_E.rtf", "nwt_E/nwt_12_2Ki_E.rtf",
          "nwt_E/nwt_13_1Ch_E.rtf", "nwt_E/nwt_14_2Ch_E.rtf", "nwt_E/nwt_15_Ezr_E.rtf", "nwt_E/nwt_16_Ne_E.rtf",
          "nwt_E/nwt_17_Es_E.rtf", "nwt_E/nwt_18_Job_E.rtf", "nwt_E/nwt_19_Ps_E.rtf", "nwt_E/nwt_20_Pr_E.rtf",
          "nwt_E/nwt_21_Ec_E.rtf", "nwt_E/nwt_22_Ca_E.rtf", "nwt_E/nwt_23_Isa_E.rtf", "nwt_E/nwt_24_Jer_E.rtf",
          "nwt_E/nwt_25_La_E.rtf", "nwt_E/nwt_26_Eze_E.rtf", "nwt_E/nwt_27_Da_E.rtf", "nwt_E/nwt_28_Ho_E.rtf",
          "nwt_E/nwt_29_Joe_E.rtf", "nwt_E/nwt_30_Am_E.rtf", "nwt_E/nwt_31_Ob_E.rtf", "nwt_E/nwt_32_Jon_E.rtf",
          "nwt_E/nwt_33_Mic_E.rtf", "nwt_E/nwt_34_Na_E.rtf", "nwt_E/nwt_35_Hab_E.rtf", "nwt_E/nwt_36_Zep_E.rtf",
          "nwt_E/nwt_37_Hag_E.rtf", "nwt_E/nwt_38_Zec_E.rtf", "nwt_E/nwt_39_Mal_E.rtf", "nwt_E/nwt_40_Mt_E.rtf",
          "nwt_E/nwt_41_Mr_E.rtf"
          ]

files2 = ["nwt_E/nwt_42_Lu_E.rtf"]
John_file = "nwt_E/nwt_43_Joh_E.rtf"
files3 = ["nwt_E/nwt_44_Ac_E.rtf", "nwt_E/nwt_45_Ro_E.rtf", "nwt_E/nwt_46_1Co_E.rtf", "nwt_E/nwt_47_2Co_E.rtf",
          "nwt_E/nwt_48_Ga_E.rtf","nwt_E/nwt_49_Eph_E.rtf", "nwt_E/nwt_50_Php_E.rtf", "nwt_E/nwt_51_Col_E.rtf",
          "nwt_E/nwt_52_1Th_E.rtf", "nwt_E/nwt_53_2Th_E.rtf", "nwt_E/nwt_54_1Ti_E.rtf", "nwt_E/nwt_55_2Ti_E.rtf",
          "nwt_E/nwt_56_Tit_E.rtf", "nwt_E/nwt_57_Phm_E.rtf", "nwt_E/nwt_58_Heb_E.rtf", "nwt_E/nwt_59_Jas_E.rtf",
          "nwt_E/nwt_60_1Pe_E.rtf", "nwt_E/nwt_61_2Pe_E.rtf", "nwt_E/nwt_62_1Jo_E.rtf", "nwt_E/nwt_63_2Jo_E.rtf",
          "nwt_E/nwt_64_3Jo_E.rtf", "nwt_E/nwt_65_Jude_E.rtf", "nwt_E/nwt_66_Re_E.rtf"]


def get_all_scripts(files):
    for file in files:
        process(file)


def process_john(file):
    lines = open_file(file)
    cleanContent = clean_up(lines)
    scripts = each_file_scripts(cleanContent)
    scripts.pop(0)
    for index in range(336, 348):
        scripts.insert(index, "")
        index + 1
    return scripts


get_all_scripts(files1)


# add 12 null data at the end of Mark 16:8
i = 0
for i in range(12):
    scriptures.append("")

get_all_scripts(files2)


# need to correct John scriptures as NWT lose 7:53, 7:1-11
# insert 12 null elements at index

John_scripts = []
John_scripts = process_john(John_file)

for s in John_scripts:
    scriptures.append(i)

get_all_scripts(files3)

print(len(scriptures))

# df = pd.read_csv('bibles.txt', delimiter="\t")
# df["new world translation"] = ""
# df.insert(loc=12, column="new world translation", value=scriptures)
# df.to_csv('bibles.txt', index=False)
