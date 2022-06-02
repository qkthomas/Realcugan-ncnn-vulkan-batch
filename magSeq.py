#!/usr/bin/env python3

factorLst = [2, 3, 4]
sepStr = ":"
resMap = {}

def lstToStr(lst):
    strVal = sepStr.join([str(x) for x in lst])
    # print(strVal)
    return strVal

def strTolst(str):
    numLst = []
    strLst = str.split(sepStr)
    for str in strLst:
        numLst.append(int(str))
    return numLst

def calMagSeq(scale, resPrev: list):
    if scale <= 1:
        # no need to upscale. save the result
        resPrev.sort()
        resMap[lstToStr(resPrev)] = True
        return
    for factor in factorLst:
        cpyResPrev = []
        for ele in resPrev:
            cpyResPrev.append(ele)
        cpyResPrev.append(factor)
        calMagSeq(scale/factor, cpyResPrev)

emptyLst = []
calMagSeq(4, emptyLst)
print(resMap.keys())