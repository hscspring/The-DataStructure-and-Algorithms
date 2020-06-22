import re
import locale
import pnlp

pcomp = re.compile(r'[⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻]')
NEED_PRON = ["kHanyuPinyin", "kCantonese",
             "kKorean", "kJapaneseOn", "kVietnamese"]

########## Pronunciation ##########


def get_pron_rawdict(fp: str):
    lines = pnlp.read_lines(fp)
    dct = {}
    for line in lines:
        if line.startswith("#"):
            continue
        unic, lang, pron = line.strip().split("\t")
        if unic not in dct:
            dct[unic] = {}
        dct[unic][lang] = pron
    return dct


def get_pron_dict(pron_rawdict: dict):
    res = {}
    for unic in pron_rawdict:
        prons = []
        for need in NEED_PRON:
            pron = pron_rawdict[unic].get(need, "null")
            pron = ",".join(pron.split())
            if need == "kHanyuPinyin":
                pron = pron.split(":")[-1]
            prons.append(pron)
        res[unic] = ";".join(prons)
    return res


########## Composition ##########


def get_char_and_comp_rawdict(fp: str):
    lines = pnlp.read_lines(fp)
    char_dct = {}
    comp_dct = {}
    for line in lines:
        if line.startswith("#"):
            continue
        item = line.strip().split("\t")
        unic = item[0]
        char = item[1]
        comp = item[2:]
        if unic not in char_dct:
            char_dct[unic] = {}
        if char not in comp_dct:
            comp_dct[char] = {}
        char_dct[unic] = char
        comp_dct[char] = comp
    return char_dct, comp_dct


def get_comp_dict(char_dict: dict, comp_rawdict: dict):
    res = {}
    for unic in char_dict:
        char = char_dict[unic]
        tmp = []
        for val in comp_rawdict.get(char):
            lst = []
            get_comp(comp_rawdict, val, lst)
            com = "".join(lst)
            tmp.append(com)
        res[unic] = ",".join(tmp)
    return res


########## utils ##########

def split_comp_parts(s: str):
    starts = []
    for m in pcomp.finditer(s):
        starts.append(m.start())
    res = []
    tmp = []
    if not starts:
        return [s]
    begin = starts.pop(0)
    for i, c in enumerate(s):
        if i == begin:
            if tmp:
                res.append("".join(tmp))
                tmp = []
            res.append(c)
            if starts:
                begin = starts.pop(0)
        else:
            tmp.append(c)
    if tmp:
        res.append("".join(tmp))
    return res


def get_comp(comp_rawdict: dict, s: str, res: list):
    parts = split_comp_parts(s)
    for key in parts:
        # 组成标记，或纯字符串，直接返回
        if pcomp.search(key) or (len(parts) == 1 and not pcomp.search(key)):
            res.append(key)
            continue
        tmp = []
        for p in key:
            if p == key:
                res.append(key)
                continue
            vals = comp_rawdict.get(p)
            if not vals:
                tmp.append(p)
            else:
                if tmp:
                    res.append("".join(tmp))
                    tmp = []
                # 只算了第一个
                nxt = vals[0]
                get_comp(comp_rawdict, nxt, res)
        if tmp:
            res.append("".join(tmp))


########## Combine ##########


def get_char_meta(char_dict: dict, pron_dict: dict, comp_dict: dict):
    res = []
    for unic in INTER_UNICODES:
        char = char_dict[unic]
        pron = pron_dict[unic]
        comp = comp_dict[unic]
        line = "\t".join([unic, char, pron, comp])
        res.append(line)
    return res


pron_file = "dict/Unihan_Readings.txt"
comp_file = "dict/ids.txt"

pron_rawdict = get_pron_rawdict(pron_file)
pron_dict = get_pron_dict(pron_rawdict)
print(f"Pronunciation dict length: {len(pron_dict)}.")

char_dict, comp_rawdict = get_char_and_comp_rawdict(comp_file)
comp_dict = get_comp_dict(char_dict, comp_rawdict)
assert len(char_dict) == len(comp_rawdict) == len(comp_dict)
print(f"Composition dict length: {len(comp_dict)}.")

intersection = set(pron_dict.keys()) & set(char_dict.keys())
INTER_UNICODES = sorted(
    intersection, key=lambda x: (len(x), locale.strxfrm(x)))
print(f"Intersection dict length: {len(INTER_UNICODES)}.")

char_meta = get_char_meta(char_dict, pron_dict, comp_dict)
pnlp.write_file("char_meta.txt", char_meta)
