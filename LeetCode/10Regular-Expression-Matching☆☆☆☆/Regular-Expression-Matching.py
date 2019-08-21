# A foolish try.

def splitp(p: str):
    res = []
    tmp = ""
    for i in range(len(p)):
        if p[i] != "*" and p[i] != ".":
            tmp += p[i]
        elif p[i] == ".":
            res.append(tmp)
            res.append(p[i])
            tmp = ""
        else:
            if len(res) > 0 and res[-1] == "." and tmp == "":
                res = res[:-1]
                res.append(".*")
            else:
                res.append(tmp[:-1])
                res.append(tmp[-1]+p[i])
            tmp = ""
    res.append(tmp)
    res = [w for w in res if w != ""]
    return res

def p2gen(s: str, p: str):
    sgen = ""
    cr = 0
    presp = []
    splitedp = splitp(p)
    for k,sp in enumerate(splitedp):
        lensp = len(sp)
        if "*" in sp and "." not in sp:
            i = max(0, len(sp) - 2)
            j = 0
            gs = sp[:i]
            while j <= len(s) and s[cr:cr+i+j] == gs:
                gs = sp[:-1] + sp[-2] * j
                j += 1
            
            sgen += gs[:-1]
            cr += len(gs[:-1])
            presp.append(sp[0])
        elif "." in sp and "*" not in sp:
            sgen += sp
            cr += len(sp)
        else:
            if len(sgen) > 0 and sp[0] in presp and sp[0] == sgen[-1]:
                continue
            else:
                sgen += sp
                cr += len(sp)
    return sgen

def isMatch(s: str, p: str) -> bool:
    res = True
    if p == ".*":
        return True
    pgen = p2gen(s, p)
    print(pgen)
    gen = ""
    if ".*" not in p:
        for i in range(len(pgen)):
            if pgen[i] == ".":
                try:
                    c = s[i]
                except IndexError as e:
                    return False
            else:
                c = pgen[i]
            gen += c
        res = gen == s
    else:
        n = 0
        newp = "".join([w for w in pgen.split(".*")])
        for l in newp:
            if l == ".":
                n += 1
                continue
            else:
                if l not in s:
                    res = False
                    break
        if n > len(s):
            res = False
    return res